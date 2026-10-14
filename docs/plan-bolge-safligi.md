# Plan: bölge saflığı (rengin içinde olmaması gereken renk) — 2026-10-14

## Kullanıcı geri bildirimi (kız, tüm görsel, v7.1)
1. Kahve yaprakların içinde ve kenarında **açık mavi** benekler.
2. Arkadaki turkuaz fırça darbesinin içinde **koyu kahve** noktalar/çizgiler.
3. Saç tokasındaki çiçek kaynakta **düz** turkuaz; çıktıda içinde lekeler/doku.

## Ölçülen nedenler (v7.1 filmleri üzerinde)
| Sorun | Ölçüm | Neden |
|---|---|---|
| 1 | Açık Mavi mürekkep kroması 9,1 | Zıt renk kuralı ve kalite kontrol yalnızca kroma >12 mürekkeplere bakıyordu; açık mavi "nötr" sayılıp kuraldan kaçtı. Bej/taupe yaprakları grileştirmek için açık mavi karıştırıldı. |
| 2 | Koyu Kahve mürekkebinin %14'ü soğuk (turkuaz) alanda | En koyu mürekkep (L<30) ince detay için kuraldan muaftı; program bu muafiyeti turkuazı **koyulaştırmak** için kullandı. |
| 3 | Kaynak çiçekte yerel std ≈1,8 (düz) | Düz alan da piksel piksel karışımla tramlandı; kâğıt dokusu/gürültü büyütüldü, düz alan tek mürekkep olarak tutulmadı. |

Ortak kök: karışım **piksel bazında** seçiliyor; pikselin hangi **bölgeye/renk ailesine** ait olduğu bilinmiyor.

## Düzeltme planı
1. **Kaynağı ön temizle**: kenar koruyan yumuşatma (bilateral/guided ya da mean-shift) ile kâğıt dokusu ve gürültüyü düz alanların içinden sil, kenarları koru.
2. **Bölgelere ayır**: yumuşatılmış görüntüyü renk + konumla bölgelere böl (süperpiksel/segmentasyon). Her bölge için: baskın ton ailesi, ortalama renk, iç varyans.
3. **Bölge başına izinli mürekkepler**: bölgenin ton ailesindeki mürekkepler (en fazla 2) + kâğıt. Başka aileden mürekkep o bölgede **yasak** (kroma eşiği yok, açık/soluk renkler dahil; ton açısı kroma ≥5'ten hesaplanır).
4. **En koyu mürekkep yalnızca çizgi/detayda**: kaynakta ince koyu çizgi/kontur maskesi (koyu + yüksek kenar + ince) çıkar; en koyu mürekkep sadece orada. Ton koyulaştırmak için başka aile mürekkebi kullanılmaz. Gerekirse palette o aileye koyu ton eklenir (renk sayısı izin verirse) ya da ton biraz açık kalır.
5. **Düz bölge = tramsız**: iç varyansı düşük bölge tek mürekkep, sabit kaplama; mürekkebe çok yakınsa %100 dolu (tramsız), değilse tek sabit ton (düzgün tram, gürültüsüz).
6. **Kenar ara tonları**: iki bölge arasındaki anti-alias pikselleri komşu bölgelerden birine atanır; üçüncü renk oluşmaz.
7. **Palet seçimi aile bazında**: önce ton ailelerini bul (sıcak/kahve, turkuaz/mavi, nötr), mürekkep sayısını ailelere alan ve ton aralığına göre dağıt; neredeyse kullanılmayan mürekkep (<%1) bırakılmaz.
8. **Kalite kontrolü genişlet**: (a) her bölgede yabancı aile mürekkep payı, (b) düşük kromalı mürekkepler dahil ton uyumu, (c) düz bölgede kaplama varyansı (leke), (d) en koyu mürekkebin çizgi maskesi dışındaki payı.
9. **Test**: kız görselinde kullanıcının gösterdiği üç yerde (%100 kesit: kahve yaprak, sol fırça, saç çiçeği) + ölçüm: yabancı mürekkep payı ≈0, düz bölgede leke yok. Ayıyla da tekrar dene (geriye dönük bozulma kontrolü).

## Uygulama yeri
- `tools/gorsel_am.py`: 1–7 (yeni ön işleme + bölge kısıtlı karışım).
- `tools/kalite_kontrol.py`: 8.
- Sonuç ve dersler: `docs/ogrenilenler.md`, deneme kaydı: `docs/yontem-gunlugu.md`.
