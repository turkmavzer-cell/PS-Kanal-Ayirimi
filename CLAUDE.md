# CLAUDE.md

Bu repo, tekstil baskı (emprime/serigrafi) için görsel renk ayrımı çalışmasıdır. Kullanıcı Türkçe konuşur; direkt ve kısa iletişim tercih eder.

## Her oturumun başında
Önce oku: `README.md`, `docs/ogrenilenler.md`, `docs/yontem-gunlugu.md`, `docs/acik-sorular.md`, `docs/arastirma/gorsel-analiz-karar-rehberi.md`, `docs/is-akisi-tek-ve-iki-asama.md`. Orada yazanı yeniden keşfetme.

## Ana kurallar (özet)
- Düz renkli tasarım **tramsız spot** ayrılır; tram yalnızca degrade/fotoğraf. CMYK Split Channels bu işin cevabı değildir.
- Dosya yeri ya da ayar belirsizse **kullanıcıya sor**, tahmin etme (tişört rengi, baskı boyutu, elek, mürekkep, film türü).
- Kenar ara tonları mürekkep değildir; gerçek mürekkep sayısı tasarımdan gelir.
- Film/PSD çözünürlüğü **508 PPI** (kullanıcı talimatı); `hibrit2.py` varsayılanı 508.
- Sonuçları önizleme + %100 kenar kesitiyle gözle doğrula.

## Zorunlu iş akışı (her yeni görsel; ayrıntı: `docs/arastirma/gorsel-analiz-karar-rehberi.md`)
1. Önce `docs/arastirma/gorsel-analiz-karar-rehberi.md` oku. `python3 tools/analiz.py girdi.png [maske.png]` çalıştır, raporu kullan.
2. Kullanıcı iş istediğinde **tek aşamalı mı iki aşamalı mı** yapılacağını (kısa açıklamasıyla), **tişört rengini, kaç mürekkep (kafa sayısı) istediğini ve zemin/arka planın basılıp basılmayacağını sor**; önceden ya da tahminle karar verme. Cevap gelince başla. Yöntemlerin açıklaması: `docs/is-akisi-tek-ve-iki-asama.md`.
   - Tek aşamalı: program renkleri seçer, doğrudan filmlere ayırır.
   - İki aşamalı: önce kanallara ayrılmamış tramlı önizleme (`ASAMA=onizleme`), kullanıcı Photoshop'ta renkleri düzeltip onaylar, sonra `tools/onizlemeden_ayir.py` ile onaylanan görüntü birebir filmlere ayrılır. Onay gelmeden 2. aşamaya geçme.
3. Ayır: illüstrasyon/tramlı işlerde `tools/bolge_am.py` (bölge saflığı; açık + koyu set, fon dahil). Zıt renk karıştırma yasak (Lab ton farkı >110° olan mürekkep çifti ≥%30 karışır, her renk çifti için), en koyu hariç <%10 bileşen at, ≤3 px mikro parça sil.
4. `python3 tools/kalite_kontrol.py cikti_klasoru kaynak.png` çalıştır; uyarıları çöz ya da kullanıcıya bildir.
5. %100 kesit + önizleme ile gözle doğrula. Kullanıcı yan yana karşılaştırma istemez; yalnızca bitmiş, doğrulanmış iş ver.
6. Film/PSD 508 PPI. Yazdığını repoda doğrula (git/dosya), sonra "yazdım" de.
7. Düz (tramsız) bölge (rozet, logo, yazı) kontrolü: film rengi kaynaktan dE ≤ 12, kenar pürüzlülüğü ≤ 0,03 (`kalite_kontrol.py` ölçer); %100 kesitte yalnız yazıya değil rozete/ovale de bak.
8. Atölye yorumları karar kuralıdır: makine ~6 kafa (7–8 kurutma iptaliyle), açık zeminde fon yok, kalın yazılı desen kaba kalır.

## İstek kapsamı
- "Repoda güncelle / düzenle" = yalnızca kod ve doküman değişikliği + commit/push. Ayrım çalıştırma, kullanıcının bilgisayarına dosya yazma, Photoshop açma **yapılmaz**; kullanıcı ayrıca "işlem yap" demeden iş üretilmez.

## Çalışma şekli
- Ağır hesap: `tools/tramsiz.py` (Python, numpy/opencv/Pillow). Photoshop aktarımı: `tools/photoshop/*.jsx` (önce `koyu_tisort_photoshop.jsx`, sonra `koyu_renk_duzelt.jsx`).
- Yeni öğrenilen her şeyi, her denemeyi ilgili `docs/*.md` dosyasına işle; kod değişikliklerini commit + push et (kullanıcı bu repo için onay verdi).
- Orijinal görseller ve üretilen filmler repoya **konmaz** (`.gitignore`).
- Ortam sınırları ve Photoshop/computer use dersleri: `docs/photoshop-ve-ortam-notlari.md`.

Proje talimatı (Claude Project Instructions) metni: `docs/proje-talimatlari.md`.
