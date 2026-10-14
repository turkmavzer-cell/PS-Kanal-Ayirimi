# Öğrenilenler: Doğru ve yanlış yöntemler

Bu dosya projenin **ana bilgi tabanıdır**. Yeni bir şey öğrenildikçe (doğru ya da yanlış) buraya eklenir. Kaynak etiketleri:

- **[rapor]**: `docs/arastirma/serigrafi-renk-ayrimi-raporu.md` içindeki kaynaklı bilgi
- **[deney]**: Bu projede denenip gözlenen sonuç
- **[usta]**: Baskı bilen kişinin söylediği (kaynak yok, doğrulanacak)
- **[belirsiz]**: Kaynaklar çelişiyor ya da doğrulanamadı

---

## 1. Ana kural

**Düz renkli tasarım (logo, yazı, illüstrasyon, mandala) tramsız spot ayrılır.** Her mürekkep için %100 siyah, kenarları keskin, tek bir film. Tram yalnızca gerçek degrade/gölge/fotoğraf için kullanılır. [rapor, usta]

| Görsel türü | Yöntem | Not |
|---|---|---|
| Düz renkli illüstrasyon, logo, tipografi | **Tramsız spot** | Bu projenin hedef iş türü |
| Süslemeli, çok detaylı düz renkli çizim | Tramsız spot, sık elek, 508 PPI | İnce çizgi (≈0,3 mm altı) baskıya uygun değil |
| Degrade/gölgeli çizim | Karma: düz alanlar + yalnızca geçişlerde 35–45 lpi tram | |
| Fotoğraf, açık tişört | CMYK ya da simüle proses, 55–65 lpi | |
| Fotoğraf, koyu tişört | Simüle proses ya da index, tramlı underbase | |
| Az adet, çok renk | DTG/DTF (renk ayrımı gerekmez) | |

## 2. Yanlış çıkan yöntemler (tekrar etme)

### 2.1 CMYK kanal bölme (Split Channels)
Düz CMYK'ya çevirip Cyan/Magenta/Yellow/Black'e bölmek **emprime ayrımı değildir**. Gri tonlu 4 belge verir, baskı rengi (spot mürekkep) üretmez. İstenen şey spot renk ayrımıydı. [deney]

### 2.2 Düz renkli tasarıma her kanalda tram
Otomatik renk çıkarıp her renge 45 lpi tram uygulamak (`tools/arsiv/emprime_tramli_YANLIS.py`). Usta "iyi bir çalışma değil, tramsız olmalıydı" dedi. Nedenleri: [rapor + deney]
- Düz alanlar %85–95'e düşüp tramlı basılır, oysa %100 olmalıydı.
- Kenar yumuşatma (anti-aliasing) trama girince kenarda küçük noktalar çıkar; bu noktalar elekte tutunmaz.
- Kenar ara tonları (gri-pembe halelerle) ayrı "mürekkep" gibi işlendi; gereksiz kalıp ve istasyon demek.
- Tram Photoshop'ta 508 PPI'da üretildi; tramı RIP üretmeli, kenarlar basamaklı olur.
- Gereksiz moiré riski; 45 lpi için ≈180–225/inç elek gerekir.
- 45 lpi'de hücre ≈ 0,56 mm; 0,3–0,5 mm'lik ince çizgi kesik noktalara bölünür.

### 2.3 Kenar ara tonlarını mürekkep saymak
K-means ile bulunan merkezlerin bazıları gerçek mürekkep değil, iki rengin kenar geçişidir (örnek: gri-pembe `173,152,151`, koyu kırmızı `133,37,31`). Bunlar **elenmeli**: bir rengin "iki başka rengin karışım doğrusuna" uzaklığı (Lab) < ~14 ise ara tondur. [deney]

