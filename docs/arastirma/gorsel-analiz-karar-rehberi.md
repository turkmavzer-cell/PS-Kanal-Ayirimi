# Görsel analiz ve karar rehberi

Amaç: Yeni bir görsel (JPEG/PNG) geldiğinde **neye bakıp hangi kararı vereceğimizi** baştan sabitlemek; böylece aynı hatalar (düz lekeler, beyaz noktalar, zıt renk benekleri, yanlış PPI, atölye kapasitesini aşan renk sayısı) tekrar etmez.

Kaynak etiketleri: **[kaynak]** web kaynağından doğrulandı (bağlantı en altta), **[atölye]** atölyeden gelen yorum/dosya, **[deney]** bu projede gözlendi, **[yorum]** benim çıkarımım, doğrulanmadı.

Tarih: 2026-10-14.

---

## 0. Zorunlu akış (her yeni iş)

1. `python3 tools/analiz.py girdi.png` çalıştır, raporu oku (bölüm 1).
2. Kullanıcıya sor: **tek aşamalı mı iki aşamalı mı** (bkz. `docs/is-akisi-tek-ve-iki-asama.md`), **tişört rengi** (açık/koyu/ikisi), **kaç mürekkep** (atölyenin kafa sayısı), **zemin/arka plan baskıda olsun mu**. Kullanıcı bu üçünü "iş istediğinde bana sor" diye belirtti, önceden sorma, iş istenince sor.
3. Yöntemi seç (bölüm 2) ve parametreleri bu rehberden al.
4. Ayır, sonra `python3 tools/kalite_kontrol.py cikti_klasoru` çalıştır (bölüm 7); uyarıları çöz.
5. Önizleme + %100 kesitle gözle doğrula (özellikle: açık tonlu sıcak alanlar, ince çizgiler, kenarlar).
6. PSD'yi **508 PPI** ile oluştur (kullanıcı talimatı).
7. Yeni öğrenileni `docs/` içine, kodu `tools/` içine işle, commit + push.

---

## 1. Neye bakarak karar veririz (analiz ölçütleri)

| Ölçüt | Nasıl ölçülür | Karar |
|---|---|---|
| Çözünürlük ve baskı boyutu | piksel boyutu ÷ PPI = cm | Baskı boyutunda 300 PPI'nın altındaysa sorun [kaynak: printablepress]. Bu projede 508 PPI ile çalışılır. |
| Düz alan oranı (flat) | Komşu piksel farkı küçük, geniş birleşik bileşen yüzdesi | Yüksek: tramsız spot. Düşük, sürekli geçişli: tram. |
| Degrade/doku oranı | Yerel kontrast ve gradyan dağılımı | Suluboya/boyama dokusu varsa tramsız spot **olmaz**, tram gerekir [deney]. |
| Gerçek mürekkep sayısı | Palet adayı (k-means / sayma), küçük alanlı renkler ayrı | Tasarımdaki gerçek renk sayısı belirler, üst sınır değildir. Atölye kapasitesini aşıyorsa azalt. |
| Zemin | Köşe/kenar renk ve doku | Kâğıt dokulu zemin ve fırça darbeleri baskıya girmez, kullanıcı seçer. Kâğıt beyaz noktası görselin kendi beyazına normalize edilir [deney]. |
| En ince çizgi/detay | Çizgi kalınlığı (distance transform) px → mm | Tramlı ekranda ince çizgi, hücre boyutundan küçükse kopar [deney]. |
| JPEG artefaktı / hale | Kenarlarda halka, mozaik 8x8 desen, upscaler renk halesi | Hale gerçek mürekkep sanılabilir: morfolojik temizle [deney: lacivert hale]. |
| Beyaz noktası | Figür dışı kâğıt renginin yüzdelik değeri | Gri-krem kâğıt beyaza çekilir, yoksa tüm sayfa mürekkep sanılır. |
| Küçük kapsamlı renk | Palet renginin toplam piksel yüzdesi | %1 altı = ya birleştir ya atölyeye sor (siyah kanal, bej kanal örneği) [deney]. |

---

## 2. Yöntem seçimi

Kaynaklardan [Impressions: Color Separations 101, Printable Press]:
- **Spot renk (tramsız)**: logo, çizgi film, sert kenarlı grafik; küçük tramlarla gölge eklenebilir.
- **Simüle proses**: fotogerçekçi görseller, koyu tişört dahil; Photoshop'ta spot mürekkepli kanal (tonal) ayrımı; parlak baskı.
- **Index**: açık ve koyu tişört; aynı boyutlu karesel noktalar, tek açı, simüle prosesten çoğu zaman daha çok renk ister; portre/degrade zayıf.
- **CMYK proses**: beyaz/açık tişörtte fotogerçekçi iş; yüksek elek (305–355), kayıt ve nokta büyümesi denetimi şart.

Bu projedeki karşılıkları:

