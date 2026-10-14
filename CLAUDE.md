# CLAUDE.md

Bu repo, tekstil baskı (emprime/serigrafi) için görsel renk ayrımı çalışmasıdır. Kullanıcı Türkçe konuşur; direkt ve kısa iletişim tercih eder.

## Her oturumun başında
Önce oku: `README.md`, `docs/ogrenilenler.md`, `docs/yontem-gunlugu.md`, `docs/acik-sorular.md`, `docs/arastirma/gorsel-analiz-karar-rehberi.md`. Orada yazanı yeniden keşfetme.

## Ana kurallar (özet)
- Düz renkli tasarım **tramsız spot** ayrılır; tram yalnızca degrade/fotoğraf. CMYK Split Channels bu işin cevabı değildir.
- Dosya yeri ya da ayar belirsizse **kullanıcıya sor**, tahmin etme (tişört rengi, baskı boyutu, elek, mürekkep, film türü).
- Kenar ara tonları mürekkep değildir; gerçek mürekkep sayısı tasarımdan gelir.
- Film/PSD çözünürlüğü **508 PPI** (kullanıcı talimatı); `hibrit2.py` varsayılanı 508.
- Sonuçları önizleme + %100 kenar kesitiyle gözle doğrula.

## Zorunlu iş akışı (her yeni görsel; ayrıntı: `docs/arastirma/gorsel-analiz-karar-rehberi.md`)
1. Önce `docs/arastirma/gorsel-analiz-karar-rehberi.md` oku. `python3 tools/analiz.py girdi.png [maske.png]` çalıştır, raporu kullan.
2. Kullanıcı iş istediğinde **tişört rengini, kaç mürekkep (kafa sayısı) istediğini ve zemin/arka planın basılıp basılmayacağını sor**; önceden ya da tahminle karar verme. Cevap gelince başla.
3. Ayır: illüstrasyon/tramlı işlerde `tools/bolge_am.py` (bölge saflığı; açık + koyu set, fon dahil). Zıt renk karıştırma yasak (Lab ton farkı >110° olan mürekkep çifti ≥%30 karışır, her renk çifti için), en koyu hariç <%10 bileşen at, ≤3 px mikro parça sil.
4. `python3 tools/kalite_kontrol.py cikti_klasoru kaynak.png` çalıştır; uyarıları çöz ya da kullanıcıya bildir.
5. %100 kesit + önizleme ile gözle doğrula. Kullanıcı yan yana karşılaştırma istemez; yalnızca bitmiş, doğrulanmış iş ver.
6. Film/PSD 508 PPI. Yazdığını repoda doğrula (git/dosya), sonra "yazdım" de.
7. Atölye yorumları karar kuralıdır: makine ~6 kafa (7–8 kurutma iptaliyle), açık zeminde fon yok, kalın yazılı desen kaba kalır.

## Çalışma şekli
- Ağır hesap: `tools/tramsiz.py` (Python, numpy/opencv/Pillow). Photoshop aktarımı: `tools/photoshop/*.jsx` (önce `koyu_tisort_photoshop.jsx`, sonra `koyu_renk_duzelt.jsx`).
- Yeni öğrenilen her şeyi, her denemeyi ilgili `docs/*.md` dosyasına işle; kod değişikliklerini commit + push et (kullanıcı bu repo için onay verdi).
- Orijinal görseller ve üretilen filmler repoya **konmaz** (`.gitignore`).
- Ortam sınırları ve Photoshop/computer use dersleri: `docs/photoshop-ve-ortam-notlari.md`.

Proje talimatı (Claude Project Instructions) metni: `docs/proje-talimatlari.md`.
