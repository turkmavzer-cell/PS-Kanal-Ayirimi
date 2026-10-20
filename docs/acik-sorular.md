# Açık sorular ve yapılacaklar

## Atölyeye / ustaya sorulacaklar
(Araştırma raporundan uyarlanmıştır.)
1. Elek: renkler ve underbase için hangi T numarası ve iplik kalınlığı?
2. Film mi basılıyor, doğrudan kalıba (CTS/CTP) mı pozlanıyor? Film ise hangi yazıcı, Dmax yeterli mi?
3. Mürekkep: plastisol, su bazlı, pigment, discharge?
4. Tişört rengi? Lacivert-siyah alanlar basılmayıp kumaş rengi mi kullanılsın?
5. Underbase düz mü tramlı mı? Choke miktarı (punto/mm)?
6. Pres manuel mi otomatik mi? Butt registration mı trap mı? Trap payı kaç mm?
7. Dosya biçimi: katmanlı vektör (AI/PDF/EPS), spot kanallı PSD/TIFF, ayrı 1-bit film? Çözünürlük?
8. En ince çizgi ve en küçük yazı için minimum kalınlık (ör. 0,3 mm / 8 pt)? Mandala çizgileri açılır mı?
9. Renk sırası ve ara kurutma?
10. Kayıt işareti biçimi, pozlama testi, ilk provayı onaya gönderme? Ayrıca **"lap" ile ne kastediliyor?** (araştırmada doğrulanamadı)

## Geliştirme listesi
- [ ] Palet otomatik tespiti `tramsiz.py`'ye eklensin (v2'deki k-means + ara ton eleme kodu). Renk sayısı komut satırından verilebilsin (`--renk 6`).
- [ ] Turuncu/kırmızı ve krem/beyaz ayrımı için palet genişletme seçeneği.
- [ ] Anahattı açık kapalı şekiller (örn. "E" harfi): kapatma/doldurma seçeneği veya uyarı.
- [ ] Vektöre çevirme (trace) yolu: ne zaman raster yeterli, ne zaman şart?
- [ ] Kayıt işaretleri ve film kenar bilgisi (renk adı) eklensin.
- [ ] Film çıkışı: 1-bit PNG yeterli mi, TIFF/PDF mi isteniyor?
- [ ] Belgeyi PSB olarak kaydetme adımı.
- [ ] Birleşik JSX betiğinin renk atamayı neden uygulamadığı; tek betiğe indirme.
- [ ] Gerçek degradeli tasarımlar için **karma** (düz + yalnızca geçişte tram) mod; tramı RIP'e bırakma.
- [ ] Başka test görselleri (logo, yazı ağırlıklı, degradeli) ile yöntemi sına.
- [ ] Underbase seçenekleri: düz / tramlı (%60–70), Siyah altına konma tercihi.

## Karar bekleyenler
- Usta ve atölye onayı: v3 filmleri gerçek baskıda denenmedi.
- Koyu tişörtte lacivert-siyah anahatların görünmemesi tasarım değişikliği gerektirebilir (anahat rengi).


## Eklenenler (13 Ekim)
- [ ] Atölye: 0,127 mm (3 px) ve 0,085 mm (2 px) dagitik tram noktasi hangi elekte basilabilir? Ayicik icin FM mi AM mi tercih?
- [ ] Ayicik koyu tisort seti (underbase) istenirse eklenecek.
- [ ] hibrit.py: palet ve esikler otomatik/parametrik olsun; `--koyu` secenegi.
- [ ] Mandala v4: lacivert cizgi kanali, krem/sari kontur, potrace tabanli arac `tools/` altina alinacak.
- [ ] Ayicik: `GAM=1 SHARP=0.25` ile tum gorseli yeniden ayir, cene/göz/yanak kontrol et, filmleri ve PSD'yi guncelle.
- [ ] Koyu bolgelerdeki dagnik tek beyaz noktalar (parlama maskesi kalintisi) temizlensin.

