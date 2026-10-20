# Onaylı dosya 654 — çalışma stili (2026-10-20)

Kullanıcı `İndirilenler\654` klasörünü "onaylı, doğru çalışma stili" diye verdi. Burada **ölçülenler** ve **çıkarımlar** ayrı yazıldı. Marka/müşteri adı bilerek yazılmadı.

## Klasör
- `654 j.jpg` — 3187×3487 düzleştirilmiş önizleme (beyaz zeminde siyah sıçrama + spor ayakkabı + alt tarafta beyaz üstüne beyaz logo, görünmez).
- `654 layer.psd` — 660 MB, 10791×11808, **CMYK 8 bit**, 4 kanal, 5 katman.
- `654.psd` — 783 MB, 10791×16249 (alta +4441 px boş tuval), CMYK + **16 ek kanal** (1 saydamlık + 15 spot).

## Ölçülenler
- **Çözünürlük 508 PPI** (PSD çözünürlük bilgisi 33292288/65536 = 508). 10791 px ≈ 54 cm; sanat alanı 11808 px ≈ 59 cm yükseklik.
- Katmanlar (alttan üste, hepsi görünür): ayakkabı (eğik, yumuşak alfa) · sıçrama negatifi (siyah zeminde beyaz, opak) · sıçrama (beyaz üstüne siyah, opak) · logo (CMYK %0 = beyaz, alfa ile) · ayakkabı (düzeltilmiş duruş, yumuşak alfa). Yani katman dosyası kaynak/hazırlık, kanal dosyası ayrım.
- Belge baskı bilgisinde CMYK ekran: C 47,4 lpi 108,4° · M 47,4 lpi 161,6° · Y 50 lpi 90° · K 53 lpi 45° (Photoshop varsayılan nokta şekli 6; kanal içeriği tram değil, sürekli ton).
- 15 spot kanal adları "Cyan copy 5", "Black copy 2", "Green copy" gibi: CMYK kanalı çoğaltılıp spota çevrilmiş, **adlandırılmamış**. Alternatif renkleri Lab olarak tanımlı: **beyaz** (L=100) kanal 6, 9, 16, 19 · **gri** (L≈52) kanal 7, 10, 13, 17 · **siyaha yakın** (L=0) kanal 8, 11, 14, 18 · **siyaha yakın** (L≈4) kanal 5, 12, 15 (bu üçü tüm tuvalde tek değerli, yani boş/yer tutucu).
- Kanal içerikleri (kanal 0–3 = CMYK bileşik; hepsi 508 PPI tuvalde):
  - 6, 7, 8: sıçrama — 6 sert siyah gövde, 7 orta ton, 8 açık ton (aynı yerde üst üste biner; ton dilimleri).
  - 9: ayakkabı silüeti, sert tek renk (beyaz tanımlı). 10, 11: ayakkabı orta ve açık ton (sürekli ton).
  - 13, 14: ayakkabı + sıçrama orta/açık ton, sürekli ton (233 seviye).
  - 16: sert birleşim maskesi = ayakkabı silüeti + sıçrama gövdeleri + logo (beyaz tanımlı, alt taban gibi).
  - 17, 18: aynı 13/14 içeriği **1 bit AM tram**: ölçüm (FFT) ≈ **45 lpi, 15°** (nokta periyodu 11,2 px).
  - 19: logo, sert, beyaz tanımlı (iki boyutta).
- Alt 4441 px şeridi tüm kanallarda boş.

## Çıkarım (doğrulanmadı)
Çalışma stili: (1) CMYK'de katmanlı hazırlık (ayakkabı, sıçrama, logo ayrı katman, saydam kenarlı); (2) kanalları çoğaltıp **ton dilimleriyle** spot kanallara ayırma (sert gövde / orta ton / açık ton); (3) sert **birleşim silüeti** ile alt taban (beyaz); (4) nihai film kanallarının **1 bit AM tram 45 lpi 15°** olarak üretilmesi; (5) logonun ayrı sert kanal. Mürekkep tanımı beyaz + gri + siyah gibi görünüyor; tişört rengi bu dosyadan bilinmiyor.

Projedeki önceki AM denemesi (45 lpi, 15°, tek açı, yuvarlak nokta) bu stille uyumlu.

## Açık / sorulacak
- Tişört rengi ne (beyaz taban gerekçesi)? Sıçrama negatif katmanı koyu tişört içinse bu dosya koyu set.
- Kanal 5, 12, 15 boş mu, bilerek mi?
- Gri spotun gerçek mürekkep rengi/karışımı ve her kanalın baskı sırası dosyada yok.
- 13/14 sürekli ton kanalları ile 17/18 tram kanalları ikisi de dosyada: film olarak hangisi gidiyor?

## İnceleme tekniği (not)
650–800 MB CMYK PSD'yi 4 GB'lık cihaz kabuğunda `psd-tools` ile açmak yerleşik: katman yapısı `PSDImage.open` + kanal başına `ch.get_data`; birleşik görüntü kanallarını **RLE satır tablosundan seyrek satır okuyarak** çözmek (her 48. satır, her 8. piksel) 20 kanalı ~3 sn'de verdi; tam çözünürlük kırpma aynı yolla.