### 2.4 Piksel başına tek "en yakın renk" ataması
Kenardaki karışık piksel yanlışlıkla bir üçüncü renge (ör. Mavi 2) atanır ve ince hale yapar. Çözüm: önce **iki renk karışım modeli** (en iyi çifti bul, `t ≥ 0,5` ise ikincisi), sonra kalan ince parçalar (genişlik < 7 px) komşu sınıfa verilir. [deney]

### 2.5 Underbase'i tüm tasarımın altına koyup küçültmek
- Choke yalnızca **dışa bakan** kenarlarda yapılmalı; iç kenarlarda yapılırsa renk altında boşluk kalır. [rapor + deney]
- Koyu rengin (lacivert/siyah) altına beyaz konmaz. [rapor]
- Choke ince detayları yok eder; yok olacak ince parçalar choke'lanmadan korunmalı. [rapor + deney]

## 3. Doğru çıkan yöntem (v3, `tools/tramsiz.py`)

1. Baskı ölçüsünde **508 PPI** (kullanıcı talimatı; eskiden 600 → 9094 px @38,5 cm; 508'de 7701 px). [atölye dosyaları 508]
2. Gerçek mürekkep paleti (kenar ara tonları elenmiş), beyaz = kâğıt/tişört. Açıktan koyuya sıralı = baskı sırası.
3. Kaynak bikübik büyütülür; her piksel iki renk karışım modeliyle **sert** sınıflandırılır (yumuşak geçiş yok).
4. Medyan filtre (5 px) ve ince parça temizliği (< 7 px, en koyu mürekkep hariç).
5. Kenara bağlı beyaz = tişört/kâğıt; kapalı iç beyazlar = tasarım beyazı.
6. **Trap:** açık renk, kendinden koyu renklerin altına 4 px (~0,17 mm) taşar, dışarıya yayılmaz.
7. **Underbase (koyu tişört):** `UB = erode(tüm mürekkep ∪ tasarım beyazı, 2 pt) ∪ ince parçalar`, en koyu mürekkebin (Siyah) altı hariç (kenarında trap payı kadar çakışma).
8. Çıktı: her mürekkep için 1-bit PNG film (siyah = mürekkep), açık ve koyu tişört için ayrı klasör, önizleme.

Sonuç gözle kontrol edildi (önizlemeler `docs/ornekler/`): %100'de kenarlar düz ve keskin, nokta yok. [deney]

## 4. Sayısal referanslar

| Büyüklük | Değer | Kaynak |
|---|---|---|
| Çalışma çözünürlüğü | 300 PPI standart, ince yazıda 600 | [rapor] |
| 1 punto | 1/72 inç ≈ 4,2 px @300, 7 px @508, 8,3 px @600 | hesap |
| Underbase choke | 2–3 punto; hassas preste 1 punto | [rapor] TGB-99 |
| Trap (stroke) | ≤ 2 punto | [rapor] FESPA |
| Elek (iplik/inç) ≈ lpi × 4–5 | 45 lpi → 180–225/inç ≈ 71T–89T | [rapor] |
| Türk "T" → inç | T × 2,54 (43T≈110, 77T≈195, 120T≈305) | [rapor] |
| Tramda basılabilir ton aralığı | %5–%86 (45 lpi, 196 elek) | [rapor] Saati |
| Tekstilde elek | 43T–55T kalın; 55T–77T genel; 90T–140T ince yazı/tram | [rapor] Türk kaynak |
| Tram açısı | 22,5°, 25°, 61° vb. kaynağa göre değişir | [belirsiz] |

## 5. Çalışma kuralları (süreç dersleri)

- **Dosya yeri belirsizse kullanıcıya sor**, tahmin etme. (İndirilenler klasörü örneği.) [deney]
- Ayrımdan önce **tişört rengi (açık/koyu), baskı boyutu, elek, mürekkep türü, film türü** netleştirilir.
- Otomatik renk sayısı (örn. "en fazla 24") üst sınırdır, hedef değil. Gerçek mürekkep sayısı tasarım belirler.
- Sonuçları her zaman **önizleme + %100 kenar kesiti** ile gözle doğrula; sayısal metrik tek başına yetmez.
- Beğenilmeyen sonuç, "yanlış yöntem" mi "yanlış parametre" mi diye ayrıştırılır; yöntem ise bu dosyaya yazılır.

## 6. Açık / belirsiz noktalar
Bkz. `docs/acik-sorular.md`.


## Hibrit gorsel dersi (Ayicik, 13 Ekim)
- "Her sey tramsiz" kuralı yalnizca duz renkli tasarim icin dogru. Tek gorselde hem duz yazi hem fotografik bolge varsa **hibrit**: duz kisimlar tramsiz spot, fotografik kisim dagitik tram (veya tramli spot). Once gorseli bolgelere ayir.
- Fotografik tuyu 5 duz kahveye indirmek kabul edilmedi (yamali illustrasyon gorunumu).
- Kenar ara tonlari (lacivert/beyaz sinirinda) yumusak harita ile bile sahte mürekkep kiymigi uretir; kucuk parca silme ve alt-piksel esik gerekir.
- Kaynak kalitesi sinirdir: bulanik/yapay zeka kaynaginda kalem dokusu geri gelmez; yuksek cozunurluk veya vektor kaynak iste.

- Fotografik objede en koyu mürekkep gercek en koyu golgeden acik olmamali, yoksa golge detayi duz bloga ezilir. Palet tonlari goruntunun tonal araligini (en koyu dahil) kapsamali.
- Kucuk parlamalar (goz isigi) tramla/yumusatmayla solar: acik esik ustu pikselleri "mürekkep yok" yap. Esik cok dusuk olursa (L>93) krem alanlar da beyaza ucar; ~96,5 kullan.
- Fotograf+duz yazi iceren gorselde: once duz arka plandan seffaf kesim (alfa + renk temizligi) uretmek hem kenar kalitesini hem beyaz ayrimini iyilestirir.
- 4 yerine 6 mürekkep: ayicikta ΔE ortalamasi 8,3 -> 5,5, en kotu %5 24,4 -> 12,4 (olcum, `yontem-gunlugu.md` v5).
- Hata yayilimli tramda en yakin murekkep secimini dogrusal RGB'de yapma: koyu tonlar sikisir, orta-koyu murekkepler secilmez, yamali/parcali gorunum cikar. Secimi algisal (gama) uzayda yap, hatayi dogrusalda yay.
- Yerel kontrast artirma (unsharp) tramlamadan once fotografik objede sicramalari buyutur; 0,5 fazla, ~0,25 dene.

- Bileşen tespitinde metin kenar parçacıkları ayı sınırını şişirebilir; küçük bileşenler süzülmeli, rozet ayrı bileşen olarak tutulmalı (ayı.jfif deneyimi).

- Paletin karanlık ucunda boşluk bırakma: büyük gölge alanları (çene altı, kol altı) iki koyu mürekkep arasına düşerse düz leke olur. Yeni görselde ilk işlem: en koyu iki mürekkep arası ΔE'yi ölç, gölge bandını %100'de orijinalle karşılaştır; gerekirse mürekkep sayısını artır (bu görselde 7).
- Küçük parlama bileşenleri (<20 nokta) beyaz benek yapar; gerçek parlamalar büyüktür.

- Palet seçimi tek seferlik k-means değil, "tramla-ve-puanla" olmalı: büyük koyu kütle tonu bir mürekkebe denk gelirse düz leke olur; küçük palet değişimi sonucu bölgeler arasında kaydırır. Çözüm: aday paletleri gerçekten tramlayıp bölge testiyle seç.
- Koyu gölgeler nötr olabilir (R≈G≈B); kahve-siyah mürekkep bunlara uymaz, ayrı nötr siyah mürekkep gerekir (ayıcık kulak/karın).

- Girdi çözünürlüğü değişince (örn. üst çözünürlüğe netleştirme) tüm piksel-birimli eşikler ölçeklenmeli; büyütme (upscale) araçları kenarda renkli hale bırakabilir — lacivert/renk maskeleri ince yapıları dışlamalı.

- Kaynak görsel kalitesi sonucu en çok etkileyen girdidir: 1024 px genişlikteki bulanık görselde tüy detayı yoktu; üst çözünürlüğe netleştirilmiş 4096x6144 sürüm belirgin daha iyi sonuç verdi (kullanıcı geri bildirimi, 2026-10-14). Düşük çözünürlüklü girdide önce netleştirme önerilir.

## Atölye yöntemi: "651 deneme cihan.psd" analizi (2026-10-14, kullanıcı: "bu işi yapanlar bu şekilde yapıyor")
Tasarım: "Everything in life is art" (kaligrafi yazı + oymalı barok panel), ayıcık değil. Kaynak: PSD bilgisayarda (300 MB, bulut aktarımı zaman aşımı) → psd-tools ile yerinde incelendi.
- Belge: CMYK, 8 bit, 7680x9945 px, çözünürlük 508 PPI (≈38,4 cm), 7 spot kanal + saydamlık. Katmanlar: Layer 6 (görünür, ana sanat), Layer 4 (gizli).
- Kanal sırası: fon, gri, siyah, tram(boş), fon?, gri, siyah, siyah 2. Son 4 kanal bitmap (yalnız 0/255): **fon** (%59, düz), **gri** (%27, tramlı), **siyah** (%20,7, tramlı), **siyah 2** (%3,7, düz yazı çizgileri). İlk set (gri, siyah) sürekli tonlu ara kanallar (184/204 gri seviye), sonra tramlanmış.
- Tram: yuvarlak nokta (AM), ~45 lpi, 15° açı, nokta periyodu ≈11,35 px (508/45) → muhtemelen Photoshop Bitmap > Halftone Screen (çıkış 508 ppi, 45 lpi, 15°, round). gri ve siyah kanallar AYNI açı/sıklıkta.
- Yapı: gri ve siyah tramlar üst üste (siyahın %19,5'i grinin içinde; gri/siyah neredeyse hiç fon dışına taşmıyor) → ton arttıkça ikinci mürekkep eklenen "yığılmış ton" şeması. fon = tüm panel altında düz taban (koyu tişört altlığı gibi), yazı çevresinde ince (≈birkaç px) boşluk bırakılmış; yazı (siyah 2) fon/tramlarla neredeyse hiç çakışmıyor (%0,1–0,9).
- Çıkarım: gerçek atölye tramı kaba (45 lpi ≈ 0,56 mm hücre), benim FM 3 px (0,127 mm) noktamdan çok daha iri. FM 3 px baskıda tutmama riski yüksek; AM 45 lpi / 15° atölyenin kanıtlı değeri. Renkli ayıcık için çok mürekkepli AM tram (açılar arası ayrım) denenmeli.
- Kaynak belirsizliği: lpi/açı/şekil FFT ölçümü ve görsel inceleme; PSD'de halftone ayarı kaydı bulunmadı (resource boş), bu yüzden "muhtemelen" Photoshop bitmap halftone.

## ÖÖRNEKK.psd analizi (atölye örneği #2, "Casa Blanca" illüstrasyonu)
- 6704x9941 px, 508 PPI, 8-bit Multichannel, 13 spot kanal. Photoshop halftone ayarı dosyada 45 lpi olarak kayıtlı; kanal FFT'si de 45 lpi (periyot 11,2 px @508 PPI) veriyor.
- Yöntem 651'den farklı: **CMY+K süreç (process) tramı** + altlık. Yellow/Magenta/Cyan/siyah kanalları aynı 45 lpi'de yuvarlak nokta; dört kanalın açısı da **45° (aynı)**, standart 15/75/0/45 değil → gözlem, nedeni bilinmiyor (atölyeye sorulacak).
- CMY kanalları birbiriyle çakışıyor (üst üste basım): Y∩M≈%52, M∩C≈%85 vb. Bizim indeks ayrımımızdan (piksel başına tek mürekkep) farklı.
- Her tonun 8-bit "copy" kanalı (sürekli ton) yedek olarak duruyor; tramlı 1-bit kanallar bunlardan üretilmiş.
- Altlık "fon" iki sürümde (fon 1 / fon 2, ikincisi ≈%7 daha geniş → muhtemelen yayılmış/choke varyantı, kesin değil), kapsama %67–72, tek 2-seviye kanal; beyaz yazı alanları altlıktan boşaltılmış.
- "siyah" adlı kanal tamamen dolu (tek değer) ve "beyaz -siyah" kanalı %4,8 kapsama (yazı alanı) → rolleri kesin değil.
- Görsel: açık/orta renkli, suluboya tarzı; koyu tişört için tasarlanmış gibi (beyaz altlık + CMY).

## Atölye geri bildirimi (WhatsApp, 2026-10-14) — ayıcık
Kaynak: atölyeden Ömer Desinatör ve Serhat (kullanıcı aktardı, ekran görüntüsü). Atölyenin kendi sözleri, kesin kural değil, firmadan firmaya değişir.
- Ömer'in ayrımı: 1 siyah (göz/burun), 2-3-4 kahve tonları, 5 "BE GENTLE" ovali, 6 lacivert, 7 fon; ayrıca Be Gentle yazı içi beyaz ise beyaz da eklenmeli → **toplam 8 renk**.
- **Makine kapasitesi sınır koyar:** makine kafası az, en çok ~6 renk basılabilir; kurutmalar var, bazen kurutmalar iptal edilip 7-8 renge çıkılabiliyor. Kafa yetmezse kahveler bir azaltılır, mevcut renklerden bağlama (birleştirme) yapılır.
- **Açık zemin (beyaz tişört) → fon yapılmaz**, kalıptan kurtarılır.
- Serhat: 6 renge bile düşürebileceğini, 6 kafa basıyorsa söyledi.
- Az renkte tasarım daha ince işlenir: pat boya kullanılır, kalıplar ince kalıba çekilir, "cam gibi" çıkar. Yazıları kabaran (kalın) desenler "kaba" kalır. Her desen tek kalıpta kurtarılmaz; kafa yetmezse renk iptal/azaltma istenir. Sonuç firmanın imalat kapasitesine bağlı.
- Sonuç: bizim 9 film (8 ayıcık + lacivert) atölyenin 6-8 renk beklentisinin üstünde. Hedef mürekkep sayısı atölyenin kafa sayısından gelir; bunu sormadan tek doğru sayı yok.
- [stated 2026-10-14] PSD ve film çözünürlüğü 508 PPI (atölye standardı; 45 lpi → hücre ≈11,3 px). `hibrit2.py` varsayılan PPI=508, `PPI=600` env ile eski.

## Tram benekleri: zıt renk karıştırma hatası (atölye geri bildirimi, 2026-10-14)
- Atölyeden: bej/kahve dalların içinde "ne işi var bu mavilerin" — turkuaz benekler.
- Neden: `gorsel_am.py` her piksele en küçük hatalı (a,b) karışımı seçiyor; gri-bej tonlar için en iyi çözüm sıcak mürekkep + az turkuaz (zıt renk, doygunluk düşürür). Sayıca doğru, baskıda kirli benek.
- Çözüm: turkuaz, sıcak mürekkeple yalnızca ≥%30 karışabilir (`TQMIN`); ayrıca en koyu hariç ikincil bileşen <%10 atılır (`MINC`). Sıcak bölgede turkuaz piksel 135 bin → 10 bin.
- Kural: tram ayrımında mürekkepleri saf matematiksel en iyi karışıma bırakma; zıt renk (turkuaz/sıcak) karışımlarını yasakla, minimum nokta kapsamı koy.


## Hata → neden → kural tablosu (2026-10-13/14 oturumları)
Karar ölçütleri: `docs/arastirma/gorsel-analiz-karar-rehberi.md`. Kontrol araçları: `tools/analiz.py` (önce), `tools/kalite_kontrol.py` (sonra).

| Hata | Neden | Kural |
|---|---|---|
| Çene altı/kulak/karın düz leke | Tek k-means paleti; geniş koyu kütle bir mürekkeple çakışıyor | Aday paletleri dither edip puanla (dE + koyu-düz-leke %); doku eşitle |
| Beyaz noktalar koyu alanda | Kâğıt rengi "mürekkep yok" pikselleri | İzole kâğıt noktalarını en yakın mürekkebe çevir |
| Hata başka yerde ortaya çıkıyor | Tek bölgeye göre ayar | Her çalıştırmada bölge test tablosu (yüz/çene/kol/ayak/kulak/karın) |
| Lacivert sanılan hale | Upscaler mavi halka | Lacivert maskeyi morfolojik aç, `K=sw/1024` ölçekle |
| Aday paletler bozuluyordu | `fs_dither` girdiyi yerinde değiştiriyor | Her aday için `img.copy()` |
| Bölge testi atlandı | `K` değişkeni döngüde ezildi | Yerel değişken adı farklı ve açık olsun |
| Siyah kanal çok küçük | Koyu küçük alan k-means'te kayboluyor | Notr siyah mürekkebi en koyu piksellerden ayrı çıkar; kapsama <%0,5 ise birleştir sor |
| Bej/kahve dalda mavi benek | Gri düşürmek için zıt renk (turkuaz) küçük miktarda karıştırıldı | Ton açısı farkı >110° olan mürekkep çifti ≥%30 karışsın (genel kural, `TQMIN`); en koyu hariç <%10 bileşen at (`MINC`); kalite_kontrol ton uyumsuzluğunu ölçer |
| ≤3 px mikro noktalar | Maske kenarı ve katsayı geçişi | Bağlı bileşen <`MINPX` (4 px) sil |
| 600 PPI film üretildi | PPI sabit koddaydı | PPI 508, env ile değişir; `kalite_kontrol` PPI meta kontrol eder |
| Yan yana karşılaştırma verildi | Kullanıcı istemedi | Yalnızca bitmiş, kendi doğruladığım iş |
| Tişört rengi/renk sayısı tahmin edildi | Soru sorulmadı | İş istenince tişört rengi, renk sayısı ve zemini **sor** |
| Atölye kapasitesini aşan renk (9 film) | Kafa sayısı bilinmiyordu | Hedef renk sayısını kullanıcı/atölye söyler |
| Aşırı iddia (repoda yazılı demek) | Doğrulanmadı | Yazdığımı `git`/dosyadan doğrula, sonra söyle |

## Bölge saflığı hataları (kullanıcı geri bildirimi, kız v7.1, 2026-10-14)
- Kroma eşiğiyle (>12) yazılan zıt renk kuralı **soluk renkleri** (açık mavi C≈9) kaçırır → kural kroma ≥5'ten ton açısıyla çalışmalı.
- "En koyu mürekkep muaf" istisnası, tonu koyulaştırmak için kötüye kullanıldı (koyu kahvenin %14'ü turkuaz alanda) → en koyu mürekkep yalnızca çizgi/kontur maskesinde.
- Düz alan (yerel std ≈2) piksel karışımıyla tramlanınca leke olur → düz bölge tek mürekkep/sabit ton, kâğıt dokusu önceden yumuşatılır.
- Kök neden: piksel bazlı karışım bölgeyi bilmiyor. Plan: `docs/plan-bolge-safligi.md`.

## İp/solucan çapak ve ten lekesi (kız v8 geri bildirimi, 2026-10-14)
- Göreli koyuluk (black-hat) "çizgi" ölçüsü olarak kullanılmaz: suluboya renkli şekillerin koyu kenar şeridi çizgi sanılır ve en koyu mürekkep ince çapak üretir. Çizgi = mutlak koyu (L<38) + düşük kroma.
- Basılamayacak inceliği (MINW, 3 px @508 PPI ≈ 0,15 mm) filmden sil: ince ip gibi parçalar baskıda zaten tutunmaz, ekranda çapak görünür.
- Ten gibi yumuşak alanda piksel bazlı mürekkep çifti seçimi yama yapar; çift bölge çapında sabitlenmeli ve kaplama o çift için yeniden çözülmeli. Yumuşak alanda %100 dolu yama noktalı alanın yanına gelmemeli.
- Çil gibi küçük ayrıntılar yumuşatmadan ve oylamadan korunmalı (yumuşatılmamış kaynak + hata artarsa geri dön).

- [kullanıcı, 2026-10-14] "Repoda güncelleme yap" denince yalnızca repo değişir; ayrım çalıştırıp İndirilenler'e yazmak ve Photoshop'a geçmek istenmemişti (v9 bu yüzden istenmeden üretildi).

## Düz rozet/logo çapağı ve yanlış renk (ayı, 2026-10-14)
- Belirti: ayıdaki oval rozetin DIŞ kenarında çapak/çıkıntı (iç beyaz halka temiz); rozet kahve iken filmde neredeyse siyah (Siyah Kahve).
- Neden 1 (kenar): `hibrit2.py` düz rozet maskesini color-to-alpha ile düzeltilmiş rengten (`Fc`) hesaplıyordu. Kenar kuşağında renk, küçük alfaya bölündüğü için (alfa ≥0,25) piksel gürültüsü 4 kata kadar büyüyor; eşik bu gürültüyü çıkıntıya çevirdi. Kuşak yalnızca kenara bağlı arka planla temas eden dış kenarda var, bu yüzden iç halka temiz çıktı. Lacivert yazı alfa kapısı (`al ≥ 0,5`) kullandığı için temizdi; rozette kapı yoktu. Kaynak kenar pürüzsüzdü (kontrol edildi), hata araçta.
- Neden 2 (renk): rozet rengi doğru ölçüldü (73,42,32) ama paletin en yakın mürekkebi Lab'da Siyah Kahve (dE 19); palette orta-koyu kahve yoktu. Düz alan tek mürekkeple basıldığı için palet ona göre seçilmeli ya da uyarı çıkmalı.
- Düzeltme: rozet maskesi ham kaynak renginden + alfa kapısıyla; açma (5 px) + medyan (9 px) ile ince çıkıntı silinir (`FLAT_R`, 0 = kapalı); rozet–mürekkep dE > 12 ise uyarı; `BADGE_INK_OWN=1` rozete ayrı mürekkep (ek film) verir.
- Kural: düz (tramsız) bölgede kenar rengi bölmeyle büyütülmez; alfa kapısı her düz bölgede olmalı; düz bölgenin film rengi kaynaktan dE ≤ 12 olmalı, değilse ayrı mürekkep ya da paleti düzelt.
- Kontrol: `kalite_kontrol.py` artık `kanallar_hibrit.json` içindeki `duz_bolgeler` için kenar pürüzlülüğü (eşik 0,03; çıkıntılı rozet 0,070, temiz yazı 0,006) ve renk dE ölçer. Eski ayı çıktısında iki hata da yakalandı.
- Sınır: düzeltmenin `hibrit2.py` kısmı yalnız derleme ve film kırpması üzerinde açma+medyan denemesiyle sınandı; uçtan uca ayıda yeniden çalıştırılmadı (kullanıcı istemedi). Bir sonraki çalıştırmada kalite kontrolle doğrula.
