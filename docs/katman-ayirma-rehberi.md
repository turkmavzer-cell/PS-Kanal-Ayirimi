# Katman Ayırma Rehberi ve Standart Operasyon Protokolü (SOP)

Bu rehber, Photoshop ve Python ile herhangi bir görseli (özellikle zırh, illüstrasyon, tekstil deseni) **2 ile 10 arasında bağımsız, kusursuz ve profesyonel nesne katmanına (layers)** ayırma standardıdır.

---

## 1. Temel İlke ve Zihniyet Ayrımı

* **Renk Ayrımı (Color Separation):** Piksellerin mürekkep rengine göre ayrılmasıdır (Spot kanal / emprime filmi).
* **Nesne Katmanı Ayrımı (Structural Layer Separation):** Tasarımın **fiziksel, anatomik ve tasarımsal parçalarının** (ör. toka, kemer, kafatası, omuzluk, karın plakaları, göz ışığı) bağımsız katmanlar haline getirilmesidir.

> **Altın Kural:** Bir katman, başka bir katmanı delik deşik eden rastgele bir yapboz parçası değildir. Her katman tek başına açıldığında anatomik ve estetik olarak tam, kenarları pürüzsüz bir nesne olmalıdır.

---

## 2. Kesinlikle Yasaklanan Hatalar (Kara Liste)

1. **ASLA Bounding Box / Dikdörtgen Kutu Kesimi Yapma:**
   - Nesneleri ayırmak için koordinat kutuları (`mask[y0:y1, x0:x1]`) kullanılmaz. Bu durum komşu katmanlarda dikdörtgen delikler ve anlamsız bloklar bırakır.
2. **ASLA Düz Çizgili Poligon Kesimi Yapma:**
   - Kavisli ve organik zırh plakalarının üzerinden jiletle düz çizgi çekilmez. Ayrım daima tasarımın doğal dikiş/birleşim çizgilerini (`seam lines`) takip eder.
3. **ASLA Nesnenin İçini Delik Bırakma:**
   - Göz ışığı veya ağız boşluğu başka katmana gidecek diye kafatasının ortası yırtık delik haline getirilmez. Kafatası tam çizilir; ışık onun üstüne binen ayrı bir katmandır.
4. **ASLA Sert 1-Bit Jilet Kenar Bırakma:**
   - Kenarlarda 1-1.5 piksellik alt-piksel yumuşatma (`sub-pixel alpha matting`) uygulanır.

---

## 3. Katman Sayısı Belirleme Standardı (2 - 10 Katman)

* **2 – 3 Katman:** Zemin + Ana Obje (+ Tipografi veya Işık).
* **4 – 6 Katman:** Zemin + Arka Gövde + Ana Karakter + Aksesuarlar + Efektler.
* **7 – 10 Katman (Zırh / İllüstrasyon / İleri Düzey):**
  1. `Zemin`: Arka plan (#000000 veya şeffaf).
  2. `Gogus_Zirhi_ve_Boyunluk`: Ana taşıyıcı göğüs gövdesi ve boyunluk.
  3. `Karin_Zirhi_Plakalari`: Mafsallı karın plakaları (doğal kavis çizgisiyle).
  4. `Kemer`: Sağ ve sol kemer kayışı, bronz raylar ve yıldız perçinler.
  5. `Kemer_Tokasi`: Altıgen toka çerçevesi, iç kabartması ve perçinleri.
  6. `Omuzluklar`: Sağ ve sol ayrık omuz korumaları.
  7. `Zincir_ve_Yildizlar`: Sarkan zincirler ve göğüs montaj yıldızları.
  8. `Iskelet_Kafalari`: Üstteki boynuzlu kafatası ve sarkan amblem kafatası.
  9. `Goz_Isiklari`: Kor kırmızı göz alevi ve ışıma efekti.

---

## 4. Z-Index (Derinlik) Sıralaması (Aşağıdan Yukarıya)

```
09. Goz_Isiklari (En Üstte)
08. Iskelet_Kafalari
07. Zincir_ve_Yildizlar
06. Omuzluklar
05. Kemer_Tokasi
04. Kemer
03. Karin_Zirhi_Plakalari
02. Gogus_Zirhi_ve_Boyunluk
01. Zemin (En Altta)
```

---

## 5. Otomatik Doğrulama ve Kalite Kontrol

PSD kaydedilmeden önce script şu kontrolleri doğrular:
1. Her katmanın tekil PNG çıktısında dikdörtgen kesik veya anlamsız kopuk parça olmamalıdır.
2. Tüm katmanlar üst üste bindiğinde orijinal görselle fark: `Error <= 0.05` olmalıdır.
3. Katman adlarında Türkçe karakter kullanılmaz (`Iskelet_Kafalari`, `Omuzluklar`, `Kemer_Tokasi`).
