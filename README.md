# PS-Kanal-Ayirimi

Bir görseli tekstil baskı (emprime / serigrafi) için **renk ayrımı filmlerine** (spot mürekkep kanalları) ayırma çalışması. Claude + Photoshop (bilgisayar kontrolü) + Python ile geliştirilir.

## Durum
| Sürüm | Yöntem | Durum |
|---|---|---|
| v1 | CMYK Split Channels | Yanlış (emprime ayrımı değil) |
| v2 | Otomatik spot + her renge tram | Yanlış (düz renkli iş trama çevrilmiş) |
| v3 | Tramsız spot, trap, choke'lu underbase | Düz renkli işler için (`tools/tramsiz.py`) |
| **v9** | **Bölge saflıklı AM tram (45 lpi, 508 PPI), açık + koyu set** | **Güncel** (illüstrasyon/dokulu işler, `tools/bolge_am.py`), gerçek baskıda henüz denenmedi |

Ayrıntı: [docs/yontem-gunlugu.md](docs/yontem-gunlugu.md)

## İş akışı: tek aşamalı / iki aşamalı
Her işin başında hangisinin kullanılacağı sorulur. Ayrıntı: [docs/is-akisi-tek-ve-iki-asama.md](docs/is-akisi-tek-ve-iki-asama.md)
- **Tek aşamalı:** program renkleri seçer, doğrudan filmlere ayırır → `python3 tools/bolge_am.py girdi.png cikti 6 5`
- **İki aşamalı:** 1) kanallara ayrılmamış tramlı önizleme → `ASAMA=onizleme python3 tools/bolge_am.py girdi.png cikti 6 5`; kullanıcı Photoshop'ta renkleri düzeltip onaylar; 2) `python3 tools/onizlemeden_ayir.py duzenlenmis.png cikti acik|koyu cikti/onizleme_palet.json`
- Sonra: `tools/kalite_kontrol.py` ve PSD (`tools/photoshop/psd_olustur_tek_adim.jsx`, her set için ayrı PSD).

## Hızlı başlangıç (düz renkli iş, tramsız)
```bash
pip install numpy opencv-python Pillow
python3 tools/tramsiz.py girdi.jpg cikti_klasoru
```
Çıktı: `Acik_Tisort/` (mürekkep filmleri), `Koyu_Tisort/` (beyaz zemin + mürekkep filmleri), önizlemeler. Paleti `tools/tramsiz.py` içindeki `INKS` sözlüğünden ayarla; baskı boyutu ve diğer ayarlar dosyanın başındaki sabitlerde.

Photoshop'ta Multichannel Spot Color belge: `tools/photoshop/koyu_tisort_photoshop.jsx` (film klasörü betikle aynı dizinde olmalı), ardından `tools/photoshop/koyu_renk_duzelt.jsx`. Ayrıntı: [docs/photoshop-ve-ortam-notlari.md](docs/photoshop-ve-ortam-notlari.md)

## Klasörler
- `docs/bozuk-gorselden-desen-uretim-promptu.md`: **Nano Banana Pro ile bozuk/giyilmiş görselden kusursuz 2D desen üretim (MeChi 3.3 & Desen Mühendisliği) global ve değişken prompt sistemi**
- `docs/is-akisi-tek-ve-iki-asama.md`: tek ve iki aşamalı yöntemin açıklaması
- `docs/ogrenilenler.md`: doğru/yanlış yöntemler, karar tablosu, sayısal değerler (**ana bilgi tabanı**)
- `docs/yontem-gunlugu.md`: her denemenin kaydı
- `docs/acik-sorular.md`: atölye soruları ve yapılacaklar
- `docs/photoshop-ve-ortam-notlari.md`: Photoshop/computer use/ortam dersleri
- `docs/proje-talimatlari.md`: Claude Project talimat metni
- `docs/arastirma/`: Perplexity promptu ve kaynaklı araştırma raporu
- `docs/ornekler/`: önizleme görselleri
- `tools/`: `tramsiz.py` (duz renkli isler), `hibrit.py` + `fs_dither.c` (duz + fotografik hibrit isler), `photoshop/` (JSX), `arsiv/` (yanlis eski denemeler)

## Notlar
Orijinal görseller ve üretilen filmler (büyük dosyalar) repoya konmaz.
