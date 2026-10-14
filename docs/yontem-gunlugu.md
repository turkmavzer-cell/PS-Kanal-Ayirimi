# Yöntem günlüğü

Her deneme için: ne yapıldı, parametreler, sonuç, karar. Yeni denemeler en alta eklenir.

Test görseli: Gemini üretimi mandala + "BE BRAVE" tipografi (`Gemini_Generated_Image_9clbdv9clbdv9clb.jfif`, 1686×2528 px, 300 PPI, 14,27×21,4 cm). Düz renkli, ~4 mürekkep. Görsel repoda **tutulmaz**; yerelde İndirilenler klasöründeydi.

---

## v1: CMYK kanal bölme (reddedildi)
- Photoshop'ta `Image > Mode > CMYK`, ardından Channels panel menüsünden `Split Channels`.
- Çıktı: Cyan, Magenta, Yellow, Black gri tonlu 4 belge.
- Sonuç: Kullanıcının istediği "emprime renk ayrımı" bu değildi. Bkz. `ogrenilenler.md` §2.1.
- Not: Photoshop'ta orijinal belge ayrımla kapanır; geri almak için dosya yeniden açılmalı.

## v2: Otomatik spot ayrım + tram (reddedildi)
- Araç: `tools/arsiv/emprime_tramli_YANLIS.py`
- Parametreler: 508 PPI, 38,488 cm genişlik, 45 lpi, açılar 45/15/75/0..., en çok 24 renk, k-means (Lab) + iki renk karışım modeli, her mürekkep için TRAM + tramsız YEDEK, beyaz zemin (0,15 mm choke), 1-bit PNG kanallar.
- Photoshop'a Multichannel olarak aktarım: `tools/arsiv/multichannel_olustur_tramli.jsx` + renk düzeltme `tools/arsiv/kanal_renkleri_duzelt_tramli.jsx`.
- Sonuç: Palet 4 mürekkebe indi (2 ara ton elendi). Görsel olarak orijinale yakın simülasyon, ama usta dosyayı **kötü buldu**; sebep: düz renkli iş trama çevrilmiş. Bkz. `ogrenilenler.md` §2.2.
- İlk denemede 6 mürekkep çıkmış, 2'si kenar ara tonuydu (gri halelere yol açtı); ara ton eleme eklendi.
- Photoshop gözlemi: kanallar `channels.add()` ile maske kanalı olarak eklenir; bileşik görünüm **kırmızı** olur. Spot Color'a çevirmek gerekir (`ogrenilenler.md` / `photoshop-ve-ortam-notlari.md`).

## v3: Tramsız spot ayrım (güncel)
- Araç: `tools/tramsiz.py`
- Girdi: görsel, çıktı klasörü. Palet şimdilik **kodda sabit** (`INKS`): Siyah `24,25,47`, Mavi 1 `9,43,121`, Mavi 2 `59,113,158`, Kırmızı `231,47,15`. (Önceki otomatik tespitten.)
- Parametreler: 600 PPI, 38,5 cm genişlik (9094×13636 px, 124 MP), trap 4 px, choke 2 pt (17 px), medyan 5, ince parça yarıçapı 3.
- Süre: ~2,5 dk sınıflandırma + ~40 sn son işlem (2 çekirdek, 8 GB bellek bulut ortamı).
- Çıktı: `Acik_Tisort/` (4 film), `Koyu_Tisort/` (underbase + 4 film), önizlemeler.
- Photoshop: `tools/photoshop/koyu_tisort_photoshop.jsx` kanalları Multichannel belgeye toplar; ardından `koyu_renk_duzelt.jsx` Spot Color + renk atar.
- Sonuç (gözle): %100'de düz ve keskin kenar; renkler orijinal ile uyumlu; ince Mavi 2 halelerinin çoğu temizlendi, çok küçük kalıntılar var.
- Bilinen sorunlar:
  1. Kaynakta sağ taraftaki "E" harfinin anahattı açık (orta çıkıntının alt kenarı yok) → koyu tişört setinde bu harfin beyaz dolgusu "dış" sayılıp basılmıyor. (`docs/ornekler/E_harfi_acik_anahat_sorunu.png`)
  2. Koyu tişörtte lacivert-siyah anahatlar görünmez olur; "MMXXIV", rakamlarda beyaz dolgular tuhaf kalır (tasarım sorunu).
  3. Turuncu ve kırmızı tek "Kırmızı"da; krem konturlar beyaza katılıyor. Kullanıcı ayrı tonlar isterse palet genişletilmeli.
  4. Birleşik betik (oluştur + renk ata tek dosyada) Photoshop'ta renkleri uygulamadı; **iki ayrı betik** şeklinde çalıştı. Nedeni bilinmiyor.
  5. Palet otomatik tespit edilmiyor (v2'deki tespit kodu v3'e taşınmadı).
