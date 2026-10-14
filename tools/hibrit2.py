"""Hibrit emprime ayrimi v5 (acik tisort): once duz arka plandan SEFFAF kesim (alfa + renk temizligi),
sonra yazi/rozet/yildiz = tramsiz spot; fotografik obje = dagitik tram (FM) indeks ayrimi, gercek koyu mürekkep,
parlama (specular) korumasi ve yerel kontrast artirma.
Kullanim: python3 tools/hibrit2.py girdi.png cikti_klasoru [nokta_px=3] [obje_murekkep_sayisi=6]
"""
import sys, os, time, json, ctypes
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
src_path, out_dir = sys.argv[1], sys.argv[2]
DOT = int(sys.argv[3]) if len(sys.argv) > 3 else 3
NK = int(sys.argv[4]) if len(sys.argv) > 4 else 7
PPI, WCM = 600, 38.5
SPEC_L = float(os.environ.get('SPEC_L', 96.5))           # bu parlakligin ustu = mürekkep yok (parlama)
SHARP = float(os.environ.get('SHARP', 0.5))             # yerel kontrast miktari
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]", *a, flush=True)
os.makedirs(os.path.join(out_dir, "Acik_Tisort"), exist_ok=True); os.makedirs(os.path.join(out_dir, "kesim"), exist_ok=True)
NAVY = ("Lacivert", (10,45,90))
PAPER = (252,252,252)
def rgb2lab(a): return cv2.cvtColor(a.astype(np.float32)/255.0 if a.dtype==np.uint8 else a.astype(np.float32), cv2.COLOR_RGB2Lab)

