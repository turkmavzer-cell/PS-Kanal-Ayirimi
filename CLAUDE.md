# CLAUDE.md

Bu repo, tekstil baskı (emprime/serigrafi) için görsel renk ayrımı çalışmasıdır. Kullanıcı Türkçe konuşur; direkt ve kısa iletişim tercih eder.

## Her oturumun başında
Önce oku: `README.md`, `docs/ogrenilenler.md`, `docs/yontem-gunlugu.md`, `docs/acik-sorular.md`. Orada yazanı yeniden keşfetme.

## Ana kurallar (özet)
- Düz renkli tasarım **tramsız spot** ayrılır; tram yalnızca degrade/fotoğraf. CMYK Split Channels bu işin cevabı değildir.
- Dosya yeri ya da ayar belirsizse **kullanıcıya sor**, tahmin etme (tişört rengi, baskı boyutu, elek, mürekkep, film türü).
- Kenar ara tonları mürekkep değildir; gerçek mürekkep sayısı tasarımdan gelir.
- Sonuçları önizleme + %100 kenar kesitiyle gözle doğrula.

## Çalışma şekli
- Ağır hesap: `tools/tramsiz.py` (Python, numpy/opencv/Pillow). Photoshop aktarımı: `tools/photoshop/*.jsx` (önce `koyu_tisort_photoshop.jsx`, sonra `koyu_renk_duzelt.jsx`).
- Yeni öğrenilen her şeyi, her denemeyi ilgili `docs/*.md` dosyasına işle; kod değişikliklerini commit + push et (kullanıcı bu repo için onay verdi).
- Orijinal görseller ve üretilen filmler repoya **konmaz** (`.gitignore`).
- Ortam sınırları ve Photoshop/computer use dersleri: `docs/photoshop-ve-ortam-notlari.md`.

Proje talimatı (Claude Project Instructions) metni: `docs/proje-talimatlari.md`.