- Karar: Usta ve atölye onayı bekleniyor (elek, film türü, kayıt tipi).

## v3.1 / v4 denemeleri (mandala, 13 Ekim) - sadece kirpma testi, repoya arac eklenmedi
- v3'te 4 mürekkep kaldigi icin acik mavi yaprak, turuncu vurgu, krem kontur kayboldu; medyan 5 + ince parca temizligi ince kalem cizgilerini kalinlastirdi/kopardi.
- Deneme A: 6 mürekkep + once buyut, olasilik haritasini Gaussian yumusat, sonra argmax: kenarlar akici, ama lacivert/beyaz sinirinda sahte acik mavi/turuncu kiymik cikti (kenar ara tonu).
- Deneme B: A + bilateral kaynak temizligi + kucuk parca silme + potrace (`potracer`, bezier) ile vektor iz: kiymiklar gitti, akici egriler; ama ince cizgiler kalinlasti, kucuk sari cicek/krem kontur kayboldu. Kaynak zaten bulanik; kalem dokusu kaynaktan cikmaz.
- Siradaki: lacivert cizgiyi parlaklik tabanli ayri kanal olarak iz surmek, yumusatmayi yalniz genis alanlara uygulamak, krem/sari kontur icin ayri mürekkep denemek. Daha yuksek cozunurluklu kaynak sorulacak.

## v-hibrit: Ayicik gorseli (fotografik + duz yazi) (guncel, acik tisort)
- Girdi: `Tatli Gunun Sevimli Ayicigi.png` 1024x1536 (yazi lacivert duz, rozet duz, ayicik kabarik tuy fotograf gibi). Arac: `tools/hibrit.py` + `tools/fs_dither.c` (C, serpantin Floyd-Steinberg, dogrusal RGB).
- Yontem: yazi + yildizlar + rozet = tramsiz spot (alt-piksel kenar, kübik buyutme + esik); ayicik = dagitik tram (FM) cok mürekkepli indeks ayrimi (Krem, Karamel, Kahve, Koyu Kahve); rozet duz dolgusu Koyu Kahve filmini paylasir. Nokta 3 px = 0,127 mm @600 PPI (varsayilan); 2 px = 0,085 mm cok ince. 5 film, 9094x13641.
- Test sonucu: ayicigi duz renge indirmek (5 kahve) tuyu leke leke yamaya cevirdi, kullanici kabul etmedi. Dagitik tram kabul.
- Not: bilesen analizi ile ayicik/rozet otomatik ayrildi (en buyuk iki bilesen); lacivert = Lab b* < -8. Palet kodda sabit.
- Bilinen: tram noktasinin elek/pozlama ile basilabilirligi atölyeye sorulmali; koyu tisort seti yapilmadi; esik/anti-aliasing icin trap yok (indeks noktalar birbirine degmez).

