# Bozuk / Giyilmiş Görselden Kusursuz 2D Desen Üretim Prompt Sistemi (Nano Banana Pro)

Bu kılavuz, `H:\Drive'ım\PROMPTLAR` altındaki **MeChi 3.3**, **Desen Mühendisliği II (v2.0)**, **Desen Mühendisliği Kişilik (v3.0)** ve **Giysi Deseni Temizleme ve Ayırma** protokollerinin sentezidir.

Amacı: Kullanımı imkansız, bozuk, eksik, düşük kaliteli, kırışık kumaş üzerindeki veya **model üzerinde giyilmiş tişört/elbise/kumaş** fotoğraflarındaki deseni; hiçbir mikro ayrıntıyı atlamadan, **Nano Banana Pro (Gemini Image)** ile tekstil baskı ve renk ayrımına (`PS-Kanal-Ayirimi`) doğrudan girebilecek **2K/4K, %100 düz (flat 2D), gergin tuval ve sıfır doku/gölge** içeren tekil bir görsele dönüştürmektir.

---

## 1. Temel Felsefe ve Altın Kurallar

1. **Düzenleme Değil, Kusursuz Yüzeyde Mutlak Yeniden Yaratma (`Absolute Recreation on a Perfect Surface`):**
   - Yapay zekaya asla fotoğrafı "düzenlemesi, temizlemesi veya ütülemesi" söylenmez.
   - Yüklenen fotoğraf yalnızca bir **adli referans şeması (forensic reference)** olarak ele alınır ve desen, idealize edilmiş dijital bir yüzey üzerinde sıfırdan yeniden inşa edilir.
2. **"Gergin Tuval" (`Stretched Canvas / Smart UV Unwrap`) Prensibi:**
   - Giysi veya kumaş üzerindeki 3 boyutlu kıvrımlar, büzülmeler, perspektif daralmaları ve silindirik eğrilikler matematiksel olarak düzleştirilir (`orthographic 2D projection`).
3. **Sıfır Detay Kaybı ve Sıfır Halüsinasyon:**
   - Görseldeki her bir nokta dizilimi, kontur kalınlığı, iç gölgeleme (stippling/hatching), motif sayısı ve renk geçişi prompt içinde **açıkça tarif edilir**. Modelin kendi kafasından desen uydurması veya karmaşık detayları basitleştirmesi kesin dille yasaklanır.
4. **Prompt Dili:**
   - Analiz Türkçe açıklanır, ancak **Nano Banana Pro** için üretilen nihai promptlar maksimum model verimliliği için **her zaman İngilizce** verilir.

---

## 2. Zorunlu Görsel Analiz Kontrol Listesi (Prompt Yazmadan Önce)

Kullanıcı bozuk veya giyilmiş bir görsel yüklediğinde, prompt oluşturulmadan önce görsel şu **7 parametre** açısından mikro düzeyde taranır ve hiçbir ayrıntı atlanmaz:

1. **Desen Türü (`[KAPSAM]`):**
   - **Tam Tuval / Metraj Desen (All-Over / Repeating Pattern):** Elbise, gömlek veya kumaşın tamamını kaplayan desen (tuvalin 4 kenarına kesintisiz uzatılmalı).
   - **Tekil Parça Baskı (Isolated Placement Graphic):** Tişört göğüs baskısı, arma veya çerçeveli illüstrasyon (kesilmeden merkeze tam oturtulmalı).
2. **Ana Motifler ve Mikro Detaylar (`[ANA OBJE VE MİKRO DETAYLAR]`):**
   - Figürler, geometrik formlar, çiçek/yaprak/hat çizgileri, elemanların birbirine göre konumu, iç içe geçme (interlocking) sırası, nokta sayıları ve dizilim yönleri.
3. **Çizgi, Doku ve Teknik Üslup (`[STİL VE TEKNİK ÖZELLİKLER]`):**
   - Vektörel düz renk (flat vector), noktalama (dot-matrix / stippling), gravür/tarama çizgileri (engraving / cross-hatching), fırça darbesi veya serigrafi spot katman yapısı.
4. **İdealize Edilmiş Renk Paleti (`[RENK PALETİ]`):**
   - Fotoğraftaki gölgeli, soluk veya sarı ışık altındaki kirli renkler **değil**; bu renklerin baskıdaki gerçek, saf, homojen (solid) karşılıkları ve yaklaşık HEX kodları.
5. **Zemin Rengi Kararı (`[ZEMİN RENGİ]`):**
   - Açık zeminli tişört → Saf Beyaz (`#FFFFFF`).
   - Koyu zeminli tişört → Saf Siyah (`#000000`).
   - Desene ait özel fon rengi → Gölgelerden arındırılmış, tek ton (flat/solid) idealize zemin rengi.
