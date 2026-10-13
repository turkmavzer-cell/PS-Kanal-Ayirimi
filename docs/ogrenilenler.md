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
| Süslemeli, çok detaylı düz renkli çizim | Tramsız spot, sık elek, 600 PPI | İnce çizgi (≈0,3 mm altı) baskıya uygun değil |
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

1. Baskı ölçüsünde **600 PPI** (38,5 cm genişlik → 9094 px). [rapor: küçük yazı için 600 dpi]
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