| Görsel | Önerilen yöntem | Not |
|---|---|---|
| Düz renkli logo/yazı/rozet/mandala | Tramsız spot | ince kontur için sık elek [kaynak] |
| Ayıcık gibi: yumuşak dokulu ama kısıtlı renk | **AM tram (45 lpi) ile indeks ayrım (çakışmasız)** | atölye işleri 45 lpi; ayı 8–9 mürekkep |
| Suluboya/illüstrasyon (kız kişisi) | AM tram, 6 mürekkep, karışım yasakları (bölüm 5) | |
| Çok renkli fotoğraf, açık tişört | CMYK/simüle proses, 55–65 lpi [kaynak: T-Biz] | atölyeye sor, bu projede henüz yapılmadı |
| Atölye örneği "Casa Blanca" | CMY+K 45 lpi + altlık "fon" | [atölye] ayrı açı kullanılmamış, hepsi 45° |

[atölye] "651 deneme cihan" ayrımı: spot mürekkep yığılması (fon/gri/siyah/siyah 2), 45 lpi, 15°. "ÖÖRNEKK" ayrımı: CMY+K, 45 lpi, hepsi 45°. Yani atölye iki farklı mantık kullanıyor; hangisini seçeceğimizi görsele ve kafa sayısına göre belirleriz.

---

## 3. Tram parametreleri

| Konu | Bilgi |
|---|---|
| lpi | Elek sayısı ÷ 5 (güvenli) veya ÷ 4 (iyi kontrollü karanlık odayla, daha zor) [kaynak: screenprinting.com]. Basit spot + az tint 35, detaylı spot ve çok gölge 45, fotogerçekçi el tezgâhı 55, otomatik 65 [kaynak: T-Biz]. Atölyemiz 45 lpi kullanıyor [atölye]. |
| Nokta aralığı | %2 nokta elekte tutunmayabilir; 5% yanmayabilir, %10 moiré yapabilir; %75 ve üstü test baskıda dolu çıkabilir [kaynak: T-Biz]. Saati'ye göre 45 lpi basılabilir ton aralığı 196 PW 55 µm elekte %6–%86, 230 PW 48 µm'de %4–%90 [kaynak: mevcut rapor, bölüm 3, Saati]. → film kapsamı yaklaşık %4–6 altı ve %86–90 üstü uçlarda dikkat. Bizde `DMIN=0.03`, `MINC=0.10` [yorum, atölye testiyle doğrulanmalı]. |
| Nokta büyümesi | Düzgün baskıda yaklaşık %25 → %35; kötüde iki katı; gölgeleri açık hazırla [kaynak: T-Biz]. Baskıcılar genelde %30 nokta büyümesi varsayar [kaynak: screenprinting.com]. Henüz film kompanzasyonu yapmıyoruz [açık]. |
| Açı | Kaynaklar 22,5°–25° önerir, 0/90 ve 45°'den kaçın der [kaynak: screenprinting.com, T-Biz]. Atölye dosyalarında 15° (651) ve 45° (Casa Blanca) var [atölye]. **Çelişki**: atölyeye sorulmalı. Biz şimdilik 15°. |
| Nokta şekli | Yuvarlak veya elips [kaynak]; bizde yuvarlak. |
| Film PPI | Kaynaklar film çıkışını 1200 DPI öneriyor [kaynak: Printable Press]; atölye dosyaları 508 PPI. Kullanıcı 508 istedi. 45 lpi → hücre ≈ 11,3 px. |
| Tek açı, çakışmasız | Index'te tüm kanallar aynı açıyı paylaşır, kanallar arası moiré riski düşük [kaynak: Printable Press]. Bizim yöntemimizde de her piksel tek mürekkep. |

---

## 4. Kaç mürekkep (renk sayısı)

- Her mürekkep ayrı elek ve ayrı kafa. Renk sayısı makinenin basabildiğini aşmamalı [kaynak: Impressions].
- [atölye] Makinede çoğunlukla en çok ~6 kafa; kurutmalar iptal edilirse 7–8. Kafa yetmezse en yakın tonlar birleştirilir. Açık zeminde fon yapılmaz. Az renkte kalıp ince, boya pat kullanılır; kalın yazılı desen kaba kalır. Karar firmanın kapasitesine bağlı.
- Index için tipik 5–8 renk, portre ve fotoğraf için en az 7–8 [kaynak: Printable Press].
- Kural: **hedef sayıyı kullanıcı söyler** (ya da atölyeden öğrenir); analiz raporundaki "gerçek renk sayısı" yalnızca bilgi içindir.

---

## 5. Karışım ve palet kuralları (hata çıkan yerler)

Bu bölüm [deney] ve [yorum]; web kaynağı bulunamadı.