6. **Hasar, Eksik ve Kıvrım Tespiti (`[ONARIM BÖLGELERİ]`):**
   - Modelin kolu/saçı altında kalan, kat izinde kaybolan, yıpranmış, çatlamış veya kadrajdan hafif taşmış bölgelerin tespiti ve simetri/tekrar mantığıyla tamamlanması talimatı.
7. **Tipografi ve Logo Durumu (`[METİN PROTOKOLÜ]`):**
   - Metin varsa harf harf doğru yazılışı (`'[METİN]'`), font ailesi ve uygulanacak metin modülü (Grafiksel Sadakat / İmha Et & İdealleştir / Silme).

---

## 3. Ortak Global ve Değişken Master Prompt Mimarisi

Yeni bir görsel geldiğinde aşağıdaki **Global İskelet** kullanılır ve köşeli parantez içindeki **`[DEĞİŞKEN]`** alanları görselin analizine göre eksiksiz doldurulur:

### A. Tek Parça Global Master Prompt (Doğrudan Kopyala-Yapıştır Formatı)

```text
[MAIN TASK: ABSOLUTE 2D GRAPHIC RECREATION]
From the provided reference image, recreate the [ANA OBJE / DESENİN GENEL TANIMI] as an ultra-high-resolution (4K), crystal-clear, geometrically perfect, orthographically flat, full-frame 2D digital production artwork. Do not edit or filter the original photo; use it strictly as a structural and stylistic reference to reconstruct the entire artwork from scratch on an idealized, perfectly taut, flat digital canvas.

[MICRO-DETAIL & ARCHITECTURAL SPECIFICATION]
Meticulously analyze and faithfully replicate every single detail of the design without simplification or omission:
- Motif & Geometry: [MOTİFLERİN, ŞEKİLLERİN, ORANLARIN, SİMETRİNİN VE Kesişimlerin MİLİMETRİK TARİFİ].
- Fine Details & Texture Logic: [NOKTA DİZİLİMLERİ / ÇİZGİ KALINLIKLARI / KONTURLAR / İÇ DETAYLAR — ÖRN: HER ŞERİTTEKİ NOKTA SAYISI, KONTUR YAPISI].
- Idealized Color Palette: Reconstruct using clean, solid, uniform, high-contrast spot colors completely free of photographic noise or lighting shifts: [RENK 1 + ROLÜ + HEX], [RENK 2 + ROLÜ + HEX], [RENK 3 + ROLÜ + HEX], [RENK 4 + ROLÜ + HEX].
- Background Specification: [ZEMİN RENGİ MODÜLÜ — B1, B2 veya B3'ten uygun olanı seç].

[FIDELITY, REPAIR & RECONSTRUCTION PROTOCOL]
Systematically repair and reconstruct all areas obscured or distorted by garment folds, seams, perspective warp, blur, fabric wear, cracks, or low resolution. Intelligently regenerate any missing, cropped, or folded-over sections in the exact original artistic style and geometric rhythm. Maintain 100% fidelity to the original motif shapes—do not hallucinate unrequested decorative elements and do not simplify intricate details.
[KOMPOZİSYON MODÜLÜ — A1 (Tam Tuval Metraj) veya A2 (Tekil Baskı) modülünü buraya ekle].
[TİPOGRAFİ MODÜLÜ — C1, C2 veya C3 modülünü buraya ekle].

[CRITICAL PROHIBITION PROTOCOL - HIGHEST PRIORITY]
CRITICAL: Present the final output strictly as a standalone, pure 2D flat graphic artwork.
- DO NOT include any t-shirt, dress, garment silhouette, collar, sleeves, seams, stitching, or mannequin/human body parts.
- DO NOT include any fabric weave, canvas grain, knit texture, cotton fibers, or surface roughness.
- DO NOT include any wrinkles, folds, creases, drapery, 3D surface curvature, or perspective distortion.
- DO NOT include any shadows, studio lighting gradients, specular highlights, reflections, glare, or vignette.
Every color region must have uniform luminance and flat, print-ready consistency across the entire canvas.
```

---

## 4. Görselin Durumuna Göre Eklenecek Değişken Modüller

Global şablondaki ilgili yerlere görselin tipine göre aşağıdaki hazır modüllerden uygun olanlar yerleştirilir:

### Modül A — Kompozisyon ve Tuval Kaplama (`[KOMPOZİSYON MODÜLÜ]`)