- [x] Koyu alanlardaki beyaz benekler SPEC_MIN ile temizlendi (v5.3).
- [ ] Atölye (WhatsApp grubu) görüşü bekleniyor: 3 px (0,127 mm) nokta baskıda tutar mı; siyah kanal (%0,17) ayrı film olarak mantıklı mı; elek/mürekkep/film türü.
- [x] Ayıcık AM tram denemesi yapıldı (45 lpi, 15°, yuvarlak nokta, tek açı, 9 film; hibrit2.py AM=1). Açık: mürekkep başına ayrı açı/moiré, 45 lpi yeterli mi, siyah kanal çok küçük — atölye görüşü bekleniyor.
- [ ] Atölyenin makine kafa sayısı (6? 8?) ve kurutma durumu → hedef mürekkep sayısı; ayıcık için 6/7/8 renkli azaltılmış set (siyah, 3 kahve, lacivert, +beyaz/fon). Beyaz tişörtte fon yok, Be Gentle içi kâğıt rengi; koyu tişörtte beyaz mürekkep gerekir.
- [ ] Atölyeye sor (karar rehberi bölüm 8): açı (15°/25°/45°), elek sayısı, nokta büyümesi kompanzasyonu, en küçük basılabilir nokta/detay, kafa sayısı, siyah gibi küçük kanalın birleştirilmesi, spot yığılma mı CMY+K mı.
- [ ] Kız kişisi: PSD'yi yeniden oluştur (düzeltilmiş filmler `Emprime_Kiz_AM_508`'de; Photoshop'ta bilgisayar erişimi gerekir). Bej kanal %0,21 → atılıp 5 renge inilebilir.
- [ ] analiz.py/kalite_kontrol.py eşikleri atölye geri bildirimiyle ayarla; hale (upscaler) ölçümü henüz yok.
- [x] **Bölge saflığı planını uygula** (v8, `tools/bolge_am.py`; segmentasyon yerine ton ailesi + yumuşatma kullanıldı) (`docs/plan-bolge-safligi.md`): ön yumuşatma, bölge segmentasyonu, bölge başına izinli mürekkep, en koyu yalnızca çizgide, düz bölge tramsız, kenar ataması, aile bazlı palet, kalite kontrolü genişlet; kız + ayıda test.
- [ ] bolge_am: aile içinde koyu ton gerekirse (koyu turkuaz kontur) aileye koyu mürekkep ayır; elbise beyazı/kâğıt ayrımı için daha iyi figür maskesi.
- [ ] bolge_am'ı ayıda dene (geriye dönük kontrol).
- [ ] İki aşamalı yöntemi gerçek görselle dene (önizleme 75 MP indexed PNG Photoshop'ta düzenleme hızı; Color Table ile renk değişimi; 2. aşamada artık piksel raporu).

- [ ] Kız kişisi v9.1: önizleme (İndirilenler\Emprime_Kiz_Onizleme) kullanıcı onayı bekleniyor; onaydan sonra `onizlemeden_ayir.py ... acik onizleme_palet.json`, kalite kontrol, PSD. Elbise bölgesinde izole koyu nokta/yüzde beyaz nokta temizliği (MINPX) değerlendirilebilir.

- [ ] "Lap" tam olarak ne demek? (Erkut'a sor: düz taban + tram mı, üst üste baskı mı?) Cevaba göre film aşamasında taban filmi altlığı uygulanacak.
- [ ] LAP=1 önizlemesi onaylanırsa `onizlemeden_ayir.py`'de taban + nokta üst üste (overprint) desteği.

## Eklenenler (20 Ekim) — bölge/mürekkep katmanları
- [x] `japon_katmanli.psd` kullanıcı tarafından açılıp kontrol edildi: "başarılı, katmanlar başarılı ayrıştırılmış" (2026-10-20).
- [ ] Teslim edilen PSD'nin adları Türkçe karakterli; kullanıcı sonucu başarılı buldu, ASCII sürüm istemedi. Kural (ASCII ad) geçerli kalır; bu dosya için yeniden üretim yapılmadı, sonraki işlerde baştan ASCII ver.
- [ ] Fuji'nin alt koyu kütlesi Dağ grubuna verildi; kullanıcı başka istiyor mu?
- [ ] Siyah katmanlardaki yarı saydam kâğıt dokusu kabul mü, eşikle sıfırlansın mı (daha temiz, kenar yumuşaklığı azalır)?
- [ ] Bölge maskesini otomatik çıkaran genel yol yok (örnek el çizimi çokgenlerle kılavuzlu); başka görselde yeniden kurulacak.