# ---------- 1) seffaf kesim ----------
src = np.asarray(Image.open(src_path).convert('RGB')); sh, sw = src.shape[:2]
W = int(round(WCM/2.54*PPI)); s = W/sw; H = int(round(sh*s))
f32 = src.astype(np.float32)/255
border = np.concatenate([f32[0], f32[-1], f32[:,0], f32[:,-1]]); bgc = np.median(border, 0)
lab = rgb2lab(src); bgl = rgb2lab(np.uint8(bgc*255)[None,None,:])[0,0]
near = (np.sqrt(((lab-bgl)**2).sum(2)) < 3.5).astype(np.uint8)
n, cc = cv2.connectedComponents(near, connectivity=4)
bl = np.unique(np.concatenate([cc[0],cc[-1],cc[:,0],cc[:,-1]])); bl = bl[bl>0]
bg = np.isin(cc, bl)                                     # kenara bagli beyaz = arka plan (icerideki beyazlar kalir)
fg = ~bg
band = fg & (cv2.dilate(bg.astype(np.uint8), np.ones((5,5),np.uint8)) > 0)   # arka plana 2 px icindeki kenar kusagi
# color-to-alpha (beyaz arka plan icin): p = a*F + (1-a)*B, en kucuk gecerli a
d_dark = np.where(f32 < bgc, (bgc-f32)/np.maximum(bgc,1e-3), 0).max(2)
d_light = np.where(f32 > bgc, (f32-bgc)/np.maximum(1-bgc,1e-3), 0).max(2)
a_band = np.clip(np.maximum(d_dark, d_light), 0.0, 1.0)
alpha = np.where(bg, 0.0, np.where(band, np.maximum(a_band, 0.25), 1.0)).astype(np.float32)
Fc = np.where(band[...,None], np.clip(bgc + (f32-bgc)/np.maximum(alpha,1e-3)[...,None], 0, 1), f32)
# arka plan pikselleri icin en yakin on plan rengi (kübik buyutmede sizmasin)
lbl = cv2.distanceTransformWithLabels((~fg).astype(np.uint8)^0 if False else (bg).astype(np.uint8), cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)[1]
fgidx = np.flatnonzero(~bg.ravel()); Fflat = Fc.reshape(-1,3)
Fc = Fc.copy(); Fc[bg] = Fflat[fgidx[0]]
# basit: lbl etiketi arka plan pikseline en yakin 0 (on plan) piksel degil; once on plan koordinat tablosu
ys0, xs0 = np.where(~bg); coordmap = np.zeros(bg.shape+(2,), np.int32)
_, lab2 = cv2.distanceTransformWithLabels(bg.astype(np.uint8), cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
# lab2: sifir (on plan) piksellerin kendi etiketi; dolgu icin etiket->koordinat
fg_lab = lab2[~bg]; first = {}
for lb, y, x in zip(fg_lab.tolist(), ys0.tolist(), xs0.tolist()): first.setdefault(lb, (y,x))
by, bx = np.where(bg); 
for y, x in zip(by.tolist(), bx.tolist()):
    yy, xx = first[int(lab2[y, x])]; Fc[y, x] = Fc[yy, xx]
log('kesim: on plan %', round(100*fg.mean(),1), 'kusak px', int(band.sum()))

# bilesenler: obje / yazi-rozet
lab = rgb2lab((Fc*255).astype(np.uint8))
navy = (lab[...,2] < -8) & fg
nav_reg = cv2.dilate(navy.astype(np.uint8), np.ones((7,7),np.uint8)) > 0
rest = cv2.morphologyEx((fg & ~nav_reg).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3,3),np.uint8))
n, ccr, st, _ = cv2.connectedComponentsWithStats(rest, connectivity=8)
order = [i for i in np.argsort(-st[1:,4])+1 if st[i,4] > 1500 and min(st[i,2], st[i,3]) > 40]
big = np.where(np.isin(ccr, order), ccr, 0).astype(np.int32)
# kucuk parcalar (kopuk tuyler) en yakin buyuk bilesene baglanir; yakin kenarlar birlesmez
dist_big, nearest = cv2.distanceTransformWithLabels((big == 0).astype(np.uint8), cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
lab_to_comp = np.zeros(nearest.max()+1, np.int32); lab_to_comp[nearest[big > 0]] = big[big > 0]
assign = np.where((rest > 0) & (dist_big <= 30), lab_to_comp[nearest], 0)
bear_id = order[0]; badge_ids = order[1:]
log('bilesenler', [(int(st[i,4]), [int(v) for v in st[i,:4]]) for i in order])
bear_core = assign == bear_id; badge_core = np.isin(assign, badge_ids)
bear_m = (cv2.dilate(bear_core.astype(np.uint8), np.ones((5,5),np.uint8)) > 0) & ~badge_core
badge_m = (cv2.dilate(badge_core.astype(np.uint8), np.ones((5,5),np.uint8)) > 0) & ~bear_core
text_m = fg & ~bear_m
def save_rgba(mask, path):
    a = (alpha*mask*255).round().astype(np.uint8)
    Image.fromarray(np.dstack([(Fc*255).round().astype(np.uint8), a]), 'RGBA').save(path)
save_rgba(bear_m, os.path.join(out_dir,'kesim','ayicik_seffaf.png')); save_rgba(text_m, os.path.join(out_dir,'kesim','yazi_rozet_seffaf.png'))
log('seffaf PNG kaydedildi')

# ---------- 2) duz kisimlar: lacivert + rozet (600 PPI) ----------
wL = rgb2lab(np.array([[PAPER]], np.uint8))[0,0]
navy_L = rgb2lab(np.array([[NAVY[1]]], np.uint8))[0,0]
badge_rgb = np.median((Fc[badge_m & (lab[...,0] < 40)]*255), 0)
badge_L = rgb2lab(badge_rgb.astype(np.uint8)[None,None,:])[0,0]
Fc8 = (Fc*255).round().astype(np.uint8)
navy_f = np.zeros((H,W), bool); badge_f = np.zeros((H,W), bool)
for y0 in range(0, H, 256):
    h = min(256, H-y0)
    M = np.float32([[1/s,0,0.5/s-0.5],[0,1/s,(y0+0.5)/s-0.5]])
    kw = dict(flags=cv2.INTER_CUBIC|cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
    tl = rgb2lab(np.clip(cv2.warpAffine(Fc8, M, (W,h), **kw), 0, 255)).reshape(-1,3) - wL
    al = cv2.warpAffine(alpha, M, (W,h), **kw)
    def cover(tgt): ab = tgt-wL; return ((tl@ab)/float(ab@ab)).reshape(h,W)
    nn = dict(flags=cv2.INTER_NEAREST|cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
    rn = cv2.warpAffine(nav_reg.astype(np.uint8), M, (W,h), **nn) > 0
    rb = cv2.warpAffine(badge_m.astype(np.uint8), M, (W,h), **nn) > 0
    navy_f[y0:y0+h] = (cover(navy_L) >= 0.5) & rn & (al >= 0.5)
    badge_f[y0:y0+h] = (cover(badge_L) >= 0.5) & rb
log('duz kisimlar tamam')

# ---------- 3) obje: palet + dagitik tram ----------
ys, xs = np.where(bear_m); pad = 6
x0, x1 = max(xs.min()-pad,0), min(xs.max()+pad+1, sw); y0_, y1 = max(ys.min()-pad,0), min(ys.max()+pad+1, sh)
Cc = Fc[y0_:y1, x0:x1]; Ac = (alpha*bear_m)[y0_:y1, x0:x1]
dw, dh = int(round((x1-x0)*s/DOT)), int(round((y1-y0_)*s/DOT))
cu = np.clip(cv2.resize(Cc, (dw,dh), interpolation=cv2.INTER_CUBIC), 0, 1)
au = np.clip(cv2.resize(Ac, (dw,dh), interpolation=cv2.INTER_CUBIC), 0, 1)[...,None]
pap = np.array(PAPER, np.float32)/255
comp = cu*au + pap*(1-au)
# yerel kontrast (tuy detayi): sadece obje icinde
blur = cv2.GaussianBlur(comp, (0,0), 5.0)
comp = np.clip(comp + SHARP*(comp-blur), 0, 1)*au + pap*(1-au)
labc = rgb2lab(comp)
spec = (labc[...,0] > SPEC_L) & (au[...,0] > 0.5)           # parlama: mürekkep yok
# kucuk beyaz benekleri at (gercek parlama buyuk bilesendir): <SPEC_MIN nokta
_n, _cl, _st, _ = cv2.connectedComponentsWithStats(spec.astype(np.uint8), connectivity=8)
_keep = np.zeros(_n, bool); _keep[1:] = _st[1:,4] >= int(os.environ.get('SPEC_MIN', 20))
spec = _keep[_cl]
comp[spec] = pap
# palet: obje piksellerinden k-means; en koyu merkez = gercek en koyu bolge
sel = (au[...,0] > 0.9) & ~spec
px = labc[sel].astype(np.float32)
if len(px) > 400000: px = px[np.random.RandomState(0).choice(len(px), 400000, replace=False)]
cen = cv2.kmeans(px, NK, None, (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,80,0.1), 4, cv2.KMEANS_PP_CENTERS)[2]
cen = cen[np.argsort(cen[:,0])]
dark = px[px[:,0] <= np.percentile(px[:,0], 3)]; cen[0] = dark.mean(0)       # en koyu: gercek golge tonu
rgbp = np.clip(cv2.cvtColor(cen.reshape(1,-1,3), cv2.COLOR_Lab2RGB).reshape(-1,3), 0, 1)
bear_names = (["Siyah Kahve","Koyu Kahve","Kahve","Orta Kahve","Karamel","Acik Karamel","Krem","Ekstra"])[:NK]
bear_names = bear_names if NK >= 4 else [f"Ton {i+1}" for i in range(NK)]
BEAR = {nm: tuple(int(round(v*255)) for v in c) for nm, c in zip(bear_names, rgbp)}
# rozet mürekkebi = palette badge rengine en yakin
bdist = [np.linalg.norm(cen[i]-badge_L) for i in range(NK)]; BADGE_INK = bear_names[int(np.argmin(bdist))]
log('palet', BEAR, 'rozet:', BADGE_INK)
lin = lambda v: np.where(v <= 0.04045, v/12.92, ((v+0.055)/1.055)**2.4).astype(np.float32)
img = np.ascontiguousarray(lin(comp))
pal = np.ascontiguousarray(lin(np.vstack([pap[None], rgbp]).astype(np.float32)))
here = os.path.dirname(os.path.abspath(__file__)); so = os.path.join(here,'fs_dither.so')
if not os.path.exists(so): os.system(f'gcc -O2 -shared -fPIC -o {so} {os.path.join(here,"fs_dither.c")}')
GAM = int(os.environ.get('GAM', 1))
lib = ctypes.CDLL(so); idx = np.zeros((dh,dw), np.uint8)
lib.fs_dither(img.ctypes.data_as(ctypes.c_void_p), dh, dw, pal.ctypes.data_as(ctypes.c_void_p), len(pal), idx.ctypes.data_as(ctypes.c_void_p), GAM)
idx[spec] = 0
log('hata yayilimi bitti', idx.shape)
big = np.repeat(np.repeat(idx, DOT, 0), DOT, 1)
oy, ox = int(round(y0_*s)), int(round(x0*s)); hh, ww = min(big.shape[0], H-oy), min(big.shape[1], W-ox)
bear_idx = np.zeros((H,W), np.uint8); bear_idx[oy:oy+hh, ox:ox+ww] = big[:hh,:ww]
del big, img, comp, cu, au

# ---------- 4) filmler ----------
inks = dict(BEAR); inks[NAVY[0]] = NAVY[1]
masks = {nm: (bear_idx == i+1) for i, nm in enumerate(bear_names)}
masks[BADGE_INK] |= badge_f; masks[NAVY[0]] = navy_f
del bear_idx
lum = lambda c: rgb2lab(np.array([[c]], np.uint8))[0,0,0]
order = sorted(inks, key=lambda k: -lum(inks[k]))
def save(mask, path): Image.frombytes('1',(W,H),np.packbits(~mask,axis=1).tobytes()).save(path, dpi=(PPI,PPI), compress_level=6)
sets = []
for n_, k in enumerate(order):
    fn = f"{n_+1:02d}_{k.replace(' ','_')}.png"; save(masks[k], os.path.join(out_dir,"Acik_Tisort",fn)); sets.append([f"{n_+1:02d} {k}", fn, list(inks[k])])
    log('kaydedildi', fn, 'kapsama %', round(100*masks[k].mean(),2))
json.dump({'W':W,'H':H,'ppi':PPI,'dot_px':DOT,'sets':{'Acik_Tisort':sets}}, open(os.path.join(out_dir,'kanallar_hibrit.json'),'w'), ensure_ascii=False, indent=1)
canvas = np.zeros((H,W,3), np.uint8); canvas[:] = (250,250,250)
for k in order: canvas[masks[k]] = inks[k]
Image.fromarray(cv2.resize(canvas,(W//8,H//8),interpolation=cv2.INTER_AREA)).save(os.path.join(out_dir,'onizleme_acik.png'))
Image.fromarray(canvas).crop((0,0,W,H)).save(os.path.join(out_dir,'_tam_onizleme.png')) if False else None
np.save(os.path.join(out_dir,'_scale.npy'), np.array([s]))
# yuz kirpmalari (kaynak koordinati, 600 PPI)
def cropsrc(x0_, y0__, x1_, y1__):
    return canvas[int(y0__*s):int(y1__*s), int(x0_*s):int(x1_*s)]
import re as _re
cx=[int(v) for v in os.environ.get('CROP','390,770,500,890').split(',')]; Image.fromarray(cropsrc(*cx)).save(os.path.join(out_dir,'_kirp.png'))
Image.fromarray(cropsrc(440,700,540,780)).save(os.path.join(out_dir,'_goz.png')); Image.fromarray(cropsrc(480,820,600,900)).save(os.path.join(out_dir,'_cene.png'))
for item in os.environ.get('CROPS','').split(';'):
    if ':' in item:
        nm, bx = item.split(':'); bx = [int(v) for v in bx.split(',')]; Image.fromarray(cropsrc(*bx)).save(os.path.join(out_dir, f'_{nm}.png'))
log('BITTI')