* **A1. Tam Tuval / Tekrarlayan Kumaş veya Elbise Deseni (`All-Over Pattern`):**
  > `Full-Frame Edge-to-Edge Extension: The pattern must extend continuously, evenly, and seamlessly to fill the entire rectangular canvas from edge to edge (100% full bleed). DO NOT confine the pattern to the shape or silhouette of a garment or cloth piece. Every repeat unit must maintain identical scale, spacing, and geometric alignment across the entire frame.`

* **A2. Tekil Göğüs Baskısı / İzole Grafik (`Isolated Placement Graphic`):**
  > `Complete Centered Composition: Present the graphic as a complete, uncropped, perfectly centered standalone 2D illustration with balanced margin breathing room around the outer perimeter. Reconstruct any edges or tips that were cut off or tucked into garment folds.`

### Modül B — Zemin Rengi Otomasyonu (`[ZEMİN RENGİ MODÜLÜ]`)

* **B1. Açık Zeminli Görseller İçin (Saf Beyaz):**
  > `Present the final graphic on a solid, pure, unshaded white (#FFFFFF) background with crisp, clean separation from the design elements.`

* **B2. Koyu Zeminli Görseller İçin (Saf Siyah):**
  > `Present the final graphic on a solid, pitch-black (#000000) background with zero ambient light or gray haze.`

* **B3. Desene Entegre Özel Zemin Rengi İçin:**
  > `Present the final graphic on a perfectly flat, solid, uniform background that is an idealized, unshaded version of the original's [ZEMİN RENGİ TANIMI, örn: deep espresso brown #231C18] color, completely stripped of any fabric grain or lighting falloff.`

### Modül C — Metin ve Tipografi Yönetimi (`[TİPOGRAFİ MODÜLÜ]`)

* **C1. Grafiksel Sadakat (Dokulu, Noktalı veya El Çizimi Sanatsal Metin — Kural 9):**
  *(Metin desenin dokusunun bir parçasıysa; örn. noktalardan oluşan logo, kaligrafik amblem)*
  > `Graphical Text Fidelity: Meticulously recreate the exact shapes, proportions, and construction of the text '[TAM METİN]' as an integral graphic element. Treat each letter strictly as a precise visual shape to be drawn in its exact original [nokta/kontur/fırça] style, correcting only the fabric warp while preserving the exact letterform geometry.`

* **C2. İmha Et ve İdealleştir (Kıvrımdan Yamulmuş Standart Font — Kural 4.5 / 8.3):**
  *(Standart bir font kumaş katlanmasından dolayı yamulmuş/bozulmuşsa)*
  > `CRITICAL Text Idealization: COMPLETELY DISCARD the warped spatial baseline of the original text reference. Do not trace the fabric-distorted letters. Instead, re-generate the exact text '[TAM METİN]' using a clean, geometrically precise [FONT STİLİ: örn. bold vintage slab-serif / varsity block] font, perfectly aligned on a razor-straight horizontal baseline (or a mathematically symmetrical arc with level endpoints).`

* **C3. Metin Yok veya İstenmeyen Etiket/Logo Silme (Kural 3.3):**
  > `No Unwanted Text/Tags: DO NOT include any garment tags, size labels, watermarks, or extraneous text. The output must contain only the pure graphic artwork.`

---

## 5. Vaka Örneği: Goyardine Chevron Monogram Görseli İçin Üretilen Prompt

**Görsel Analizi:**
- **Kapsam:** Tam tuval tekrarlayan geometrik monogram desen (`Modül A1`).
- **Ana Motif:** İç içe geçen (interlocking) 3 boyutlu illüzyonlu Y-şekilli (chevron) şeritlerden oluşan petek/örgü kafes.
- **Mikro Detaylar:** Her bir Y-kolu düz boyama değil, minik dairesel noktalardan (dot-matrix / stippling) oluşur:
  1. **Sağ kol (Krem/Fildişi):** Yatay/diyagonal hizalı sık krem noktalar; belirli periyotlarla siyah noktalarla yazılmış mikro tipografi: üst kolda `"E: GOYARD"`, orta/alt diyagonal kolda `"HONORE"` ve `"PARIS"`.
  2. **Sol üst kol (Karamel/hardal kahve):** Sık dokulu sıcak toprak/ochre nokta dizilimi.
  3. **Sol alt/orta geçiş kolu (Boz/Taupe):** Açık gri-bej nokta dizilimi.
- **Zemin:** Koyu espreso/siyah-kahve (`#1F1916`), kanvas dokusundan arındırılmış tam düz zemin (`Modül B3`).