## v5: Seffaf kesim + 6 mürekkepli dagitik tram (Ayicik, guncel)
- Arac: `tools/hibrit2.py` (+ `fs_dither.c`). Kullanim: `python3 tools/hibrit2.py girdi.png cikti [nokta_px=3] [obje_murekkep=6]`.
- Sorunlar (v-hibrit): (1) cene altı gölge detayi kayboldu: gölgeler en koyu mürekkepten (66,41,32) daha koyuydu, o aralik duz bloga ezildi; (2) göz parlamasi soldu: kucuk beyaz leke buyutmede yumusadi, hata yayilimi onu mürekkep noktasina cevirdi.
- Cozum: duz beyaz arka plandan seffaf kesim (kenara bagli beyaz = arka plan, kenar kusaginda color-to-alpha + renk temizligi; icerideki beyazlar korunur) -> `Kesim/ayicik_seffaf.png`, `yazi_rozet_seffaf.png`; obje icin k-means ile 6 mürekkep, en koyu mürekkep = gercek en koyu golge tonu (3. yuzdelik ortalamasi); parlama korumasi (L>96,5 ve alfa>0,5 = mürekkep yok); yerel kontrast (unsharp 5 px, miktar 0,5).
- Olcum (ayicik, nokta bulaniklastirilmis ΔE): 4 renk ort 8,3 / en kotu %5 24,4; 5 renk 6,8/15,4; 6 renk 5,5/12,4; 7 renk 5,1/13,0; 8 renk 4,4/11,3 -> 6 renk dirsek noktasi.
- Ilk parlama esigi L>93 krem burnu beyaza ucurdu (yanlis); 96,5'e cikarilinca krem korundu, göz parlamasi beyaz kaldi.
- Sonuc: cene detayi geri geldi, burun kremi korundu. 7 film (6 kahve tonu + lacivert; rozet en yakin kahve filmini paylasir). Bilinen: koyu bolgelerde dagnik tek beyaz noktalar (parlama maskesi kalintisi); nokta 2 px (0,085 mm) elek icin zor, 3 px varsayilan.

## v5.1: Sol yanak "parcalanma" teshisi ve duzeltme (13 Ekim, denendi, henuz uygulanmadi)
- Belirti: ayicigin sol yanaginda duz karamel yamalar + yogun siyah noktali alanlar, arada orta ton yok (`docs/ornekler/ayicik_yanak_parcalanma_karsilastirma.png`).
- Neden: (1) en yakin murekkep secimi dogrusal isik uzayinda yapiliyordu; orada koyu tonlar birbirine cok yakin, orta-koyu kahveler secilmiyor, piksel ya Karamel'e ya Siyah Kahve'ye gidiyordu. (2) yerel kontrast (unsharp 0,5) bu sicramayi buyuttu. (3) kaynak bu bolgede zaten bulanik.
- Duzeltme: secimi algisal uzayda yap (C kodunda `sqrt` ile gama 2; `fs_dither(..., gam=1)`), hata yayilimi dogrusal kalir. `tools/hibrit2.py` artik `GAM` (varsayilan 1), `SHARP`, `SPEC_L`, `CROP` ortam degiskenlerini okur.
- Karsilastirma: algisal secim + kontrast 0,5 orta tonlari geri getirdi; kontrast 0 en yumusak ama tuy dokusu az. Onerilen: algisal secim + kontrast ~0,25 (denenmedi, tum goruntude cene ve göz parlamasi tekrar kontrol edilmeli).
- Not: `onizleme`/PSD ciktilari v5 (dogrusal secim, kontrast 0,5) halinde; yeni ayar henuz filmlere uygulanmadi.

## Katmanli PSD uretimi: kavisli yazi + ozgun cizim top (13 Ekim)
- Istek: referans gorsel (Lakers sweatshirt fotografi) logolar olmadan, yalniz yazilar + ortadaki top, her nesne ayri katman, yuksek kalite PSD.
- Karar: marka logolari/wordmark yeniden uretilmedi; top ozgun cizildi (referans kopyalanmadi). Referans 663x738 kumas fotografi oldugu icin kaynaktan "net" cikarim yapilmadi, yerlesim sifirdan kuruldu.
- Arac: `tools/tasarim/kavisli_yazi_top.py` (Orbitron OFL fontu, U yolu uzerinde harf harf yerlestirme, kontur yazi, degisken kalinlikli tarama, ortografik dunya haritasi kareli doldurma, 3B dikisler) -> katman PNG'leri + `katmanlar.json`; `tools/tasarim/katman_psd_olustur.jsx` Photoshop'ta PSD'yi kurar ve kaydeder (betikle kaydetmek Farkli Kaydet penceresi sorunlarini onler).
- Cikti: 7087x7889 px, 600 PPI (30 x 33,4 cm), 9 katman (Zemin, Yazi Ic cumle, Dis sol/alt/sag, Top Govde/Tarama/Harita/Dikisler). Katmanlar raster (canli metin degil).
- Ders: Claude masaustu uygulamasi odagi calan betik sirasinda one gecebiliyor; `open_application` + ekran goruntusu ile dogrula. Photoshop betik calisirken tiklamalar islenmez.

---

