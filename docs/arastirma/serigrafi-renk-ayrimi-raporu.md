# Tekstil Serigrafi Baskıda Renk Ayrımı: Tramlı mı, Tramsız mı?

Bu rapor emprime/serigrafi tişört baskısında renk ayrımının nasıl yapıldığını anlatıyor. Sizin yaptığınız işin (otomatik renk çıkarma, 508 PPI'da 45 lpi tramlı kanallar, tramsız yedek kanal ve beyaz zemin) neden eleştirildiğini de değerlendiriyor. Kaynaklar üretici ve tedarikçi dokümanları (Murakami, Saati, ScreenPrinting.com/Ryonet), PRINTING United (eski SGIA) teknik yazıları, Scott Fresener'in T-Biz eğitimleri, FESPA, Adobe yardım sayfaları, Türk atölye rehberleri ve forumlar.

İşaretler: Her iddianın yanında kaynağı link olarak verildi. **[yorum]** benim çıkarımım demektir; kaynakta doğrudan yazmaz ama kaynaklı bilgilerden türetilmiştir. **[kaynaksız]** yaygın pratik olduğunu düşündüğüm ama bu araştırmada belgeleyemediğim bilgidir. **[belirsiz]** kaynakların çeliştiği ya da doğrulayamadığım noktadır. Wilflex ve Union Ink için renk ayrımına özel bir teknik doküman bulamadım; bu iki marka yalnızca mürekkep ve elek aralığı bağlamında geçiyor.

---

## 10 Maddelik Özet

1. **Düz renkli tasarımda tram gerekmez.** Tram yalnızca degrade, gölge ya da yarı saydamlık taklit edilecekse kullanılır. Düz renkli bir işte her renk %100 dolu, keskin kenarlı ayrı bir film olur ([Reddit r/SCREENPRINTING](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/); [PRINTING United – Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)).
2. **Logo, yazı, clipart ve sert kenarlı grafiklerde standart yöntem spot (düz) renk ayrımıdır.** Bu ayrım tercihen vektör programında yapılır ([Scott Fresener – Color Separations 101](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/)).
3. **Tramlı spot, simüle proses, CMYK ve index ayrı tekniklerdir.** Hepsi ton ya da renk geçişi üretmek için var: simüle proses opak spot mürekkeplerle tram kullanır, CMYK şeffaf mürekkep kullanır, index ise eşit boyutlu kare (stokastik) noktalar kullanır ([Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/); [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)).
4. **Kenar yumuşatma (anti-aliasing) düz renk ayrımının baş düşmanıdır.** Yumuşak kenarlı bir dosya trama çevrilince eskiden temiz olan kenar boyunca küçük tram noktaları çıkar ([Screen Printing Magazine](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)). Bu noktaların çoğu elekte tutunamayacak kadar küçüktür ([Saati Tech Tips](https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf)).
5. **Moiré, tram noktaları ile elek dokusunun girişimidir** ([Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire)). Tram kullanmayan düz renk ayrımında bu risk tanım gereği ortadan kalkar [yorum].
6. **Elek sıklığı ile lpi bağlantılıdır.** Pratik kural: elek (iplik/inç) ≈ lpi × 4–5. 45 lpi için yaklaşık 180–225 iplik/inç gerekir, bu da Türk "T" sistemiyle kabaca 71T–89T eder ([Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire); [Ryonet pozlama kılavuzu](https://3518025.app.netsuite.com/core/media/media.nl?id=4578871&c=3518025&h=ab2e8b6e2f9684f4d557&_xt=.pdf); T dönüşümü: [OkanGökhan](https://www.okangokhan.com/serigrafi-ipek-numarasi-secimi/)).
7. **Ara tonlar ayrı mürekkep değildir.** Kenardaki gri-pembe haleler, en yakın baskı rengine atanacak ya da atılacak piksellerdir. Renk sayısı tasarımdaki gerçek mürekkep sayısıyla belirlenir [yorum; dayanağı: Photoshop Color Range'de düşük fuzziness'in "hayalet renkleri" önlemesi – [Screen Printing Mag](https://screenprintingmag.com/pre-separate-complex-graphics-with-index-tables/)].
8. **Koyu tişörtte beyaz zemin (underbase) gerekir ve mutlaka daraltılmalıdır (choke).** Önerilen değer 2–3 punto, hassas preste 1 punto ([PRINTING United TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)). Düz renkli işlerde underbase genellikle düz basılır, simüle proseste ise tramlı ([PRINTING United – Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf)).
9. **Sizin yönteminiz fotoğraf ya da degrade için uygun bir yaklaşım; düz renkli mandala/tipografi için yanlış.** Doğru dosya büyük olasılıkla sizin "tramsız yedek kanalınızın" temizlenmiş, kenar yumuşatması giderilmiş ve trap/choke eklenmiş hâlidir [yorum].
10. **Uzmanlar ayrıntılarda anlaşamıyor.** Tram açısı (22,5°, 25°, 61°), elek/lpi oranı (4, 4,5 ya da 5) ve choke miktarı kaynaktan kaynağa değişiyor. Türk kaynakları da evrensel bir reçete olmadığını, atölyede test edilmesi gerektiğini vurguluyor ([OkanGökhan – Dosya Hazırlama](https://www.okangokhan.com/serigrafi-baski-dosyasi-hazirlama/)).

---

## 1. Temel Kavramlar

### Tramlı ve tramsız ne demek

Serigrafi kalıbı ikili (binary) çalışır: bir nokta ya mürekkep geçirir ya geçirmez. Gri ya da yarı saydam alan doğrudan basılamaz. Reddit'teki bir baskıcının ifadesiyle "the screen lets the ink through or it doesn't" ([Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/)). OkanGökhan da kalıbın gerçek anlamda yarı saydam gri alan basmadığını, ton farklarının farklı boyut ya da yoğunlukta noktalarla taklit edildiğini yazar ([OkanGökhan](https://www.okangokhan.com/serigrafi-baski-dosyasi-hazirlama/)).

- **Tramsız (düz renk, solid, "line art"):** Filmdeki her alan %100 opak siyahtır, kalıpta tamamen açık olur ve tek, düz bir mürekkep katmanı basılır.
- **Tramlı (halftone):** Ton, düzenli bir ızgaradaki noktaların büyüklüğüyle oluşturulur. %50 gri, %50 boyutunda noktaya dönüşür ([Ryonet – What are Halftones](https://www.youtube.com/watch?v=rDbtlB5BE1E)). Noktaların frekansı lpi (inç başına çizgi) ile ölçülür; dpi/ppi ise çözünürlüktür, ikisi farklı şeylerdir ([T-Biz – Halftone Dots Made Easy](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)).

### Ayrım türleri

| Yöntem | Nasıl çalışır | Tipik kullanım | Kaynak |
|---|---|---|---|
| **Spot (düz) renk** | Her renk ayrı, önceden karıştırılmış mürekkep ve ayrı film/kalıptır; yalnızca kendi tonunda basılır | Logo, yazı, clipart, çizgi film, sert kenarlı grafik | [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0), [Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/) |
| **Tramlı spot** | Spot renklerin içinde gölge/degrade için tram kullanılır. Clement: spot renkte farklı opaklık ya da degrade varsa tram gerekir | Gölgeli illüstrasyon, tonlu logo | [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0), [T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/) |
| **Simüle proses** | "Sahte CMYK": opak spot mürekkeplerin (kırmızı, sarı, mavi, gri vb.) düz ve tramlı görüntüleriyle fotogerçekçi sonuç üretilir; açık ve koyu tişörtte çalışır | Fotoğraf benzeri, çok tonlu illüstrasyon, koyu tişört | [Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/), [Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0) |
| **CMYK proses** | Cyan, macenta, sarı ve siyah şeffaf mürekkeplerin tramlarıyla renk karışımı elde edilir; mürekkepler şeffaf olduğu için koyu tişörtte genellikle kullanılmaz | Açık tişörtte fotoğraf | [Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0), [Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/) |
| **Index (indeksli renk)** | Photoshop'un Indexed Color moduyla sınırlı palet oluşturulur; eşit boyutlu, rastgele dağılmış kare noktalar ("diffusion dither") kullanılır. Noktalar üst üste değil yan yana basılır | Çok renkli fotogerçekçi işler, çok istasyonlu pres | [Fresener – Index](https://t-biznetwork.com/uncategorized/index-color-separations-for-screen-printing/), [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0) |
| **Stokastik (FM) tram** | Nokta boyutu sabittir, nokta sayısı/aralığı değişir. AM tramda ise aralık sabit, nokta boyutu değişkendir. FM moiré'yi büyük ölçüde ortadan kaldırır ama kümelenme gibi başka bozulmalar getirebilir | Moiré riskli işler, ince detay | [Drukkerij SK el kitabı](https://www.drukkerijsk.eu/assets/Screenprint_halftoneprint.pdf) |

Notlar:
- Clement'e göre index 2–256 renk kullanabilir ama preste çok istasyon gerektirir ([Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)). FESPA'daki bir uygulayıcı, index ile tam renkli bir iş için genellikle 8–12 elek gerektiğini söylüyor ([FESPA](https://www.fespa.com/en/news-media/screen-separations-in-printing/)).
- Fresener index'i "stochastic" olarak da adlandırıyor ([Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/)). Yani index, Photoshop tabanlı bir FM tram türü olarak görülebilir [yorum].

### Türk atölye jargonu

| Terim | Anlamı | Kaynak / durum |
|---|---|---|
| **Film / pozitif** | Her renk için şeffaf taşıyıcıya basılmış opak siyah görüntü. Siyah ne kadar opaksa (Dmax) pozlama o kadar net olur | [OkanGökhan – Kalıp](https://www.okangokhan.com/serigrafi-baski-kalibi-yapisi-bilesenleri/), [OkanGökhan – Emprime](https://www.okangokhan.com/emprime-baski-nedir-2026/) |
| **Kalıp** | Çerçeve, mesh (ipek/elek), emülsiyon ve film/pozlama sonucu oluşan şablonun bütünü | [OkanGökhan – Kalıp](https://www.okangokhan.com/serigrafi-baski-kalibi-yapisi-bilesenleri/) |
| **İpek / gaze / elek / mesh** | Gerilmiş polyester dokuma. Türkiye'deki "T" numarası **santimetre başına iplik** sayısıdır | [Rear Serigrafi](https://www.rearserigrafi.com/haberdetay/serigrafi-baski-teknigi-ipek-baski.html), [OkanGökhan](https://www.okangokhan.com/serigrafi-ipek-numarasi-secimi/) |
| **Pozlama / ışıklama** | UV ile emülsiyonun sertleştirilmesi. Kaynaklar "pozlama" diyor; "ışıklama" kelimesi incelenen Türkçe kaynaklarda geçmiyor | "Işıklama"nın atölye ağzındaki karşılığı **[kaynaksız]** |
| **Tram / raster** | Ton için kullanılan nokta yapısı | [OkanGökhan – Tram](https://www.okangokhan.com/serigrafi-baskida-tram-kullanimi/) |
| **Kontur / dolgu** | Kontur: çizgi/kenar hattı; dolgu: içi dolu renk alanı | Genel grafik terimi **[kaynaksız]** |
| **"Lap"** | — | Bu terimin serigrafideki yerleşik bir anlamını doğrulayamadım **[belirsiz]**; atölyeye ne kastettiğini sormanız iyi olur |
| **Renk ayrımı ve film çıkışı** | Türk emprime firmaları bu ifadeyi "her çeşit emprime desen tasarım renk ayrımı ve film çıktısı" şeklinde hizmet olarak sunuyor | [Armut ilanı](https://armut.com/kucukcekmece-tisort-baski) |

**Elek dönüşümü:** inç değeri ≈ T değeri × 2,54. Örnekler: 43T ≈ 110/inç, 77T ≈ 195/inç, 120T ≈ 305/inç ([OkanGökhan](https://www.okangokhan.com/serigrafi-ipek-numarasi-secimi/)). Fresener da aynı eşleşmeyi kullanıyor: 230 mesh (90 cm), 305 mesh (120 cm) ([Fresener – Dark Shirts](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/)). Dikkat: Türkiye'de "120'lik ipek" dendiğinde 120T (≈305/inç) kastedilir; ABD'deki "120 mesh" ise yaklaşık 47T'dir [yorum].

---

## 2. Hangi Görsel Türünde Hangi Yöntem

| Görsel türü | Tercih | Neden / kaynak |
|---|---|---|
| **Düz renkli illüstrasyon, vektör, logo, tipografi** | **Tramsız spot** | Fresener spot rengi logolar, sert kenarlı grafikler ve koyu konturlu görseller için sayar; vektör programında yapılmasını önerir ([Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/)). Düz renkte tram gerekmez ([Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/)) |
| **Süslemeli, mandala benzeri, çok detaylı düz renkli çizim** | **Tramsız spot ve daha sık elek** | İnce detay için daha sık ipek önerilir ([Rear Serigrafi](https://www.rearserigrafi.com/haberdetay/serigrafi-baski-teknigi-ipek-baski.html); [OkanGökhan](https://www.okangokhan.com/serigrafi-ipek-numarasi-secimi/): ince yazı/logo için 90T üstü). Küçük yazılar için 600 dpi ile çalışılması önerilir ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)). İnce çizginin tram hücresine bölünmesi sorunu için 3. bölüme bakın [yorum] |
| **Fotoğraf, sürekli tonlu görsel** | **Tramlı: simüle proses, CMYK ya da index** | Sürekli ton, tram olmadan basılamaz ([Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)). Fotogerçekçi işte manuel preste 55 lpi, otomatik preste 65 lpi ([T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)) |
| **Degrade/gölge içeren çizim** | **Karma: düz spot alanlar ve yalnızca geçişlerde tram** | Fresener'e göre spot işler gölgeleme için küçük tram noktaları içerebilir ([Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/)). Basit tonlu spot işte 35 lpi, çok gölgeli spot işte 45 lpi ([T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)) |
| **Açık renk tişört** | Spot iş: tramsız, underbase yok. Fotoğraf: CMYK ya da simüle proses | CMYK açık tişörtte iyi çalışır, koyuda çalışmaz ([Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/)) |
| **Koyu renk tişört** | Spot iş: tramsız renkler ve **choke edilmiş beyaz underbase**. Fotoğraf: simüle proses ya da index ve tramlı underbase | Underbase siyah/renkli tişörtte gerekir ([Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0)). Düz underbase atletik baskı ve düz renk bloklarında, tramlı/tonal underbase simüle proseste kullanılır ([PRINTING United – Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf)) |

**Dijital baskı karşılaştırması:** DTG, serigrafi gibi çok sayıda kalıp için renk ayrımı gerektirmeden tam renk basar ve az adette ekonomiktir. DTF de altına beyaz taban basar ama giysi rengine doğru soldurma yapamaz, sert kenarlarla sınırlıdır ([Transfer Express](https://www.transferexpress.com/videos/dtg-vs-dtf-is-direct-to-garment-dead)). Sizin 4–5 renkli düz tasarımınız yüksek adette serigrafiye, az adette DTG/DTF'ye daha uygun düşer [yorum]. DTF/DTG RIP'leri underbase'i otomatik üretir, ama choke ayarı yine gerekir ([NestSheet](https://www.nestsheet.com/white-underbase)).

---

## 3. Tramın Sorun Çıkardığı Durumlar

### Moiré

Murakami moiré'yi "the interference of halftones and mesh" diye tanımlar: elek iplikleri ya da kesişim noktaları tram noktalarının bir kısmını kapatır. Önleme yolu, tramı RIP'te uygun açıya koymak ve her tram noktasına en az dört elek açıklığı düşürmektir ([Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire)). Saati'ye göre elek kapasitesinden küçük noktalar, açı kurallarına uyulsa bile moiré yapabilir ([Saati](https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf)). Clement 45° ve 90° açılardan kaçınılmasını söyler, çünkü noktalar ipliklerle hizalanıp kırpılır ([Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0)).
→ Tramsız ayrımda nokta olmadığı için bu girişim mekanizması da yoktur [yorum].

### Nokta büyümesi (dot gain)

- Fresener, baskıda %30–40 nokta büyümesi görülebileceğini ve ayrımı yapanın bunu hesaba katıp ayrımları daha zayıf hazırlayabileceğini söylüyor ([Fresener – Secrets videosu](https://www.youtube.com/watch?v=YJvCRSgYv3U)).
- %95 noktalar baskıda büyüyüp dolu görünebilir ([T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)).
- Düşük gerilimli elek ıslak mürekkepte sürüklenip dot gain yaratabilir ([Saati](https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf)).
- Fazla boya ve yumuşak rakle tram noktalarını birleştirebilir ([OkanGökhan – Tram](https://www.okangokhan.com/serigrafi-baskida-tram-kullanimi/)).

### Elek sıklığı ve lpi ilişkisi (sayısal)

| Kural / değer | Kaynak |
|---|---|
| Elek = lpi × 4 ya da 4,5; 55 lpi için 240 iplik/inç | [Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire) |
| Elek = lpi × 5: 35 lpi → 175, 45 lpi → 225, 55 lpi → 275 | [Ryonet pozlama kılavuzu](https://3518025.app.netsuite.com/core/media/media.nl?id=4578871&c=3518025&h=ab2e8b6e2f9684f4d557&_xt=.pdf) |
| Floresan ışıkta ×5, tek nokta ışık kaynağında ×4; giyside pratik aralık 30–60 lpi | [Ryonet – What are Halftones](https://www.youtube.com/watch?v=rDbtlB5BE1E) |
| 200 mesh en fazla 40 lpi tutar (1/5 oranı) | [Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/) |
| Önerilen tram: 45 lpi, 61°, eliptik nokta | [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0) |
| Vellum/lazer filmde 45 lpi; genel üst kalite 55; otomatik pres 65–75 lpi | [Fresener – Dark Shirts](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/) |
| Tramlı baskı 135S üzerinden önerilmez | [Murakami – Thin Threads](https://www.murakamiscreen.com/_files/ugd/6863d4_698eab2eb9e24874adc1b4832992494b.pdf?index=true) |
| Türkiye: tramda genellikle 77T ve üzeri, ince tram 90T üzeri; 43T ince tramda yetersiz kalabilir | [OkanGökhan – Tram](https://www.okangokhan.com/serigrafi-baskida-tram-kullanimi/) |

**Elek numaralarının genel kullanımı (43T–120T aralığı):**

| Elek | Kullanım | Kaynak |
|---|---|---|
| 110/inç (≈43T) | Underbase, blok yazı, büyük spot renk; underbase tek geçişte basılır | [ScreenPrinting.com](https://www.screenprinting.com/blogs/news/mesh-count-and-you) |
| 156/inç (≈61T) | Orta mürekkep, daha fazla detay. Simüle proseste underbase için de öneriliyor | [ScreenPrinting.com](https://www.screenprinting.com/blogs/news/mesh-count-and-you), [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0) |
| 150S/160S/180S | Spot renkler (Murakami ince iplik) | [Murakami – Thin Threads](https://www.murakamiscreen.com/_files/ugd/6863d4_698eab2eb9e24874adc1b4832992494b.pdf?index=true) |
| 225S–230 (≈90T) | Simüle proses, proses renk, su bazlı | [Murakami](https://www.murakamiscreen.com/_files/ugd/6863d4_698eab2eb9e24874adc1b4832992494b.pdf?index=true), [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0) |
| 305 (≈120T) | İnce tram, CMYK ve simüle proses üst renkleri | [ScreenPrinting.com](https://www.screenprinting.com/blogs/news/mesh-count-and-you), [Fresener](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/) |
| TR: 43T–55T kalın opak tekstil; 55T–77T genel tekstil; 90T–140T ince yazı/tram | Türk atölye rehberi | [OkanGökhan](https://www.okangokhan.com/serigrafi-ipek-numarasi-secimi/) |
| TR: Tekstilde genellikle 43T; ince detayda 55T/61T | Türk atölye rehberi | [OkanGökhan – Emprime](https://www.okangokhan.com/emprime-baski-nedir-2026/) |

### Küçük noktaların elekte kalmaması

- Saati'ye göre basılabilir en küçük nokta en az **bir elek açıklığı + 1,5 iplik çapı** olmalıdır. Saati'nin tablosunda **196 PW 55 µm elekte 45 lpi'nin basılabilir ton aralığı %6–%86**, 230 PW 48 µm'de %4–%90'dır ([Saati](https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf)). Bu aralığın altındaki noktalar düşer, üstündekiler dolar.
- Fresener %5 noktayı tutmaya çalışın, %2'yi tutmak muhtemelen mümkün değil diyor ([Fresener – Dark Shirts](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/)). T-Biz de "2% may be impossible to hold on a screen" diyor ([T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)).
- Aşırı pozlama ince çizgileri kaybettirir ve tram noktalarını büyütür ([OkanGökhan – Kalıp](https://www.okangokhan.com/serigrafi-baski-kalibi-yapisi-bilesenleri/)).
- En ince çizgi ya da en küçük nokta için hedef yaklaşık iki elek açıklığı + iki iplik çapıdır ([PRINTING United – Mesh Geometry](https://www.printing.org/docs/default-source/default-document-library/journal/98-2-understanding-mesh-stencil-measuring.pdf?sfvrsn=a124f024_0)).

### İnce detay, kontur kaybı ve tırtıklı kenar

- Anti-aliasing açık vektör/raster dosya trama çevrilirse, eskiden temiz olan kenar boyunca küçük tram noktaları görülür ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)).
- Yanlış elekte 1 mm'lik çizgi 1,5–2 mm basılabilir ve kenarlar tırtıklı çıkar ([Rear Serigrafi](https://www.rearserigrafi.com/haberdetay/serigrafi-baski-teknigi-ipek-baski.html)).
- **[yorum – hesap]:** 45 lpi'de bir tram hücresi 1/45 inç ≈ 0,56 mm'dir. Mandaladaki 0,3–0,5 mm'lik bir çizgi tramlıysa tek bir hücreden ince kalır; sürekli bir çizgi yerine boncuk dizisi gibi kesik noktalara bölünür. Düz (tramsız) filmde aynı çizgi kesintisiz bir şerit olur.

### Lekeli/kirli görünüm

- Simüle proseste beyazı çok opak yapmaya çalışmak tram noktalarını yayıp "solid mass of white ink" görünümüne yol açabilir ([PRINTING United – Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf)).
- **[yorum]:** Otomatik ayrımda düz alanların %88–%95 gibi "neredeyse dolu" değerlere düşmesi sık olur. Bu tonlar 45 lpi/196 elekte basılabilir aralığın (%86) üstündedir ([Saati](https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf)). Sonuç ya kontrolsüz dolma ya da kumaşın/underbase'in arasından görünmesiyle grenli, lekeli bir yüzeydir.

### Renk sayısı ve maliyet

- Her spot renk ayrı bir kalıp demektir ([Adobe Photoshop](https://helpx.adobe.com/photoshop/using/printing-spot-colors.html); [OkanGökhan](https://www.okangokhan.com/serigrafi-baski-nasil-yapilir-2/)).
- Çok renkli işte her renk ayrı film, ayrı kalıp, kayıt ayarı ve ara kurutma gerektirir ([OkanGökhan](https://www.okangokhan.com/serigrafi-baski-nasil-yapilir-2/)).
- Otomatik ayrım kenar halelerini ayrı "renk" olarak çıkarırsa, gereksiz kalıp ve istasyon eklenir [yorum].

---

## 4. Kenar Yumuşatma ve Renk Sayısı

### Ara tonlar neden ayrı mürekkep değildir

Kenar yumuşatma, ekranda tırtığı gizlemek için iki renk arasına ara renkli pikseller koyar. Gri-pembe haleler tasarımcının seçtiği renkler değildir, bu geçişin ürünüdür. Serigrafide bir piksel ya bir mürekkebe aittir ya hiçbirine [yorum]. Reddit'teki baskıcı vektörleştirilmemiş işin kullanılabilmesi için dosyanın "300dpi and aliased" olması gerektiğini, yani "every pixel is black and not fuzzed gray smoothness at the edges" olmasını şart koşuyor. Pozitifin tüm piksellerini siyah yapmak için %50 threshold bitmap öneriyor ([Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/)). Screen Printing Magazine, vektör dosyası Photoshop'ta açılırken Anti-aliased kutusunun kapatılmasını öneriyor; büyütünce kenarlar pürüzlü ("jaggies") görünse de keskin kalır ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)). Fresener da aynı uyarıyı yapıyor: vektörü Photoshop'a getirirken anti-aliasing'i kapatın, 300 dpi ya da üstünde kalın ([Fresener – Secrets videosu](https://www.youtube.com/watch?v=YJvCRSgYv3U)).

### Renk indirgeme yöntemleri

| Yöntem | Ne yapar | Kaynak / not |
|---|---|---|
| **Select > Color Range** | Her baskı rengini seçer, kanal olarak kaydeder, spot kanala çevirir. Fuzziness seçimin genişliğini belirler | [Photoshop spot ayrım videosu](https://www.youtube.com/watch?v=lFYKpA8luiE). Düşük fuzziness "ghost colors"ı önler ([Screen Printing Mag](https://screenprintingmag.com/pre-separate-complex-graphics-with-index-tables/)) |
| **Indexed Color, Custom palet** | Görüntüyü seçtiğiniz palete indirger. Index ayrımında Diffusion dither %100 kullanılır | [ScreenPrintingNow](https://www.screenprintingnow.com/techniques/how-to-make-index-color-separations-for-screen-printing/), [BrightHub](https://www.brighthub.com/multimedia/publishing/articles/1318/) |
| **Indexed Color, Dither: None** | Düz renk için her pikseli en yakın palet rengine atar, nokta deseni oluşturmaz | Düz spot ayrımda bu ayarın kullanımı **[kaynaksız]**; kaynaklar dither'ı yalnızca index (noktalı) ayrım için anlatıyor |
| **Threshold / Bitmap %50** | Her kanalı saf siyah-beyaza çevirir; anti-aliasing'i öldürür | [Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/) |
| **Posterize** | Ton sayısını azaltır | Serigrafi kaynaklarında bu iş için özel bir öneri bulamadım; genel Photoshop aracı **[kaynaksız]** |
| **Illustrator Live Color / Recolor** | Vektör renklerini birkaç spot renge atar | [Adobe Illustrator](https://helpx.adobe.com/illustrator/using/printing-color-separations.html) |

### Kaç renkte karar verilir

- Renk sayısı, tasarımın gerçek mürekkep listesidir. Sizin örneğinizde lacivert-siyah, iki mavi ve kırmızı-turuncu var; koyu tişörtte artı underbase. Haleler sayılmaz [yorum].
- Koyu tişörtte zemin rengi tasarımdaki bir rengin yerine kullanılabilir. Örneğin siyah tişörtte lacivert-siyah alanlar hiç basılmayıp kumaş gösterilebilir. Bu yaygın pratik **[kaynaksız]**, ama TGB-99 tasarımdaki gri gibi bir rengin underbase olarak da kullanılabileceğini yazıyor ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)).
- Üst üste baskıyla renk sayısı düşürülebilir: FESPA'da yedi spot renkli bir kaplan görselinin sarı, kırmızı, mavi ve siyah ile dört renge indirildiği anlatılıyor ([FESPA](https://www.fespa.com/en/news-media/screen-separations-in-printing/)).
- Renk sayısı preste kaç istasyon olduğuyla da sınırlıdır ([BrightHub](https://www.brighthub.com/multimedia/publishing/articles/1318/); [Drukkerij SK](https://www.drukkerijsk.eu/assets/Screenprint_halftoneprint.pdf)).

### Vektöre çevirme (trace) ne zaman şart

- Tek renkli düz çizgi sanatında en temiz kenar için vektör önerilir. Ama 300 dpi ve kenarı yumuşatılmamış bir raster dosya vektörsüz de basılabilir ([Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/)).
- Spot ayrımın vektör programında (Illustrator/Corel) yapılması tavsiye edilir ([Fresener](https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/)).
- Clement'e göre raster görüntü çözünürlüğe bağlıdır; 72 dpi'yi 300'e büyütmek bulanıklık yaratır ([Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)).
- **[yorum]:** Sizin durumunuzda (300 PPI, yazılı ve mandala desenli JPEG) trace şu üç durumda şart sayılır: (a) baskı boyutunda 300 PPI'nın altına düşüyorsanız; (b) JPEG sıkıştırma artefaktları kenarda kirlilik yaratıyorsa; (c) trap/choke'u temiz yapmak istiyorsanız. Aksi hâlde 600 PPI'ya yeniden örnekleyip renk indirgeyerek ve %50 threshold uygulayarak raster yoldan da temiz film alınabilir. Küçük yazı için 600 dpi önerisi bu yolu destekliyor ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)).

---

## 5. İyi Çalışan İş Akışı (Düz Renkli Tasarım)

### Ortak adımlar

1. **Baskı ölçüsünü sabitleyin.** Tasarımı tişörtteki gerçek boyutunda hazırlayın. Clement 300 ppi ve 14×14 inç tarama öneriyor ([Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)); küçük yazı varsa 600 dpi ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)). OkanGökhan 300 DPI'nın tek başına kalite garantisi olmadığını hatırlatıyor ([OkanGökhan](https://www.okangokhan.com/serigrafi-baski-dosyasi-hazirlama/)).
2. **Mürekkep listesini çıkarın.** Gerçek renkleri (Pantone/atölye reçetesi), tişört rengini ve underbase gerekip gerekmediğini belirleyin.
3. **Renk indirgeyin ve kenarları sertleştirin** (4. bölüm).
4. **Her renk için tek bir %100 siyah kanal/katman oluşturun.** Tramsız olmalı; Info panelinde düz alanlar %100 okunmalı. %80 gibi bir değer tramlı basılır ([Photoshop ayrım videosu](https://www.youtube.com/watch?v=lFYKpA8luiE)).
5. **Trap ve bindirme ekleyin.**
   - Knockout varsa açık rengin çevresine pay bırakın: açık şekle stroke verin, koyu rengi overprint yapın. Stroke 2 puntoyu aşmamalı ([FESPA](https://www.fespa.com/en/news-media/screen-separations-in-printing/)).
   - Baskın koyu renk (lacivert) en üstte basılır, diğerleri onun altına taşar; beyaz lacivertin altında olmamalı ([Texsource – Illustrator Master Class](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)).
   - Otomatik ve hassas preste genellikle butt registration (kenar kenara) kullanılır, manuel preste trap eklenir ([Texsource](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)).
   - Photoshop'ta trap için Select > Modify > Expand/Contract ve alttaki kanaldan silme yöntemi kullanılır ([Adobe Photoshop](https://helpx.adobe.com/photoshop/using/printing-spot-colors.html)).
6. **Underbase oluşturun ve choke edin** (6. bölüm).
7. **Kayıt (registration) işaretleri ekleyin.** Tüm filmlerde aynı konumda olmalı ([OkanGökhan – Dosya Hazırlama](https://www.okangokhan.com/serigrafi-baski-dosyasi-hazirlama/); [Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0)).
8. **Film çıkışı alın.** Görüntü %100 opak olmalı, ışık geçirmemeli ([Ryonet kılavuzu](https://3518025.app.netsuite.com/core/media/media.nl?id=4578871&c=3518025&h=ab2e8b6e2f9684f4d557&_xt=.pdf); [OkanGökhan – Dmax](https://www.okangokhan.com/serigrafi-baski-kalibi-yapisi-bilesenleri/)). Tramlı kısım varsa tramı RIP üretmeli (AccuRIP, FilmMaker). RIP noktaları Photoshop bitmap'inden daha kalitelidir ([UltraSeps](https://m.ultraseps.com/create-halftones-in-photoshop-for-screen-printing/)).
9. **Kalıbı hazırlayın.** Elek, emülsiyon ve pozlamayı atölye test etmelidir. Fresener test filmiyle %2/%5/%10 noktaların denenmesini öneriyor ([Fresener](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/)). Saati 21 adımlı pozlama testini öneriyor ([Saati](https://www.saati.com/screen-printing-tech-tips/)). İnce detay ve tramda yaklaşık %10 EMR (emülsiyonun mesh kalınlığına oranı), genel işte yaklaşık %20 önerilir ([PRINTING United – Mesh Geometry](https://www.printing.org/docs/default-source/default-document-library/journal/98-2-understanding-mesh-stencil-measuring.pdf?sfvrsn=a124f024_0)).

### Photoshop iş akışı

1. Dosyayı RGB'de, baskı boyutunda açın. Arka planı şeffaf tutun; otomatik ayrım programları da bunu ister ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)).
2. Gerekirse 600 PPI'ya yeniden örnekleyin [yorum]. JPEG gürültüsünü temizleyin.
3. Renk indirgeyin: Indexed Color (Custom palet, sadece gerçek mürekkepler, Dither: None [kaynaksız]) ya da her renk için Color Range (düşük fuzziness).
4. Her seçimi **Save Selection** ile kanala alın, ardından **New Spot Channel**'a çevirin. Kanalları doğru adlandırın, yoksa diğer uygulamalar tanımayabilir. PSD ya da TIFF kaydedin ([Adobe Photoshop](https://helpx.adobe.com/photoshop/using/printing-spot-colors.html)). Kanalların üst üste basılma sırası Channels panelindeki sırayla belirlenir; varsayılan kanalların üstüne spot taşımak yalnızca Multichannel modunda mümkündür ([Adobe](https://helpx.adobe.com/photoshop/using/printing-spot-colors.html)).
5. Her kanala **Image > Adjustments > Threshold (128)** uygulayıp gri pikselleri yok edin ([Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/)'teki %50 threshold mantığı).
6. Trap için Expand/Contract kullanın; underbase'i choke'layın (stroke yöntemi, 6. bölüm).
7. Çıkış: RIP üzerinden ya da kanalı ayrı belgeye bölüp Bitmap (%50 threshold) ile basın. Tramlı kanallarda Bitmap > Halftone Screen kullanılır ([UltraSeps](https://m.ultraseps.com/create-halftones-in-photoshop-for-screen-printing/)), ama düz renkte buna gerek yok.

### Illustrator iş akışı

1. Raster'ı Image Trace ile vektöre çevirin ya da yeniden çizin. Outline görünümüyle (Ctrl/Cmd+Y) gizli şekilleri kontrol edin ([Texsource](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)).
2. Pathfinder > Merge ile üst üste binen şekilleri temizleyin. Select > Same Fill Color ile renksiz "çöp" şekilleri silin ve her rengi ayrı katmana alın ([Texsource](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)).
3. Her rengi **spot** swatch olarak tanımlayın (CMYK karışımı değil). Beyaz spot ekranda açık macenta görünebilir, filmde yine siyah basılır ([Texsource](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)). FESPA da renklerin "spot colours, not process" olarak tanımlanmasını şart koşuyor ([FESPA](https://www.fespa.com/en/news-media/screen-separations-in-printing/)).
4. Recolor/Live Color ile renkleri istenen spot sayısına indirin ([Adobe Illustrator](https://helpx.adobe.com/illustrator/using/printing-color-separations.html)).
5. Trap için stroke ve overprint kullanın. Window > Separations Preview ile her plakayı kontrol edin; bu panel CMYK belge modunda çalışır ([Adobe Illustrator](https://helpx.adobe.com/illustrator/using/printing-color-separations.html)).
6. Çıkış: renk başına bir sayfa, kayıt işaretleri açık, RIP ya da PostScript sürücüsüyle.

### Ayrım yazılımları ve RIP'ler

- **Separation Studio / Spot Process** (Freehand Graphics), **T-Seps** (Fresener), **UltraSeps**, **QuikSeps Professional**: spot ve simüle proses ayrımları ([emdigitizing](https://emdigitizing.com/best-9-color-separation-software-for-printers/)). Spot Process Separation Studio ham simüle proses ayrımlarını saniyeler içinde çıkarır ([Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0)).
- **RIP'ler:** AccuRIP, FilmMaker ([UltraSeps](https://m.ultraseps.com/create-halftones-in-photoshop-for-screen-printing/)); Wasatch SoftRIP ([emdigitizing](https://emdigitizing.com/best-9-color-separation-software-for-printers/)).
- **[yorum]:** Bu otomatik yazılımlar ağırlıkla simüle proses ve fotoğraf içindir. 4–5 düz renkli bir tasarımda temiz bir manuel spot ayrımı genellikle daha iyi sonuç verir. Clement de otomatik ayrımın son ayarlara hazır "ham" ayrım ürettiğini söylüyor, yani bitmiş iş değil.

---

## 6. Beyaz Zemin (Underbase) ve Koyu Tekstil

**Ne zaman gerekir:**
- Underbase, üst renklerin oturduğu ve onları parlatan, genellikle beyaz bir katmandır. Yüksek opaklıkla basılır ve flash-cure edilir ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)).
- Siyah tişörtte plastisol beyaz zemin olmadan oldukça şeffaf kalır ([Photoshop ayrım videosu](https://www.youtube.com/watch?v=lFYKpA8luiE)).
- Underbase her zaman gerekli değildir: daha opak bir mürekkep ya da "bas, flash'la, tekrar bas" yöntemi bazen tercih edilir ([PRINTING United – Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf)).

**Nasıl hazırlanır:** Underbase gereken renklerin kanalları birleştirilir ve daraltılır. Videodaki örnekte kırmızı ve kahverengi kanalları choke edilip Apply Image ile "white base" kanalına eklenmiş ([Photoshop ayrım videosu](https://www.youtube.com/watch?v=lFYKpA8luiE)). Lacivert gibi koyu renklerin altına beyaz koyulmaz ([Texsource](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)).

**Tramlı mı, tramsız mı:**
- Düz underbase, tasarımın altına "solid, flat sheet of ink" olarak basılır. Yapması kolaydır ama tuşesi daha ağırdır; atletik ve düz renk bloklarında kullanılır. Tramlı/tonal underbase simüle proses ve proseste tercih edilir ([PRINTING United – Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf)).
- TGB-99, düz üst rengin altına kaba elekten %60–70 tramlı beyaz basmanın daha yumuşak tuşe verdiğini, ama rengin o kadar parlak olmayacağını söylüyor ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)).
- Fresener, index işlerde underbase ve highlight için 55 lpi ve 25° tram anlatıyor ([Fresener – Index](https://t-biznetwork.com/uncategorized/index-color-separations-for-screen-printing/)).

**Choke miktarı:**

| Değer | Kaynak |
|---|---|
| 2–3 punto; sağlam çerçeve ve hassas preste 1 punto. "The choke of the underbase is the KEY to good underbasing!" | [TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0) |
| 600 dpi'de 10 px beyaz, merkezden stroke ≈ 5 px ≈ 1 punto daralma; 300 dpi'de 5 px stroke | [Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/) |
| 3 px beyaz stroke ile choke (videodaki örnek) | [Photoshop ayrım videosu](https://www.youtube.com/watch?v=lFYKpA8luiE) |
| Underbase tipik olarak üstündeki renklerden küçüktür | [PRINTING United – Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf) |

Hesap: 1 punto = 1/72 inç ≈ 4,2 px (300 PPI) ≈ 7 px (508 PPI) ≈ 8,3 px (600 PPI) [yorum – hesap]. Choke orantılı küçültme değildir, yalnızca konturu biraz inceltir ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)).

**Underbase elekleri:** 110 mesh ile tek geçiş ([ScreenPrinting.com](https://www.screenprinting.com/blogs/news/mesh-count-and-you)); Murakami 150S Smart Mesh ile tek geçişte opak beyaz ([Murakami – Thin Threads](https://www.murakamiscreen.com/_files/ugd/6863d4_698eab2eb9e24874adc1b4832992494b.pdf?index=true)); fotogerçekçi işte 230 ([Fresener](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/)). Beyaz plastisol 250–300 mesh'ten iyi geçmez ([Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire)).

**Yaygın hatalar:**
- **Choke yapmamak:** beyaz kenardan görünür ("white peeking out") ([Photoshop ayrım videosu](https://www.youtube.com/watch?v=lFYKpA8luiE); [TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)).
- **Underbase'i tam kürlemek:** üst renk tutunmaz, yıkamada dökülür; kısmi kürleme idealdir ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)).
- **Beyazı aşırı opak yapmaya çalışmak:** tram noktaları ezilir ([PRINTING United – Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf)).
- **Koyu rengin altına beyaz koymak** ([Texsource](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)).
- **[yorum]:** İnce mandala çizgilerinde choke çizgiyi tamamen yok edebilir. 0,4 mm'lik bir çizgi 2 punto (≈0,7 mm) choke ile sıfırlanır. Bu durumda ince detaylar ya underbase'siz basılır ya da choke küçültülür.

---

## 7. Hangi Mantık İyi, Hangisi Kötü

### Karar tablosu

| Görsel türü | Önerilen yöntem | Önerilen renk sayısı | Dikkat edilecek hata |
|---|---|---|---|
| Logo / tipografi / vektör düz renk | Tramsız spot; vektör | Gerçek mürekkep sayısı (genelde 1–4); koyu tişörtte +1 underbase | Anti-aliasing; trap eksikliği; ince yazının elek için fazla ince kalması |
| Mandala / süslemeli düz renk (sizin durumunuz) | Tramsız spot; 600 PPI raster ya da vektör; sık elek (TR'de 77T–90T civarı) | 4–5 mürekkep ve underbase; haleler sayılmaz | Tram ince çizgiyi kesik noktalara böler [yorum]; choke ince çizgiyi yok eder; aşırı pozlama ([OkanGökhan](https://www.okangokhan.com/serigrafi-baski-kalibi-yapisi-bilesenleri/)) |
| Gölge/degrade içeren çizim | Karma: düz alanlar ve sadece geçişlerde 35–45 lpi tram ([T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)) | 3–6 | %5'in altı düşer, %86–90'ın üstü dolar ([Saati](https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf)); moiré |
| Fotoğraf, açık tişört | CMYK ya da simüle proses, 55–65 lpi | 4 (+spot) | Moiré, dot gain, kayıt |
| Fotoğraf, koyu tişört | Simüle proses ya da index; tramlı underbase ve highlight beyazı | Simüle 4–8; index 6–10 ([ScreenPrintingNow](https://www.screenprintingnow.com/techniques/how-to-make-index-color-separations-for-screen-printing/)) | Underbase çok opak/kalın; 230/305 elek uyumu ([Fresener](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/)) |
| Az adet, çok renk | DTG / DTF (ayrım yok) | — | DTF'de yumuşak geçiş yok, sert kenar ([Transfer Express](https://www.transferexpress.com/videos/dtg-vs-dtf-is-direct-to-garment-dead)) |

### Sizin yönteminizin dürüst değerlendirmesi

**Yanlış olan noktalar:**
1. **Yöntem seçimi.** Fotoğraf ya da degrade mantığı (her kanala tram) düz renkli bir tasarıma uygulanmış. Düz renkte tram gerekmez ([Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/); [Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)).
2. **Kenarlar.** Anti-aliased kaynak trama girince kenarda küçük noktalar oluşur ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/)). 45 lpi'de %2–5'lik noktalar elekte tutunmaz ([Fresener](https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/); [Saati](https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf)). Sonuç tırtıklı, boncuklu ve kirli konturlardır [yorum].
3. **Otomatik renk çıkarma.** Pikseller renk mesafesine göre paylaştırılınca düz alanlar %100 yerine %85–95 gibi değerlere düşebilir. Bunlar tramlı basılır, oysa düz olmalıydı [yorum]. Info panelinde %80'in tramlı basılacağı örneği ([video](https://www.youtube.com/watch?v=lFYKpA8luiE)) bu mekanizmayı gösteriyor.
4. **Tramı Photoshop'ta, 508 PPI'da üretmek.** 45 lpi'de hücre ≈ 11,3 px; nokta kenarları basamaklı olur. RIP'in yazıcı çözünürlüğünde ürettiği noktalar daha kalitelidir ([UltraSeps](https://m.ultraseps.com/create-halftones-in-photoshop-for-screen-printing/)) [kısmen yorum].
5. **Gereksiz moiré riski** ve 45 lpi için ≈180–225/inç elek zorunluluğu ([Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire); [Ryonet](https://3518025.app.netsuite.com/core/media/media.nl?id=4578871&c=3518025&h=ab2e8b6e2f9684f4d557&_xt=.pdf)). Düz renk ise atölyenin standart tekstil eleğiyle basılabilirdi [yorum].
6. **Underbase.** Choke ve hangi renklerin altına girdiği belirtilmemişse eksik iş sayılır ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0); [Texsource](https://www.youtube.com/watch?v=Iwm7ZPAgf5k)).

**Doğru olan ya da kurtarılabilir noktalar:**
- Tramsız yedek kanal üretmeniz doğru bir refleksti. Asıl teslim edilmesi gereken dosya odur, temizlendikten sonra [yorum].
- Underbase'i ayrı kanal olarak düşünmek doğru ([Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0)).
- 45 lpi tekstil için makul bir değer ([Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0); [T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)), ama yanlış tasarıma uygulanmış.

**Yönteminizin doğru olacağı durumlar:** Tasarımda gerçek gölge ve degrade varsa; fotogerçekçi bir görselse (simüle proses); bilinçli olarak yumuşak tuşe için %60–70 tramlı underbase istenmişse ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)); ya da sınırlı mürekkeple ara tonlar üretmek için tramlı bindirme isteniyorsa ([FESPA](https://www.fespa.com/en/news-media/screen-separations-in-printing/)). O durumlarda bile tramı RIP'in üretmesi ve kenarların düz kalması daha iyi olur [yorum].

---

## 8. Karşı Görüşler ve Belirsizlikler

- **Tramlı baskı daha "affedici" olabilir.** Fresener, 3–4 Pantone eşleşmeli ve renkleri birbirine değen spot işlerin, butt register, trap ve kalın mürekkepler yüzünden yüksek kaliteli tramlı baskıdan *daha zor* olabildiğini söylüyor; tramlı baskıyı "very forgiving" buluyor ([Fresener – Secrets videosu](https://www.youtube.com/watch?v=YJvCRSgYv3U)). Bu, spot işin üretimde de kolay olduğu varsayımına bir itiraz. Ama düz renkli tasarımı trama çevirmeyi önermiyor [yorum].
- **Tramlı underbase düz işte de kullanılabilir.** Daha yumuşak tuşe için düz üst rengin altına %60–70 tram ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)). PRINTING United de giysi baskısında tonal underbase'in daha yaygın olduğunu söylüyor ([Underbases](https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf)). Hangisinin sizin işiniz için daha iyi olduğu atölyenin mürekkebine ve elek seçimine bağlı **[belirsiz]**.
- **Tram açısı:** 61° ([Clement](https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0)), 22,5° (Separation Studio) ([Clement](https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0)), 25° ([T-Biz](https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/)), 26° ([UltraSeps](https://m.ultraseps.com/create-halftones-in-photoshop-for-screen-printing/)), 27,5° ([Reddit](https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/)). Tek doğru yok; Murakami de her açının moiré'yi önlemediğini, elek bazında tablo gerektiğini söylüyor ([Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire)).
- **Elek/lpi oranı:** 4–4,5 ([Murakami](https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire)) ile 5 ([Ryonet](https://3518025.app.netsuite.com/core/media/media.nl?id=4578871&c=3518025&h=ab2e8b6e2f9684f4d557&_xt=.pdf)) arasında değişiyor. Ryonet'e göre fark pozlama ışık kaynağına bağlı ([Ryonet video](https://www.youtube.com/watch?v=rDbtlB5BE1E)).
- **Choke miktarı:** 1–3 punto ([TGB-99](https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0)) ile birkaç piksel ([Screen Printing Mag](https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/); [video](https://www.youtube.com/watch?v=lFYKpA8luiE)) arasında. Pres hassasiyetine bağlı.
- **Türk tekstilinde "standart" elek:** Bir kaynak tekstilde genellikle 43T diyor ([OkanGökhan – Emprime](https://www.okangokhan.com/emprime-baski-nedir-2026/)), diğeri tişörtte 55T/77T ([OkanGökhan – İpek](https://www.okangokhan.com/serigrafi-ipek-numarasi-secimi/)). Mürekkep türüne (su bazlı, plastisol, pigment) göre değişiyor **[belirsiz]**.
- **Evrensel reçete yok:** OkanGökhan, internetten bulunan tek bir LPI ya da mesh değerini her işe uygulamanın doğru olmadığını açıkça yazıyor ([OkanGökhan](https://www.okangokhan.com/serigrafi-baski-dosyasi-hazirlama/)).
- **Dot gain değerleri** (%30–40) tek bir uygulayıcının videosundan geliyor ([Fresener](https://www.youtube.com/watch?v=YJvCRSgYv3U)); kumaşa ve mürekkebe göre değişir **[belirsiz]**.

---

## Atölyeye Sorulabilecek 10 Somut Soru

1. Bu iş için hangi elekleri kullanacaksınız? Renkler ve underbase için T değeri (ör. 43T, 61T, 77T, 90T) ve iplik kalınlığı (S/T) ne olacak?
2. Film mi basıyorsunuz, yoksa doğrudan kalıba (CTS/CTP) mı pozluyorsunuz? Film ise lazer, inkjet ya da fotosetter mı? Opaklığı (Dmax) yeterli mi?
3. Hangi mürekkep türüyle basacaksınız: plastisol, su bazlı, pigment ya da discharge? Bu, underbase ihtiyacını ve elek seçimini değiştiriyor mu?
4. Tişört rengi ne? Lacivert-siyah alanları basmayıp kumaş rengini mi kullanalım?
5. Underbase'i düz mü yoksa tramlı mı basmamı tercih edersiniz? Ne kadar choke istersiniz (punto ya da mm)?
6. Presiniz manuel mi otomatik mi? Butt registration mı yoksa trap mı istiyorsunuz? Trap payı kaç mm olsun?
7. Dosyayı hangi formatta istersiniz: her renk ayrı katmanlı vektör (AI/PDF/EPS), spot kanallı PSD/TIFF ya da ayrı siyah-beyaz filmler? Hangi çözünürlükte?
8. En ince çizgi ve en küçük yazı için minimum kalınlığınız ne (ör. 0,3 mm / 8 pt)? Mandaladaki ince çizgiler bu eleklerde açılır mı?
9. Renk sırası ne olacak (ör. underbase → flash → açık mavi → orta mavi → kırmızı → lacivert)? Hangi renkler arasında ara kurutma yapacaksınız?
10. Kayıt işareti formatınız ve pozlama testiniz var mı (ör. Saati 21 adım ya da test şeridi)? İlk prova baskısını onaya gönderir misiniz? Ayrıca "lap" ile ne kastediliyor?

---

## Kaynaklar

**Üretici / tedarikçi teknik dokümanları**
- Murakami – How To Prevent Moire: https://www.murakamiscreen.com/technicalinfo/how-to-prevent-moire
- Murakami – Thin Threads Technical Focus: https://www.murakamiscreen.com/_files/ugd/6863d4_698eab2eb9e24874adc1b4832992494b.pdf?index=true
- SaatiPrint – Tech Tips for Screen Printers (el kitabı): https://www.catspitproductionsllc.com/Documents/SaatiPrint%20TechTip%20Handbook.pdf
- Saati – Screen Printing Tech Tips: https://www.saati.com/screen-printing-tech-tips/
- Ryonet / ScreenPrinting.com – Exposure Unit kılavuzu: https://3518025.app.netsuite.com/core/media/media.nl?id=4578871&c=3518025&h=ab2e8b6e2f9684f4d557&_xt=.pdf
- Ryonet – How to Screen Print: What are Halftones? (video): https://www.youtube.com/watch?v=rDbtlB5BE1E
- ScreenPrinting.com – Mesh Count and You: https://www.screenprinting.com/blogs/news/mesh-count-and-you
- UltraSeps – Create Halftones in Photoshop: https://m.ultraseps.com/create-halftones-in-photoshop-for-screen-printing/
- Drukkerij SK – Handbook for screen printers: Halftone printing: https://www.drukkerijsk.eu/assets/Screenprint_halftoneprint.pdf
- Adobe – Print with spot colors from Photoshop: https://helpx.adobe.com/photoshop/using/printing-spot-colors.html
- Adobe – Print color separations in Illustrator: https://helpx.adobe.com/illustrator/using/printing-color-separations.html

**Sektör kuruluşları ve dergiler**
- PRINTING United – Clement, How to Properly Prepare Screen Printing Art Files: https://www.printing.org/docs/default-source/default-document-library/journal/clement.pdf?sfvrsn=294f8072_0
- PRINTING United – Clement, Art Separations: https://www.printing.org/docs/default-source/default-document-library/clement_win20app_artseparations.pdf?sfvrsn=fe7152e0_0
- PRINTING United – TGB-99 Printing on Dark Shirts: https://www.printing.org/docs/default-source/default-document-library/resources/tgb-99-printing-on-dark-shirts.pdf?sfvrsn=e2c177fb_0
- PRINTING United – Underbases: Why, When & How: https://www.printing.org/docs/default-source/default-document-library/journal/07-1-underbases-why-when-how.pdf
- PRINTING United – Understanding Mesh Geometry, Stencil Resolution: https://www.printing.org/docs/default-source/default-document-library/journal/98-2-understanding-mesh-stencil-measuring.pdf?sfvrsn=a124f024_0
- FESPA – Screen separations in printing: https://www.fespa.com/en/news-media/screen-separations-in-printing/
- Screen Printing Magazine – Color Separations: Tips for Sharper Results: https://screenprintingmag.com/screen-printing-color-separations-photoshop-illustrator-and-corel-tips-for-sharper-results/
- Screen Printing Magazine – Pre-Separate Complex Graphics with Index Tables: https://screenprintingmag.com/pre-separate-complex-graphics-with-index-tables/

**Eğitmen / eğitim içerikleri**
- Scott Fresener – Color Separations 101: https://t-biznetwork.com/blogs/scottfresener/color-separations-101-scott-fresener/
- Scott Fresener – Index Color Separations: https://t-biznetwork.com/uncategorized/index-color-separations-for-screen-printing/
- Scott Fresener – Secrets to High-End Printing on Dark Shirts: https://t-biznetwork.com/blogs/scottfresener/secrets-to-high-end-printing-on-dark-shirts-by-scott-fresener/
- T-Biz Network – Halftone Dots Made Easy: https://t-biznetwork.com/articles/screenprinting/halftone-dots-made-easy/
- Scott Fresener – Secrets of High-End Garment Screen Printing (video): https://www.youtube.com/watch?v=YJvCRSgYv3U
- Texsource – Screen Printing Separation Master Class in Illustrator (video): https://www.youtube.com/watch?v=Iwm7ZPAgf5k
- Learn How To Screen Print – Photoshop spot color separation (video): https://www.youtube.com/watch?v=lFYKpA8luiE
- ScreenPrintingNow – How to Make Index Color Separations: https://www.screenprintingnow.com/techniques/how-to-make-index-color-separations-for-screen-printing/
- BrightHub – Indexed Color Separations in Photoshop: https://www.brighthub.com/multimedia/publishing/articles/1318/

**Forumlar**
- Reddit r/SCREENPRINTING – Does a design need to be bitmapped, vectored, or halftoned?: https://www.reddit.com/r/SCREENPRINTING/comments/137llpg/does_a_design_need_to_be_bitmapped_vectored_or/

**Türkçe kaynaklar**
- OkanGökhan – Serigrafi Baskıda Tram Kullanımı: https://www.okangokhan.com/serigrafi-baskida-tram-kullanimi/
- OkanGökhan – Serigrafi Baskı Dosyası Hazırlama: https://www.okangokhan.com/serigrafi-baski-dosyasi-hazirlama/
- OkanGökhan – Serigrafi İpek Numarası Seçimi: https://www.okangokhan.com/serigrafi-ipek-numarasi-secimi/
- OkanGökhan – Serigrafi Baskı Kalıbı: https://www.okangokhan.com/serigrafi-baski-kalibi-yapisi-bilesenleri/
- OkanGökhan – Emprime Baskı Nedir?: https://www.okangokhan.com/emprime-baski-nedir-2026/
- OkanGökhan – Serigrafi Baskı Nasıl Yapılır?: https://www.okangokhan.com/serigrafi-baski-nasil-yapilir-2/
- Rear Serigrafi – Serigrafi Baskı Tekniği / İpek Baskı: https://www.rearserigrafi.com/haberdetay/serigrafi-baski-teknigi-ipek-baski.html
- Armut – emprime renk ayrımı ve film çıkışı ilanı: https://armut.com/kucukcekmece-tisort-baski

**Diğer**
- emdigitizing – Color Separation Software listesi: https://emdigitizing.com/best-9-color-separation-software-for-printers/
- Transfer Express – DTG vs DTF: https://www.transferexpress.com/videos/dtg-vs-dtf-is-direct-to-garment-dead
- NestSheet – White Underbase with Choke (DTF): https://www.nestsheet.com/white-underbase