1. **Zıt renk karıştırma yasak.** Piksel başına "en az hata" karışımı seçilirse, gri-bej tonlar için sıcak mürekkep + az turkuaz seçilir. Matematiksel olarak doğru, baskıda kirli benek. Genel kural (her renk çifti): paletteki iki mürekkebin Lab ton açısı farkı >110° ise (ikisi de kromatik, en koyu hariç) küçük olanı ≥%30 kapsamalı (`TQMIN`); yoksa bu karışım yasak. Çıktıda `kalite_kontrol.py` bunu tersten ölçer: mürekkebin tonu, kaynak pikselin tonundan >110° farklıysa uyarır (eşik %1,5). Atölye aynı hatayı fark etti ("bej dalların içinde mavi ne işi var").
2. **Çok küçük ikincil bileşen at.** En koyu mürekkep hariç <%10 bileşen atılır (`MINC`); %2 nokta tutunmaz [kaynak: T-Biz].
3. **Koyu ince detay (göz kırpığı, gözlük, çizgi) için ayrı en koyu mürekkep** tutulur; k-means tek başına koyu küçük alanı kaçırır [deney].
4. **Palette orta ton merkezleri, doygun uç değil.** Açık tonlar kâğıtla karışarak elde edilir; bu yüzden palet adaylarını boyalı çıktı simülasyonuyla puanla, yalnızca renk uzayı mesafesiyle değil.
5. **Kullanılmayan mürekkep (<%0,5 kapsama)**: ya birleştir ya atılacak kafa olarak işaretle (kız kişisi Bej: %0,55 → %0,24).
6. **Düz/koyu geniş alan bir mürekkeple çakışırsa leke olur**: dither + puanlama; dokuyu eşitle [deney].
7. **Kâğıt (tişört) beyaz kabul edilir**; krem/gri tonlu kâğıt beyaza normalize edilir, aksi halde tüm görsel mürekkep sanılır.

---

## 6. Kaynak dosya kalitesi (JPEG/PNG)

- Spot renk baskı teslimlerinde düzleştirilmiş JPEG/PNG uygun görülmeyebilir; yazı ve gradyanlar vektör/halftone olmalı [kaynak: Printable Press]. Bizim iş akışımızda raster kaynak kaçınılmaz; bu yüzden **netleştirilmiş/upscale edilmiş kaynak** istenir.
- Baskı boyutunda en az 300 PPI [kaynak: Printable Press]; hedefimiz 508 PPI.
- Upscaler hale/blur izi bırakabilir (mavi halka lacivert sanıldı) [deney]; kenarda morfolojik açma ile temizle.
- Ayıda netleştirilmiş (başka uygulamayla upscale edilmiş) kaynak, öncekinden "daha iyi sonuç" verdi (kullanıcı): kaynak kalitesi doğrudan sonuç kalitesidir [deney].
- Koyu tişörtte underbase: üstteki renklerden 0,25–0,5 pt küçült (choke) [kaynak: Printable Press]. 508 PPI'da 1 pt ≈ 7 px, yani yaklaşık 2–3,5 px; proje kuralı 2–3 pt choke (en dışa bakan kenarlarda).

---

## 7. Çıktı doğrulama (otomatik + gözle)

`tools/kalite_kontrol.py` şunları denetler (sapma varsa uyarı):

| Kontrol | Eşik |
|---|---|
| Kullanılmayan/çok az kapsamlı mürekkep | <%0,5 uyarı |
| Zıt renk beneği (soğuk mürekkep sıcak kaynak bölgesinde) | kaynakta sıcak, filmde soğuk piksel >%1 sıcak alanın |
| Çok küçük izole nokta (≤ %2 hücre alanı) | sayısı |
| Aşırı dolu alan (>%90 kapsama) | bilgi |
| Mürekkepler arası çakışma | >%0,1 uyarı (indeks ayrımda sıfır olmalı) |
| PPI meta ve boyut | 508 beklenir |

Sonra yine **gözle**: %100 kesit (yüz/saç, ince dal, kenar) ve düşük çözünürlüklü karışım simülasyonu.

---

## 8. Belirsizlikler / atölyeye sorulacaklar

1. Açı: 15°, 25° mi, yoksa Casa Blanca'daki gibi 45° mi? Ayrı açı gerekli mi?
2. 45 lpi hangi elekte (sayı) basılıyor? Elek sayısı belirsiz.
3. Nokta büyümesi kompanzasyonu uygulanıyor mu, nasıl?
4. En küçük basılabilir nokta (%) ve en küçük tutunan detay (mm)?
5. Makine kafa sayısı ve kurutma durumu.
6. Siyah gibi çok küçük kapsamlı kanal ayrı mı tutulur, birleştirilir mi?
7. Süreç (CMY+K) mi, spot yığılma mı: hangi işte hangisi?

---

## Kaynaklar

- Screenprinting.com, A Crash Course in Halftones for Screen Printing: https://screenprinting.com/blogs/news/a-crash-course-in-halftones-for-screen-printing
- T-Biz Network, Halftone Dots Made Easy: https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/
- Impressions, Color Separations 101: https://impressionsmagazine.com/process-technique/color-separations-101/16708/
- Printable Press, Index Color Screen Printing Explained: https://www.printablepress.com/index-color-screen-printing-explained/
- Printable Press, How to Prepare Artwork Files for Screen Printing: https://www.printablepress.com/how-to-prepare-artwork-files-screen-printing/
- İç kaynaklar: `docs/arastirma/serigrafi-renk-ayrimi-raporu.md`, `docs/ogrenilenler.md`, atölye dosyaları (651 deneme cihan, ÖÖRNEKK) ve WhatsApp yorumları.
