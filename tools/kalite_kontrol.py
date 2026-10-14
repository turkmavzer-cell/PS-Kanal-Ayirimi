#!/usr/bin/env python3
"""Film ciktisi icin otomatik kalite kontrol. Karar rehberi bolum 7: docs/arastirma/gorsel-analiz-karar-rehberi.md
Kullanim: python3 tools/kalite_kontrol.py cikti_klasoru [kaynak.png] [PPI=508]
cikti_klasoru: Acik_Tisort/*.png (1-bit, siyah=murekkep) + kanallar_hibrit.json
kaynak.png (istege bagli): ayni boyutta kaynak; varsa zit renk beneği (sicak bolgede soguk murekkep) olculur.
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

# zit renk beneği
if srcp:
    src = np.array(Image.open(srcp).convert('RGB'))
    if src.shape[:2] != (H, W): warn.append('kaynak boyutu film boyutuyla ayni degil, zit renk kontrolu atlandi')
    else:
        sb = cv2.GaussianBlur(src, (0, 0), 8).astype(np.int16)
        warm = (sb[..., 0] > sb[..., 2]+25)
        del sb
        for nm, fn, rgb, a in films:
            r, g, b = rgb
            if b > r+20:                                    # soguk murekkep
                n_in = int((a & warm).sum()); n_all = max(int(a.sum()), 1)
                frac = n_in/n_all
                info.append(f'  {nm:<18} (soguk) sicak kaynak alaninda %{frac*100:.2f}')
                if frac > 0.015: warn.append(f'{nm}: soguk murekkep sicak bolgede %{frac*100:.1f} (zit renk beneği: bej/kahve icinde mavi)')

print('\n'.join(info))
print()
if warn:
    print('UYARILAR:'); [print(' -', w) for w in warn]
    sys.exit(1)
print('Otomatik kontrol temiz. Yine de %100 kesit ve onizlemeyle gozle dogrula.')
