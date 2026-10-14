#!/usr/bin/env python3
"""Film ciktisi icin otomatik kalite kontrol. Karar rehberi bolum 7: docs/arastirma/gorsel-analiz-karar-rehberi.md
Kullanim: python3 tools/kalite_kontrol.py cikti_klasoru [kaynak.png] [PPI=508]
cikti_klasoru: Acik_Tisort/*.png (1-bit, siyah=murekkep) + kanallar_hibrit.json
kaynak.png (istege bagli): ayni boyutta kaynak; varsa zit renk beneği (murekkep tonu kaynak tonundan >110 derece farkli) olculur, her renk cifti icin.
Cikis kodu 1 = uyari var. Esikler [yorum]; atolye testiyle ayarlanmali. Gozle dogrulamanin yerini TUTMAZ.
"""
import sys, os, json
import numpy as np, cv2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

d = sys.argv[1]; srcp = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].isdigit() else None
PPI_EXP = int(os.environ.get('PPI', 508))
J = json.load(open(os.path.join(d, 'kanallar_hibrit.json')))
setn = list(J['sets'])[0]; sets = J['sets'][setn]
warn = []; info = []
films = []
for nm, fn, rgb in sets:
    im = Image.open(os.path.join(d, setn, fn))
    if im.mode != '1': warn.append(f'{fn}: 1-bit degil ({im.mode})')
    dp = im.info.get('dpi', (None,))[0]
    if dp is None or abs(dp-PPI_EXP) > 1: warn.append(f'{fn}: PPI meta {dp}, beklenen {PPI_EXP}')
    a = ~np.array(im.convert('1'))                         # True = murekkep
    films.append((nm, fn, rgb, a))
H, W = films[0][3].shape
for nm, fn, rgb, a in films:
    if a.shape != (H, W): warn.append(f'{fn}: boyut farkli {a.shape}')
info.append(f'boyut {W}x{H} px, {len(films)} film')

# kapsama
tot = H*W
for nm, fn, rgb, a in films:
    c = a.sum()/tot*100
    info.append(f'  {nm:<18} kapsama %{c:.2f}')
    if c < 0.5: warn.append(f'{nm}: kapsama %{c:.2f} <0,5 — neredeyse kullanilmayan murekkep (birlestir ya da atilacak kafa)')

# cakisma (indeks ayriminda 0 olmali)
for i in range(len(films)):
    for j in range(i+1, len(films)):
        ov = (films[i][3] & films[j][3]).sum()
        if ov > 0.001*min(films[i][3].sum(), films[j][3].sum()):
            warn.append(f'{films[i][0]} ile {films[j][0]} cakisiyor: {ov} px')

# izole kucuk noktalar
cell = PPI_EXP/45.0
tiny_area = max(3, int(0.03*cell*cell))                    # %3 nokta alani ~ 4 px (508 PPI, 45 lpi)
for nm, fn, rgb, a in films:
    nlab, lab, st, _ = cv2.connectedComponentsWithStats(a.astype(np.uint8), connectivity=8)
    areas = st[1:, 4]
    tn = int((areas <= tiny_area).sum()); tot_n = len(areas)
    frac = tn/max(tot_n, 1)
    info.append(f'  {nm:<18} bilesen {tot_n}, <= {tiny_area}px olan {tn} (%{frac*100:.1f})')
    if frac > 0.10 and tn > 2000: warn.append(f'{nm}: %{frac*100:.0f} bilesen <= {tiny_area}px (elekte tutunmayacak mikro nokta)')

# zit renk beneği: murekkebin tonu, kaynak pikselin tonundan >110 derece farkliysa (genel kural, her renk cifti)
if srcp:
    src = np.array(Image.open(srcp).convert('RGB'))
    if src.shape[:2] != (H, W): warn.append('kaynak boyutu film boyutuyla ayni degil, zit renk kontrolu atlandi')
    else:
        f4 = 4; h4, w4 = H//f4, W//f4
        sl = cv2.cvtColor(cv2.GaussianBlur(cv2.resize(src, (w4, h4), interpolation=cv2.INTER_AREA), (0, 0), 3).astype(np.float32)/255, cv2.COLOR_RGB2Lab)
        sch = np.hypot(sl[..., 1], sl[..., 2]); shu = np.degrees(np.arctan2(sl[..., 2], sl[..., 1]))
        del src
        for nm, fn, rgb, a in films:
            il = cv2.cvtColor(np.array([[rgb]], np.float32)/255, cv2.COLOR_RGB2Lab)[0, 0]
            ch = float(np.hypot(il[1], il[2])); hu = float(np.degrees(np.arctan2(il[2], il[1])))
            if ch <= 12 or il[0] <= 30: continue                # notr/cok koyu murekkep: tonu yok
            cov = cv2.resize(a.astype(np.float32), (w4, h4), interpolation=cv2.INTER_AREA)
            dh = np.abs((shu-hu+180) % 360-180)
            bad = (sch > 12) & (dh > 110)
            frac = float((cov*bad).sum()/max(cov.sum(), 1e-6))
            info.append(f'  {nm:<18} kaynak tonuyla uyumsuz (>110 derece) murekkep payi %{frac*100:.2f}')
            if frac > 0.015: warn.append(f'{nm}: murekkep payinin %{frac*100:.1f}i tonu uyumsuz kaynak alanda (zit renk beneği: orn. bej/kahve icinde mavi)')

print('\n'.join(info))
print()
if warn:
    print('UYARILAR:'); [print(' -', w) for w in warn]
    sys.exit(1)
print('Otomatik kontrol temiz. Yine de %100 kesit ve onizlemeyle gozle dogrula.')
