# Photoshop ve çalışma ortamı notları

Teknik, pratik dersler. Çoğu deneyimle öğrenildi [deney].

## Ortam
- Kullanıcı: Windows PC, Photoshop 2021 (ve 2026 kurulu), Claude masaüstü uygulaması. Photoshop kapalıysa `computer_open_application` ile açılır (splash + ana ekran gelir).
- Claude bulut ortamı (Linux, 2 çekirdek, ~8 GB RAM): ağır işlemler burada yapılır. Python: `numpy`, `opencv-python`, `Pillow` yeterli.
- Kullanıcının kendi bilgisayarındaki kabuk (`device_bash`): Linux VM; **180 sn sınırı** var, **arka plan işlemi komut bitince sonlandırılır**, 4 GB RAM. Uzun işlerde dosyayı bulut ortama alıp (`device_stage_files`) orada çalıştır, sonucu `device_commit_files` ile geri yaz.

## Bilgisayar kontrolü (computer use)
- Erişim 30 dk işlem yapılmazsa **sona erer**; `computer_resolve_access` + `computer_request_access` tekrarlanır.
- Photoshop'u öne almak için `computer_open_application`; hemen ardından tıkla. Arada ekran görüntüsü/bekleme olursa odak başka pencereye (Explorer, Claude penceresi) kayabilir ve "desktop shell frontmost" hatası çıkar.
- Claude penceresi sağ paneli (Channels paneli) kapatabilir; panel dışına tıklarken dikkat.
- Menü yolu: `File > Scripts > Browse...` → dosya penceresine tam yol yazılır → Enter. (Tam ölçek koordinatları: File ≈ (33,9), Scripts ≈ (50,375), Browse ≈ (243,531), dosya adı kutusu ≈ (340,361).)
- Büyük belgede betik uzun sürer; Photoshop bu sırada ekranı güncellemez. Bitmeden sonuç kontrolü yapma (30–90 sn bekle).
- `alert()` çıktısı çoğu zaman görünmüyor (`DialogModes.NO`); sonucu ekrandan/kanal panelinden doğrula.

## Kanalları Photoshop'a aktarma (ExtendScript)
- `app.open(png)` 1-bit PNG'yi Bitmap modunda açar → `changeMode(ChangeMode.GRAYSCALE)`.
- İlk belgeyi `ChangeMode.MULTICHANNEL`'a çevir; diğer filmleri `selection.selectAll(); copy();` → hedef belgede `channels.add()` → `activeChannels=[ch]` → `paste()`.
- **Önemli:** `channels.add()` ile eklenen kanal *maske* kanalıdır; bileşik görünüm kırmızı kaplama gösterir. Her kanal için `ch.kind = ChannelType.SPOTCOLOR; ch.color = new SolidColor(...)` yapılmalı. İlk (bileşen) kanalın rengi değiştirilemez, görünürlüğü kapatılır.
- Aynı betikte oluşturma + renk atama **çalışmadı**, iki ayrı betik çalıştı (`koyu_tisort_photoshop.jsx` sonra `koyu_renk_duzelt.jsx`). Nedeni araştırılmalı.
- 124 MP × 5 kanal ≈ 620 MB; Photoshop'ta sorunsuz.
- Film PNG'lerinde **siyah = mürekkep** (Photoshop spot/CMYK kanal kuralı).

## Dosya biçimi
- 1-bit PNG, 508 PPI (eskiden 600; kullanıcı 2026-10-14 508 istedi) meta verisiyle (`dpi=(508,508)`). 124 MP'lik bir film yaklaşık 0,3–0,9 MB.
- Belgenin PSB olarak kaydı henüz yapılmadı (~900 MB beklenir).

## Python işlem notları
- 124 MP için kareler (tile) halinde çalış (256–384 satır), `cv2.warpAffine` ile büyütme.
- Morfolojik daraltma/genişletme büyük çekirdekte yavaş: `cv2.distanceTransform` ile (eşik) yap.
- Bellek: etiket haritası uint8 (124 MB); bileşen etiketleri int32 (500 MB) — sırayla sil.
- `cv2.medianBlur` etiket görüntüsünde yeni sınıf üretmez (sıralı etiketlerde iyi çalışır).
