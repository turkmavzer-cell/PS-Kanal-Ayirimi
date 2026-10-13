# Yöntem günlüğü

Her deneme için: ne yapıldı, parametreler, sonuç, karar. Yeni denemeler en alta eklenir.

Test görseli: Gemini üretimi mandala + "BE BRAVE" tipografi (`Gemini_Generated_Image_9clbdv9clbdv9clb.jfif`, 1686×2528 px, 300 PPI, 14,27×21,4 cm). Düz renkli, ~4 mürekkep. Görsel repoda **tutulmaz**; yerelde İndirilenler klasöründeydi.

---

## v1: CMYK kanal bölme (reddedildi)
- Photoshop'ta `Image > Mode > CMYK`, ardından Channels panel menüsünden `Split Channels`.
- Çıktı: Cyan, Magenta, Yellow, Black gri tonlu 4 belge.
- Sonuç: Kullanıcının istediği "emprime renk ayrımı" bu değildi. Bkz. `ogrenilenler.md` §2.1.
- Not: Photoshop'ta orijinal belge ayrımla kapanır; geri almak için dosya yeniden açılmalı.

## v2: Otomatik spot ayrım + tram (reddedildi)
- Araç: `tools/arsiv/emprime_tramli_YANLIS.py`
- Parametreler: 508 PPI, 38,488 cm genişlik, 45 lpi, açılar 45/15/75/0..., en çok 24 renk, k-means (Lab) + iki renk karışım modeli, her mürekkep için TRAM + tramsız YEDEK, beyaz zemin (0,15 mm choke), 1-bit PNG kanallar.
- Photoshop'a Multichannel olarak aktarım: `tools/arsiv/multichannel_olustur_tramli.jsx` + renk düzeltme `tools/arsiv/kanal_renkleri_duzelt_tramli.jsx`.
- Sonuç: Palet 4 mürekkebe indi (2 ara ton elendi). Görsel olarak orijinale yakın simülasyon, ama usta dosyayı **kötü buldu**; sebep: düz renkli iş trama çevrilmiş. Bkz. `ogrenilenler.md` §2.2.
- İlk denemede 6 mürekkep çıkmış, 2'si kenar ara tonuydu (gri halelere yol açtı); ara ton eleme eklendi.
- Photoshop gözlemi: kanallar `channels.add()` ile maske kanalı olarak eklenir; bileşik görünüm **kırmızı** olur. Spot Color'a çevirmek gerekir (`ogrenilenler.md` / `photoshop-ve-ortam-notlari.md`).

## v3: Tramsız spot ayrım (güncel)
- Araç: `tools/tramsiz.py`
- Girdi: görsel, çıktı klasörü. Palet şimdilik **kodda sabit** (`INKS`): Siyah `24,25,47`, Mavi 1 `9,43,121`, Mavi 2 `59,113,158`, Kırmızı `231,47,15`. (Önceki otomatik tespitten.)
- Parametreler: 600 PPI, 38,5 cm genişlik (9094×13636 px, 124 MP), trap 4 px, choke 2 pt (17 px), medyan 5, ince parça yarıçapı 3.
- Süre: ~2,5 dk sınıflandırma + ~40 sn son işlem (2 çekirdek, 8 GB bellek bulut ortamı).
- Çıktı: `Acik_Tisort/` (4 film), `Koyu_Tisort/` (underbase + 4 film), önizlemeler.
- Photoshop: `tools/photoshop/koyu_tisort_photoshop.jsx` kanalları Multichannel belgeye toplar; ardından `koyu_renk_duzelt.jsx` Spot Color + renk atar.
- Sonuç (gözle): %100'de düz ve keskin kenar; renkler orijinal ile uyumlu; ince Mavi 2 halelerinin çoğu temizlendi, çok küçük kalıntılar var.
- Bilinen sorunlar:
  1. Kaynakta sağ taraftaki "E" harfinin anahattı açık (orta çıkıntının alt kenarı yok) → koyu tişört setinde bu harfin beyaz dolgusu "dış" sayılıp basılmıyor. (`docs/ornekler/E_harfi_acik_anahat_sorunu.png`)
  2. Koyu tişörtte lacivert-siyah anahatlar görünmez olur; "MMXXIV", rakamlarda beyaz dolgular tuhaf kalır (tasarım sorunu).
  3. Turuncu ve kırmızı tek "Kırmızı"da; krem konturlar beyaza katılıyor. Kullanıcı ayrı tonlar isterse palet genişletilmeli.
  4. Birleşik betik (oluştur + renk ata tek dosyada) Photoshop'ta renkleri uygulamadı; **iki ayrı betik** şeklinde çalıştı. Nedeni bilinmiyor.
  5. Palet otomatik tespit edilmiyor (v2'deki tespit kodu v3'e taşınmadı).
- Karar: Usta ve atölye onayı bekleniyor (elek, film türü, kayıt tipi).

---

## Şablon (yeni deneme için)
```
## vN: <ad> (<durum>)
- Araç / commit:
- Girdi ve parametreler:
- Sonuç:
- Sorunlar:
- Karar:
```
