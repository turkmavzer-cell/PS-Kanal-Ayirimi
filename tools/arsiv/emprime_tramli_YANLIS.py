import sys, os, time, math, json
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
src_path, out_dir = sys.argv[1], sys.argv[2]
MAXC = 24; PPI = 508; WCM = 38.488; LPI = 45.0; CHOKE_MM = 0.15
os.makedirs(out_dir, exist_ok=True)
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]", *a, flush=True)

src = np.asarray(Image.open(src_path).convert('RGB'))
sh, sw = src.shape[:2]
W = int(round(WCM/2.54*PPI)); s = W/sw; H = int(round(sh*s))
log('src', sw, sh, 'target', W, H, 'scale', round(s,3))

def rgb2lab(a):
    f = a.astype(np.float32)/255.0 if a.dtype == np.uint8 else a.astype(np.float32)
    return cv2.cvtColor(f, cv2.COLOR_RGB2Lab)

# ---------- palette detection ----------
small = cv2.resize(src, (sw//2, sh//2), interpolation=cv2.INTER_AREA)
lab = rgb2lab(small).reshape(-1, 3)
rng = np.random.default_rng(1)
samp = lab[rng.choice(len(lab), min(len(lab), 150000), replace=False)].astype(np.float32)
WHITE = rgb2lab(np.array([[[255,255,255]]], np.uint8))[0,0]

def blend_err(samp, pal):
    best = np.full(len(samp), 1e9, np.float32)
    for i in range(len(pal)):
        d = samp-pal[i]; best = np.minimum(best, (d*d).sum(1))
    for i in range(len(pal)):
        for j in range(i+1, len(pal)):
            ab = pal[j]-pal[i]; den = (ab*ab).sum()
            if den < 1e-6: continue
            t = np.clip(((samp-pal[i])@ab)/den, 0, 1)
            r = samp-(pal[i]+t[:,None]*ab)
            best = np.minimum(best, (r*r).sum(1))
    return np.sqrt(best)

chosen = None
for k in range(2, MAXC+1):
    crit = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 60, 0.3)
    _, _, cen = cv2.kmeans(samp, k, None, crit, 3, cv2.KMEANS_PP_CENTERS)
    cen = np.array([c for c in cen if np.linalg.norm(c-WHITE) > 8], np.float32)
    pal = np.vstack([WHITE, cen]).astype(np.float32)
    e = blend_err(samp, pal)
    log('k', k, 'ink', len(cen), 'meanE', round(float(e.mean()),2), 'p98', round(float(np.percentile(e,98)),2))
    chosen = cen
    if e.mean() <= 3.0 and np.percentile(e, 98) <= 12: break
inks = chosen[np.argsort(chosen[:,0])]   # darkest first
# kenar yumusatma gecis tonlarini (baska iki rengin karisimi olanlari) ele
def dist_to_blend(c, others):
    best = 1e9
    for i in range(len(others)):
        for j in range(i+1, len(others)):
            ab = others[j]-others[i]; den = float((ab*ab).sum())
            if den < 1e-6: continue
            t = min(1, max(0, float(((c-others[i])@ab)/den)))
            best = min(best, float(np.linalg.norm(c-(others[i]+t*ab))))
    return best
while len(inks) > 2:
    ds = []
    for k in range(len(inks)):
        oth = np.vstack([WHITE, np.delete(inks, k, axis=0)])
        ds.append(dist_to_blend(inks[k], oth))
    kmin = int(np.argmin(ds))
    log('ara ton mesafeleri', [round(d,1) for d in ds])
    if ds[kmin] < 14: log('ara ton elendi', inks[kmin].round(1).tolist()); inks = np.delete(inks, kmin, axis=0)
    else: break
n = len(inks); m = n+1
pal = np.vstack([WHITE, inks]).astype(np.float32)
rgb_inks = (cv2.cvtColor(inks.reshape(1,-1,3).astype(np.float32), cv2.COLOR_Lab2RGB).reshape(-1,3)*255).clip(0,255).round().astype(int)

def tr_name(rgb):
    r,g,b = [x/255 for x in rgb]
    h,l,sat = None,None,None
    mx,mn = max(r,g,b),min(r,g,b); v=mx; d=mx-mn; sat = 0 if mx==0 else d/mx
    if d==0: hh=0
    elif mx==r: hh=((g-b)/d)%6*60
    elif mx==g: hh=((b-r)/d+2)*60
    else: hh=((r-g)/d+4)*60
    if v < 0.22: return 'Siyah'
    if sat < 0.12: return 'Gri' if v < 0.85 else 'Krem'
    if v < 0.6 and 10 <= hh < 50 and sat < 0.9: base='Kahverengi'
    elif hh < 12 or hh >= 345: base='Kırmızı'
    elif hh < 40: base='Turuncu'
    elif hh < 70: base='Sarı'
    elif hh < 165: base='Yeşil'
    elif hh < 200: base='Turkuaz'
    elif hh < 255: base='Mavi'
    elif hh < 290: base='Mor'
    else: base='Pembe'
    if sat < 0.45 and v > 0.8 and base in ('Kırmızı','Turuncu','Sarı'): base = 'Krem' if base=='Sarı' else 'Somon'
    pre = 'Koyu ' if v < 0.45 else ('Açık ' if (v > 0.9 and sat < 0.6) else '')
    return pre+base.lower() if pre else base
names = [tr_name(c) for c in rgb_inks]
cnt = {}
for x in names: cnt[x] = cnt.get(x,0)+1
seen = {}; final = []
for x in names:
    if cnt[x] > 1: seen[x] = seen.get(x,0)+1; final.append(f"{x} {seen[x]}")
    else: final.append(x)
names = final
log('INKS', list(zip(names, rgb_inks.tolist())))

# ---------- tile processing ----------
angles = [45, 15, 75, 0, 30, 60, 22.5, 67.5, 37.5, 52.5, 7.5, 82.5]
cell = PPI/LPI
TH = 384
pairs = [(i,j) for i in range(m) for j in range(i+1, m)]
bytes_w = (W+7)//8
tram = [[] for _ in range(n)]; yedek = [[] for _ in range(n)]
u_tram = []; u_solid = []
prev_tiles = []; crop = None
xs = np.arange(W, dtype=np.float32)
ink_rgb = rgb_inks.astype(np.float32)/255.0

def screen_T(y0, h, ang):
    th = math.radians(ang); c, sn = math.cos(th), math.sin(th)
    ys = (y0+np.arange(h, dtype=np.float32))
    A = 2*math.pi*(ys*sn)/cell; B = 2*math.pi*(xs*c)/cell      # u = (x c + y s)/cell
    C_ = 2*math.pi*(ys*c)/cell; D = 2*math.pi*(-xs*sn)/cell     # v = (-x s + y c)/cell
    cu = np.cos(A)[:,None]*np.cos(B)[None,:] - np.sin(A)[:,None]*np.sin(B)[None,:]
    cv_ = np.cos(C_)[:,None]*np.cos(D)[None,:] - np.sin(C_)[:,None]*np.sin(D)[None,:]
    return (1.0 - 0.5*(cu+cv_))/2.0

for y0 in range(0, H, TH):
    h = min(TH, H-y0); N = h*W
    M = np.float32([[1/s,0,0.5/s-0.5],[0,1/s,(y0+0.5)/s-0.5]])
    tile = cv2.warpAffine(src, M, (W,h), flags=cv2.INTER_CUBIC|cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
    L = rgb2lab(tile).reshape(-1,3)
    best = np.full(N, 1e9, np.float32); bi = np.zeros(N, np.int16); bt = np.zeros(N, np.float32)
    for pi,(i,j) in enumerate(pairs):
        ab = pal[j]-pal[i]; den = float((ab*ab).sum())
        if den < 1e-6: continue
        d = L-pal[i]
        t = np.clip((d@ab)/den, 0, 1)
        r = d-t[:,None]*ab; e = (r*r).sum(1)
        mk = e < best; best[mk] = e[mk]; bi[mk] = pi; bt[mk] = t[mk]
    cov = np.zeros((m,N), np.float32)
    for pi,(i,j) in enumerate(pairs):
        sel = bi == pi
        if sel.any(): cov[i,sel] = 1-bt[sel]; cov[j,sel] = bt[sel]
    comp = np.ones((h,W,3), np.float32)
    for k in range(n):
        c = cov[k+1].reshape(h,W)
        T = screen_T(y0, h, angles[k % len(angles)])
        ink = (c > T) | (c >= 0.92)
        ink &= c > 0.06
        sol = c >= 0.5
        tram[k].append(np.packbits(~ink, axis=1)); yedek[k].append(np.packbits(~sol, axis=1))
        comp *= (1 - ink[:,:,None]*(1-ink_rgb[k])[None,None,:])
    tot = 1-cov[0].reshape(h,W)
    T = screen_T(y0, h, 22.5)
    ut = ((tot > T) | (tot >= 0.92)) & (tot > 0.06)
    u_tram.append(np.packbits(ut, axis=1)); u_solid.append(np.packbits(tot >= 0.5, axis=1))
    ph = max(1, round(h/6)); prev_tiles.append(cv2.resize(comp, (round(W/6), ph), interpolation=cv2.INTER_AREA))
    if crop is None and y0 <= 5600 < y0+h: crop = (comp[:, 3000:4400]*255).astype(np.uint8)[:, :, :]
    log('tile', y0//TH+1, '/', math.ceil(H/TH))

# ---------- underbase (white): 0.15 mm choke ----------
r = max(1, int(round(CHOKE_MM/25.4*PPI)))
ker = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*r+1, 2*r+1))
def choke(chunks):
    a = np.unpackbits(np.vstack(chunks), axis=1)[:, :W].astype(np.uint8)
    a = cv2.erode(a, ker)
    return np.packbits(1-a, axis=1)
u_tram_p = choke(u_tram); u_solid_p = choke(u_solid)
log('underbase choke px', r)

def save(arr, name):
    im = Image.frombytes('1', (W, H), arr.tobytes())
    im.save(os.path.join(out_dir, name), dpi=(PPI, PPI), compress_level=6)
meta = []
order = []
for k in range(n):
    save(np.vstack(yedek[k]), f"YEDEK_{k+1:02d}_{names[k]}.png"); save(np.vstack(tram[k]), f"TRAM_{k+1:02d}_{names[k]}.png")
    order.append((f"TRAM | {names[k]}", f"TRAM_{k+1:02d}_{names[k]}.png", rgb_inks[k].tolist()))
    order.append((f"YEDEK | {names[k]}", f"YEDEK_{k+1:02d}_{names[k]}.png", rgb_inks[k].tolist()))
save(u_solid_p, "YEDEK_00_BEYAZ_FON.png"); save(u_tram_p, "TRAM_00_BEYAZ_FON.png")
order = [("TRAM | BEYAZ FON - 0.15 mm daraltılmış", "TRAM_00_BEYAZ_FON.png", [255,255,255]), ("YEDEK | BEYAZ FON - 0.15 mm daraltılmış", "YEDEK_00_BEYAZ_FON.png", [255,255,255])] + order
json.dump({'W':W,'H':H,'ppi':PPI,'channels':order}, open(os.path.join(out_dir,'kanallar.json'),'w'), ensure_ascii=False, indent=1)
prev = np.vstack(prev_tiles)
Image.fromarray((prev*255).clip(0,255).astype(np.uint8)).save(os.path.join(out_dir, 'onizleme_simulasyon.png'))
if crop is not None: Image.fromarray(crop).save(os.path.join(out_dir, 'onizleme_100pct_kesit.png'))
log('DONE')
