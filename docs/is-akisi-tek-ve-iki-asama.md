# İş akışı: tek aşamalı ve iki aşamalı yöntem

Her yeni işte, başlamadan önce kullanıcıya **"Tek aşamalı mı, iki aşamalı mı yapalım?"** diye sorulur (tişört rengi, renk sayısı ve zemin sorularıyla birlikte). Aşağıdaki açıklama, projeyi ilk kez kullanan biri de seçim yapabilsin diye yazıldı.

---

## Tek aşamalı yöntem

**Ne olur:** Görsel verilir, program renkleri kendisi seçer, tramlar ve doğrudan **film kanallarına ayırır**. Sonuç: her mürekkep için bir film (1-bit PNG, siyah = mürekkep, 508 PPI) ve Photoshop'ta açılan çok kanallı (Multichannel, spot renk) PSD.

**Adımlar:**
1. Görsel analizi (`tools/analiz.py`), sorular (tişört rengi, renk sayısı, zemin).
2. Ayırma (`tools/bolge_am.py`, varsayılan `ASAMA=tek`): açık ve/veya koyu tişört seti.
3. Otomatik kalite kontrol (`tools/kalite_kontrol.py`) + %100 kesitle gözle kontrol.
4. PSD: klasördeki `psd_olustur_tek_adim.jsx` Photoshop'ta File > Scripts > Browse ile çalıştırılır.

**Ne zaman:** Hızlı sonuç istenirse, renklerin program tarafından seçilmesi yeterliyse, düzeltme gerekirse sonradan yeniden çalıştırılabilecekse.

**Artısı / eksisi:** Hızlı. Ama bir renk yanlış seçilirse (ör. kahve yaprakta mavi, ten turuncu) düzeltmek için programın ayarlarını değiştirip baştan çalıştırmak gerekir.

---

## İki aşamalı yöntem

**Ne olur:** Program önce **kanallara ayırmadan**, baskıdaki gibi tramlı (pikselli) bir **önizleme görüntüsü** üretir. Bu görüntüde her piksel ya tişört rengidir ya da mürekkeplerden biridir (ara ton yoktur). Kullanıcı bu görüntüde istediği renkleri değiştirir, onay verir; program **onaylanan görüntüyü birebir** filmlere ayırır.

### 1. aşama — Önizleme (program yapar)
- Komut: `ASAMA=onizleme python3 tools/bolge_am.py girdi.png cikti N_acik [N_koyu_renk]`
- Çıktı:
  - `Onizleme_Acik_Tisort.png` (beyaz zemin) ve/veya `Onizleme_Koyu_Tisort.png` (tişört renginde zemin; beyaz = yalnız fon).
  - Görüntüler **Indexed Color** (renk tablolu) PNG, 508 PPI; renk sayısı = mürekkep sayısı (+ tişört, koyuda + fon beyazı).
  - `onizleme_palet.json`: hangi renk hangi mürekkep, tişört rengi.
- Bu aşamada film üretilmez.

### Kullanıcının düzenlemesi (Photoshop)
İki tür değişiklik yapılabilir:
1. **Bir mürekkebin rengini her yerde değiştirmek** (ör. sarıyı şeftaliye çevirmek): Image > Mode > Color Table; ilgili renge tıklayıp yeni rengi seç. O mürekkep görüntünün her yerinde değişir.
2. **Bir bölgeyi başka mürekkebe taşımak** (ör. kahve yapraktaki mavileri kahveye çevirmek): Bölgeyi Lasso ile seç (Feather 0, Anti-alias kapalı), içinde Magic Wand (Tolerance 0, Anti-alias kapalı, Contiguous kapalı) ile yanlış rengi seç, yeni renkle doldur (Edit > Fill) ya da Pencil aracıyla boya.

Kurallar:
- **Kenar yumuşatma kullanılmaz** (Brush yerine Pencil; seçimlerde Anti-alias ve Feather kapalı). Yoksa ara renk pikselleri oluşur; 2. aşama bunları en yakın renge atar ve raporlar.
- **PNG olarak kaydedilir** (JPEG renkleri bozar).
- **Boyut ve çözünürlük değiştirilmez** (508 PPI).
- Yeni bir renk eklenirse o **yeni bir film (kafa)** olur; kafa sayısını aşarsa program uyarır.
- Düzenleme bitince kullanıcı **onay** verir.

### 2. aşama — Kanallara ayırma (program yapar, onaydan sonra)
- Komut: `python3 tools/onizlemeden_ayir.py duzenlenmis.png cikti acik|koyu onizleme_palet.json`
- Her farklı renk bir film olur; tişört rengi = mürekkep yok.
- Koyu tişörtte **beyaz fon otomatik** çıkarılır: tişört rengi olmayan her yer, en koyu mürekkebin altı hariç, dışa bakan kenarlarda choke.
- İnce çapak ve mikro parçalar temizlenir; çok az pikselli (artık) renkler en yakın renge atanır ve raporlanır.
- Sonra kalite kontrol ve PSD (tek aşamalıdaki 3. ve 4. adım).

**Ne zaman:** Renk seçimine kullanıcı karar vermek isterse; karmaşık görsellerde (ten, iç içe renkli desen) program renkleri yanlış yere koyabiliyorsa; atölyeye göndermeden önce son kontrol istenirse.

**Artısı / eksisi:** Son karar kullanıcıda, filmler onaylanan görüntünün birebir aynısı. Ama kullanıcının Photoshop'ta zaman ayırması gerekir ve görüntü büyüktür (ör. 7000×10710 px).

---

## Kısa karşılaştırma

| | Tek aşamalı | İki aşamalı |
|---|---|---|
| Renkleri kim belirler | Program | Program önerir, kullanıcı düzeltir ve onaylar |
| Kullanıcı emeği | Az | Photoshop'ta düzenleme |
| Yanlış renk düzeltme | Programı yeniden çalıştır | Önizlemede doğrudan boya |
| Film = onaylanan görüntü | Önizleme sonradan bakılır | Evet, birebir |
| Araçlar | `bolge_am.py` | `bolge_am.py` (ASAMA=onizleme) + `onizlemeden_ayir.py` |
