"""Hibrit emprime ayrimi: duz renkli kisimlar (yazi, rozet) tramsiz spot, fotografik kisim (kabarik tuy)
dagitik tram (hata yayilimi, FM) ile cok mürekkepli indeks ayrimi. Acik tisort seti.
Kullanim: python3 tools/hibrit.py girdi.png cikti_klasoru [nokta_px]
nokta_px: tram noktasi (600 PPI'da piksel). 3 px = 0.127 mm (varsayilan), 2 px = 0.085 mm (cok ince, elek/pozlama ister).
"""
import sys, os, time, json, ctypes
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
src_path, out_dir = sys.argv[1], sys.argv[2]
DOT = int(sys.argv[3]) if len(sys.argv) > 3 else 3
PPI, WCM = 600, 38.5
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]", *a, flush=True)
os.makedirs(os.path.join(out_dir, "Acik_Tisort"), exist_ok=True)

PAPER = (252, 252, 252)
BEAR = {"Krem": (237,210,173), "Karamel": (219,154,84), "Kahve": (150,98,55), "Koyu Kahve": (66,41,32)}
NAVY = ("Lacivert", (10,45,90))
BADGE_INK = "Koyu Kahve"                    # rozet duz dolgu: bu mürekkebin tamami

def rgb2lab(a): return cv2.cvtColor(a.astype(np.float32)/255.0, cv2.COLOR_RGB2Lab)
src = np.asarray(Image.open(src_path).convert('RGB')); sh, sw = src.shape[:2]
W = int(round(WCM/2.54*PPI)); s = W/sw; H = int(round(sh*s))
log('kaynak', sw, sh, 'hedef', W, H, 'nokta px', DOT)

# ---- 1) kaynak cozunurlugunde bolge analizi: lacivert / ayicik / rozet
lab = rgb2lab(src)
dpaper = np.sqrt(((lab - rgb2lab(np.array([[PAPER]], np.uint8))[0,0])**2).sum(2))
nonpaper = dpaper > 9
navy = (lab[...,2] < -8) & nonpaper
nav_reg = cv2.dilate(navy.astype(np.uint8), np.ones((7,7), np.uint8)) > 0
rest = nonpaper & ~nav_reg
rest = cv2.morphologyEx(rest.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((9,9), np.uint8))
n, cc, st, cen = cv2.connectedComponentsWithStats(rest, connectivity=8)
order = [i for i in np.argsort(-st[1:, 4]) + 1 if st[i, 4] > 1500]
bear_id = order[0]; badge_ids = order[1:]
log('bilesenler (alan):', [int(st[i,4]) for i in order])
bear_m = cv2.dilate((cc == bear_id).astype(np.uint8), np.ones((5,5), np.uint8))
badge_m = cv2.dilate(np.isin(cc, badge_ids).astype(np.uint8), np.ones((5,5), np.uint8))