## Şablon (yeni deneme için)
```
## vN: <ad> (<durum>)
- Araç / commit:
- Girdi ve parametreler:
- Sonuç:
- Sorunlar:
- Karar:
```

## v5.2 — ayı.jfif yeni varyant (2026-10-14)
- Girdi: İndirilenler/ayı.jfif (1024x1536). Ayarlar: GAM=1, SHARP=0.25, 6 mürekkep, 3 px nokta, 600 PPI, 38,5 cm.
- Sorun: rozet ayıyla birleşti, yazı kenar parçacıkları ayı sınırını şişirdi. Çözüm: bileşenler 3x3 close sonrası alan>1500 ve min kenar>40 ile süzüldü; küçük parçalar en yakın büyük bileşene ≤30 px mesafede atandı.
- Yeni: CROPS env (isim:x0,y0,x1,y1;...) ile çoklu yakın plan kesimi.
- Gözle kontrol (yüz/kol/pati): detay ve parlama korunmuş; yüzde koyu alan kenarlarında küçük beyaz benekler var (açık soru).
- Dosyalar henüz PC'ye yazılmadı; kullanıcı onayı bekleniyor.

## v5.3 — çene altı kaybı + beyaz benekler (2026-10-14)
- Kullanıcı önizlemede çene altı gölgesinin kaybolduğunu gördü. Teşhis: 6 mürekkepte gölge tonu "Siyah Kahve" (≈32,24,20) ile "Koyu Kahve" (≈92,60,38) arasında kalıyor; arası açık olduğu için gölge düz Koyu Kahve lekesine dönüşüyor, ağız çizgisi silikleşiyor.
- Düzeltme: ayı mürekkep sayısı varsayılanı 6 → 7 (lacivertle 8 film). Gölge bandı, ağız çizgisi ve tüy dokusu geri geldi (gözle doğrulandı).
- Beyaz benekler: parlama maskesi (L>SPEC_L) 20 noktadan (SPEC_MIN) küçük bileşenlerde iptal edildi; yüzdeki beyaz beneklar gitti.
- Palet isimleri 7 ton için güncellendi (Orta Kahve eklendi).
- v5.3 teslim: İndirilenler\Emprime_Ayicik_v53 (8 film 600 PPI, Kesim, önizleme, kanallar_hibrit.json). PSD tek betikle (tools/photoshop/psd_olustur_tek_adim.jsx: kanal birleştirme + spot renk + kaydet) Photoshop 2021'de üretildi, 8 spot kanal doğrulandı, saveAs copy=true olduğu için açık belge adı 01_Krem.png kalır; kaydedilen PSD ayrıca açıldı.

## v5.4 — siyah mürekkep, kulak/karın düz leke, beyaz noktalar (2026-10-14)
- Kullanıcı: siyah ekle; koyu bölgede beyaz noktalar olmasın; kulak ve karın yüz gibi homojen detaylı olsun; "neden bir yeri düzeltirken başka yer bozuluyor?"
- Kök neden (kayıt altında): palet görüntü başına tek sefer k-means ile seçiliyordu ve sonuç gözle tek bölgede (çene, sonra yüz) kontrol ediliyordu. Büyük koyu kütleler (kulak çekirdeği, karın) kaynak tonu bir mürekkep rengine denk gelince FS hata yayılımı hiç karışım üretmiyor → düz leke. Palet 2-3 birim kayınca bir bölge düzeliyor, başka bölge düz lekeye dönüyor (örn. siyah kahve 32→34 ya da dengeli örnekleme).
- Çözüm: (1) palet adayları (3 tohum × 2 dengeleme × 3 koyu bant) gerçekten tramlanıp puanlanır: puan = ton hatası + 0.5 × koyu kütlelerdeki düz leke %; en iyisi seçilir. (2) Her çalışmada bölge testi çıktısı (yüz, çene, kol, ayak, kulak, karın: ΔE, doku oranı, düz leke %). (3) Doku eşitleme (TEX_G): detay enerjisi düşük bölgelerde yerel kontrast kazancı. (4) Nötr siyah mürekkep: koyu gölgeler nötr; kahve-siyah ona uymuyordu. (5) Beyaz nokta: koyu/orta bölgedeki izole kağıt pikselleri en yakın mürekkebe çevrilir; küçük parlama bileşenleri (<20 nokta) iptal.
- Yanlış gidenler (silme, not): DITH_N gürültüsü ve çok yüksek TEX_G düz lekeyi azaltmadı, ΔE'yi bozdu; mavi gürültü varsayılan kapalı. PAL_A>0 (ton dengeli örnekleme) kulakta düz leke yaptı.
- Bir görselde sadece tek bölgeye bakarak ayar yapma: değişiklikten sonra bölge testi tablosu + en az 4 bölgenin %100 yan yana karşılaştırması şart.