**Nano Banana Pro Promptu:**
```text
[MAIN TASK: ABSOLUTE 2D GRAPHIC RECREATION]
From the provided reference image, recreate the repeating interlocking Y-chevron dotted monogram pattern (Goyardine-style geometric lattice) as an ultra-high-resolution (4K), crystal-clear, geometrically perfect, orthographically flat, full-frame 2D digital production artwork. Do not edit or filter the original photo; use it strictly as a structural and stylistic reference to reconstruct the entire pattern from scratch on an idealized, perfectly taut, flat digital canvas.

[MICRO-DETAIL & ARCHITECTURAL SPECIFICATION]
Meticulously analyze and faithfully replicate every single detail of the design without simplification or omission:
- Motif & Geometry: An all-over repeating geometric lattice composed of interlocking Y-shaped chevron ribbons arranged in a strict, mathematically uniform isometric grid across the entire canvas. Every Y-junction and diagonal arm must have identical angles, width, and spacing.
- Fine Details & Dot-Matrix Logic: Every arm of the Y-chevron is constructed entirely from crisp, uniform, circular stipple dots arranged in neat parallel rows (hand-screenprinted pointillist dot-matrix style, not solid flat bars):
  1. Right branch of each Y: Filled with dense, evenly spaced warm ivory/cream dots (#EFEBD6). Embedded inside specific repeating ivory branches is crisp micro-lettering formed by dark negative-space/black dots reading "E: GOYARD" along the upper diagonal arm, and "HONORE" above "PARIS" along the lower vertical/diagonal arm.
  2. Upper-left branch of each Y: Filled with dense, evenly spaced warm ochre / tan / caramel-brown dots (#B88346).
  3. Lower-left interlocking segment of each Y: Filled with dense, evenly spaced warm taupe / light greige dots (#B7A99A).
- Idealized Color Palette: Reconstruct using clean, solid, uniform, high-contrast spot colors completely free of photographic noise or lighting shifts:
  - Background: Solid deep espresso black-brown (#1F1916)
  - Dot Color 1: Warm Ivory / Cream (#EFEBD6)
  - Dot Color 2: Warm Ochre / Tan Brown (#B88346)
  - Dot Color 3: Warm Taupe / Greige (#B7A99A)
- Background Specification: Present the final graphic on a perfectly flat, solid, uniform deep espresso black-brown (#1F1916) background, completely stripped of any coated-canvas weave, bumpy pebble grain, or specular lighting falloff.

[FIDELITY, REPAIR & RECONSTRUCTION PROTOCOL]
Systematically repair and reconstruct all blurred, low-resolution, or compressed areas. Maintain 100% fidelity to the original dot-matrix stipple construction and exact interlocking Y-chevron geometry—do not merge the dots into solid lines and do not hallucinate extra shapes.
Full-Frame Edge-to-Edge Extension: The pattern must extend continuously, evenly, and seamlessly to fill the entire rectangular canvas from edge to edge (100% full bleed). Every repeat unit must maintain identical scale, spacing, and geometric alignment across the entire frame.
Graphical Text Fidelity: Meticulously recreate the exact shapes, proportions, and dot-matrix construction of the micro-text 'E: GOYARD', 'HONORE', and 'PARIS' inside the ivory chevron arms as an integral graphic element.

[CRITICAL PROHIBITION PROTOCOL - HIGHEST PRIORITY]
CRITICAL: Present the final output strictly as a standalone, pure 2D flat graphic artwork.
- DO NOT include any leather texture, coated canvas weave, bumps, embossed 3D relief, or surface grain.
- DO NOT include any bag, garment, seams, stitching, wrinkles, folds, creases, or perspective distortion.
- DO NOT include any shadows, studio lighting gradients, specular highlights, reflections, glare, or vignette.
Every dot and background region must have uniform luminance and flat, print-ready consistency across the entire canvas.
```

---

## 6. Asistan İçin Çalışma Kuralı (Otomatik Tetikleyici)

Kullanıcı bu çalışma alanında:
- Bozuk, eksik, düşük çözünürlüklü, kırışık veya **model üzerinde giyilmiş** bir tişört/elbise/kumaş görseli yükleyip **"bunu düzeltmek için prompt ver" / "Nano Banana Pro promptu oluştur"** dediğinde:
1. Görseli **Bölüm 2'deki 7 maddelik kontrol listesine** göre en ince ayrıntısına kadar analiz et (hiçbir motifi, nokta/çizgi yapısını veya rengi atlama).
2. Kısa bir **Görsel Analiz Özeti (Türkçe)** sun.
3. Ardından **Bölüm 3 ve 4'teki Global + Değişken Şablona** sadık kalarak doğrudan **Nano Banana Pro**'ya yapıştırılmaya hazır **İngilizce** promptu kod bloğu içinde ver.