# ---- 2) duz renkli kisimlar (600 PPI, alt-piksel kenar): lacivert + rozet
navy_L = rgb2lab(np.array([[NAVY[1]]], np.uint8))[0,0]; wL = rgb2lab(np.array([[PAPER]], np.uint8))[0,0]
badge_L = rgb2lab(np.array([[BEAR[BADGE_INK]]], np.uint8))[0,0]
navy_f = np.zeros((H, W), bool); badge_f = np.zeros((H, W), bool)
TH = 256
for y0 in range(0, H, TH):
    h = min(TH, H-y0)
    M = np.float32([[1/s,0,0.5/s-0.5],[0,1/s,(y0+0.5)/s-0.5]])
    kw = dict(flags=cv2.INTER_CUBIC|cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
    tl = rgb2lab(np.clip(cv2.warpAffine(src, M, (W,h), **kw), 0, 255)).reshape(-1,3) - wL
    def cover(tgt):
        ab = tgt - wL; return ((tl @ ab) / float(ab @ ab)).reshape(h, W)
    rn = cv2.warpAffine(nav_reg.astype(np.uint8), M, (W,h), flags=cv2.INTER_NEAREST|cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE) > 0
    rb = cv2.warpAffine(badge_m, M, (W,h), flags=cv2.INTER_NEAREST|cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE) > 0
    navy_f[y0:y0+h] = (cover(navy_L) >= 0.5) & rn
    badge_f[y0:y0+h] = (cover(badge_L) >= 0.5) & rb
log('duz renkli kisimlar tamam')

# ---- 3) ayicik: dagitik tram (hata yayilimi) -> indeks
ys, xs = np.where(bear_m > 0); pad = 6
x0, x1 = max(xs.min()-pad, 0), min(xs.max()+pad+1, sw); y0_, y1 = max(ys.min()-pad, 0), min(ys.max()+pad+1, sh)
crop = src[y0_:y1, x0:x1].astype(np.float32); mk = bear_m[y0_:y1, x0:x1].astype(np.float32)
f = s/DOT; log('crop', x0, x1, y0_, y1, 'f', f)
dw, dh = int(round((x1-x0)*f)), int(round((y1-y0_)*f)); log('dsize', dw, dh, crop.shape, crop.dtype)
cu = cv2.resize(crop, (dw, dh), interpolation=cv2.INTER_CUBIC); mu = cv2.resize(mk, (dw, dh), interpolation=cv2.INTER_LINEAR)
cu = np.clip(cu, 0, 255)/255.0
mu = cv2.GaussianBlur(mu, (0,0), 1.0)[..., None]
cu = cu*mu + (np.array(PAPER)/255.0)*(1-mu)               # disi = kagit
lin = lambda c: np.where(c <= 0.04045, c/12.92, ((c+0.055)/1.055)**2.4).astype(np.float32)
img = np.ascontiguousarray(lin(cu).astype(np.float32))
names_bear = list(BEAR)
palrgb = np.array([PAPER] + [BEAR[k] for k in names_bear], np.float32)/255.0
pal = np.ascontiguousarray(lin(palrgb).astype(np.float32))
here = os.path.dirname(os.path.abspath(__file__)); so = os.path.join(here, 'fs_dither.so')
if not os.path.exists(so): os.system(f'gcc -O2 -shared -fPIC -o {so} {os.path.join(here,"fs_dither.c")}')
lib = ctypes.CDLL(so)
idx = np.zeros((dh, dw), np.uint8)
lib.fs_dither(img.ctypes.data_as(ctypes.c_void_p), dh, dw, pal.ctypes.data_as(ctypes.c_void_p), len(pal), idx.ctypes.data_as(ctypes.c_void_p))
log('hata yayilimi bitti', idx.shape)
big = np.repeat(np.repeat(idx, DOT, 0), DOT, 1)
oy, ox = int(round(y0_*s)), int(round(x0*s))
hh, ww = min(big.shape[0], H-oy), min(big.shape[1], W-ox)
bear_idx = np.zeros((H, W), np.uint8); bear_idx[oy:oy+hh, ox:ox+ww] = big[:hh, :ww]
del big, img, cu, idx

# ---- 4) filmler
inks = {k: BEAR[k] for k in names_bear}; inks[NAVY[0]] = NAVY[1]
masks = {}
for i, k in enumerate(names_bear): masks[k] = (bear_idx == i+1)
masks[BADGE_INK] |= badge_f
masks[NAVY[0]] = navy_f
del bear_idx
lum = lambda c: rgb2lab(np.array([[c]], np.uint8))[0,0,0]
order = sorted(inks, key=lambda k: -lum(inks[k]))             # acik -> koyu = baski sirasi
def save(mask, path):
    Image.frombytes('1', (W,H), np.packbits(~mask, axis=1).tobytes()).save(path, dpi=(PPI,PPI), compress_level=6)
sets = []
for n, k in enumerate(order):
    fn = f"{n+1:02d}_{k.replace(' ','_')}.png"
    save(masks[k], os.path.join(out_dir, "Acik_Tisort", fn)); sets.append([f"{n+1:02d} {k}", fn, list(inks[k])])
    log('kaydedildi', fn, 'kapsama %', round(100*masks[k].mean(), 2))
json.dump({'W':W,'H':H,'ppi':PPI,'dot_px':DOT,'sets':{'Acik_Tisort':sets}}, open(os.path.join(out_dir,'kanallar_hibrit.json'),'w'), ensure_ascii=False, indent=1)

# ---- 5) onizleme
canvas = np.zeros((H, W, 3), np.uint8); canvas[:] = (250,250,250)
for k in order: canvas[masks[k]] = inks[k]
Image.fromarray(cv2.resize(canvas, (W//8, H//8), interpolation=cv2.INTER_AREA)).save(os.path.join(out_dir, 'onizleme_acik.png'))
cy, cx = int(H*0.50), int(W*0.45)
Image.fromarray(canvas[cy:cy+500, cx:cx+700]).save(os.path.join(out_dir, 'onizleme_ayicik_yuz_100pct.png'))
ty = int(H*0.14); Image.fromarray(canvas[ty:ty+500, 500:1200]).save(os.path.join(out_dir, 'onizleme_yazi_100pct.png'))
log('BITTI')