## v5.5 — netleştirilmiş 4096x6144 görsel (2026-10-14)
- Girdi: kullanıcı başka uygulamayla netleştirdi (4096x6144, opak RGB, düz beyaz zemin, dizilim eski görselden farklı). Araç 1024 genişliğe göre ayarlıydı → çözünürlük çarpanı K=sw/1024 ile çekirdek boyutları, alan/mesafe eşikleri ve bölge koordinatları ölçeklendi; arka plan doldurma döngüsü vektörleştirildi (25 MP'te Python döngüsü yavaştı).
- Yeni sorun: büyütme artefaktı ince mavi kenar halesi "lacivert" sayılıp ayı kenarlarında lacivert nokta/çizgi yaptı ve ayı kenarını yedi. Çözüm: lacivert maskesine morfolojik açma (≈0.5K px'ten ince yapılar lacivert değil).
- Bölge testi koordinatları görsel dizilimine bağlıdır (1024 birimi, bu görsel için); yeni dizilimde REGIONS env ile verilmeli. Bölge testi içindeki değişken K, ölçek çarpanını eziyordu → KW olarak yeniden adlandırıldı.
- Sonuç: kulak/karın/çene/yüz %100'de gözle kontrol edildi, düz leke ve beyaz nokta yok.

## v6 — AM tram (atölye yöntemi) (2026-10-14)
- İstek: ayı desenini AM tram olarak yeniden ayarla. Yöntem (hibrit2.py, AM=1): palet k-means (siyah dahil 8 mürekkep); her piksel kağıt→en açık→…→siyah ton zincirine Lab'da izdüşürülür (u = segment + t); ardından tek bir yuvarlak-nokta ekran eşiği (kosinüs spot fonksiyonu, CDF ile alan-doğrusal) uygulanır: u'nun kesir kısmı > eşik ise sonraki (koyu) mürekkep, değilse önceki. Böylece noktalar üst üste binmez (indeks ayrımı), tek açı yeterli.
- Varsayılan: LPI=45, açı 15°, 600 PPI film (hücre 13,3 px = 0,56 mm); DMIN=0,03 (%3'ten küçük/büyük noktalar kırpılır). Env: AM=1 LPI ANG DMIN.
- Gözle kontrol: yüz, kulak, karın tramlı ve dokulu; beyaz nokta/düz leke yok. Önceki FM çıktısından detay daha kaba (beklenen).
- Atölye geri bildirimi bekleniyor: 45 lpi / 15° yeterli mi; mürekkep başına ayrı açı gerekir mi (moiré), mürekkep sayısı.

## v7 — Kız kişisi (açık tişört, 6 mürekkep, AM 45 lpi/15°, 508 PPI) — 2026-10-14
- Girdi: `kız kişisi net.png` 7000x10710, 508 PPI, suluboya illüstrasyon. Kullanıcı seçimi: açık tişört, 6 mürekkep, yalnızca figür (fırça darbeleri ve kâğıt zemin çıkar).
- Figür maskesi: elle çokgen + GrabCut (`tools/gorsel_maske_grabcut.py`, 1750 px'te), sonra sol saç/boyun/etek kenarındaki turkuaz fırça artıkları temizlendi. Kalan: sol alt etek kenarı kabaca, kullanıcıya söylendi.
- Yeni genel araç `tools/gorsel_am.py`: kâğıt beyaza normalize; her piksele en iyi (mürekkep a, mürekkep b, kâğıt) karışımı (doğrusal RGB, alan oranı); a ve b tek yuvarlak nokta ekranında art arda dolar (koyu çekirdek, açık halka) → çakışma yok. Palet: en koyu + k-means(5), tohum seçimi ağırlıklı dE ile (3,75).
- Sonuç mürekkepler: Bej(%0,55, kullanımı çok az), Sarı, Turkuaz, Karamel, Kahve, Koyu Kahve. Sönük bir 6. mürekkep: Bej atılıp 5 renge inilebilir.
- Doğrulama: azaltılmış çözünürlükte karışım simülasyonu + %100 kesit (yüz/saç, elbise); PSD Photoshop 2021'de 9094 yerine 7000x10710, 508 PPI, Multichannel açıldı.

## v7.1 — Kız kişisi, tüm görsel (zemin dahil), açık tişört, 6 mürekkep, AM 45 lpi/15°, 508 PPI — 2026-10-14
- Kullanıcı seçimi (sorulunca): açık tişört, 6 mürekkep, arka plan "hepsi" (fırça darbeleri dahil, maske yok). Kâğıt tonu (231,231,226) beyaza normalize edildi; yani baskıda kâğıt dokusu mürekkep almaz.
- `gorsel_am.py` düzeltmeleri: tam maskede beyaz noktası kenar şeridinden, renk adı otomatik (`auto_ad`), genel zıt renk kuralı, mikro parça temizliği.
- Sonuç mürekkepler: Açık Mavi, Bej, Sarı, Turkuaz, Kahve, Koyu Kahve. `kalite_kontrol.py` temiz (zıt ton payı ≤%0,05; ≤3 px parça 0).
- Gözle: %100 kesit (göz/yanak, sol fırça) temiz; Photoshop'ta 6 spot kanallı Multichannel, 508 PPI.
- Bilinen: Bej (ten) kanalı yalnızca %0,65; palet seçimi düşük kullanımlı mürekkebi cezalandırmıyor — ileride düşük kullanımlı mürekkebi artık-hata pikselleriyle yeniden seç.
- v7.1 geri bildirimi (kullanıcı, %100 Photoshop kesitleri): kahve yaprakta açık mavi, turkuaz fırçada koyu kahve, düz çiçekte leke. Ölçüldü ve nedenleri `docs/plan-bolge-safligi.md`'ye yazıldı. v7.1 bu yüzden **baskıya hazır değil**.

## v8 — Kız, bölge saflığı (`tools/bolge_am.py`), açık 6 renk + koyu fon+5 renk, 508 PPI — 2026-10-14
- Kullanıcı (soruldu): ikisi de; 6 mürekkep; zemin hepsi. Koyu tişörtte kâğıt beyazı basılmaz; fon 6 kafanın içinde (fon + 5 renk).
- Plan (`docs/plan-bolge-safligi.md`) uygulandı: çift bilateral yumuşatma → ton aileleri (72°, 208°) → piksel yalnız kendi ailesinin mürekkebiyle karışır; en koyu mürekkep başka ailede yalnız çizgi/koyu dolu şekil maskesinde; düz bölgede indeks medyan + kaplama yumuşatma; palet aile başına açgözlü (aile 0: 3, aile 1: 2 + en koyu).
- Ölçüm (yeni kontrol, kroma ≥5, ton farkı >90°): v7.1 → v8: Açık Mavi yanlış alanda %2,19 → %0,07; Koyu Kahve açık/orta yanlış alanda %11,87 → %1,73 (kalan: turkuaz şekillerin konturu). Bej kullanımı %0,65 → %8,3.
- Hata bulunup düzeltildi: (1) çiçeğin içindeki koyu dolu şekiller yalnız kontur çıktı → çizgi maskesine "koyu (L<45, C<25) dolu şekil" eklendi; (2) koyu tişörtte kâğıt dokusu yüzünden tüm zemine beyaz fon noktası → kâğıtta fon 0, opaklık rampası (dE-5)/5; (3) figür maskesine sızan kâğıt (sağ alt) beyaz dikdörtgen yaptı → maske dışına bağlı kâğıt bileşenleri figür beyazı sayılmaz.
- Gözle: üç şikâyet yeri (kahve yaprak, sol fırça, saç çiçeği) %100 simülasyonda temiz; koyu tişört tam önizleme kontrol edildi.
- Bilinen: koyu tişörtte elbise sağ alt kenarı (kaynakta elbise beyazı kâğıtla birleşik) tişört rengi kaldı; çiçek konturu kaynakta koyu turkuaz, çıktıda koyu kahve (turkuaz ailesine koyu ton ayrılmadı).
