# Perplexity araştırma promptu

Bu prompt Perplexity'ye verildi; sonuç `serigrafi-renk-ayrimi-raporu.md` dosyasındadır. Yeni araştırma gerekirse bu prompt güncellenerek yeniden kullanılır.

```
Türkiye'deki tekstil baskı sektöründe (emprime / serigrafi / ipek baskı, gerekirse dijital baskı ile karşılaştırarak) RENK AYRIMI (color separation) çalışma mantığını araştır. Hem Türkçe hem İngilizce kaynaklara bak (örnek arama terimleri: emprime renk ayrımı, serigrafi film çıkarma, tramlı/tramsız baskı, spot color separation, halftone vs flat color screen printing, simulated process, index color separation, underbase). Kaynak olarak üretici/atölye rehberleri, serigrafi malzeme firmalarının teknik dokümanları (Ryonet, Wilflex, Union Ink, Murakami, Saati vb.), sektör forumları ve eğitim videolarının metinlerini tercih et. Her önemli iddiayı kaynağıyla ver; kaynağı olmayan bilgiyi "kaynaksız/yorum" diye işaretle.

BAĞLAM (benim durumum):
Tek bir tişört baskı tasarımının renk ayrımını yaptım. Tasarım düz renkli bir illüstrasyon: yaklaşık 4-5 belirgin renk (lacivert-siyah, iki ton mavi, kırmızı-turuncu), net konturlu yazılar, süslemeli mandala deseni, kenarları yumuşatılmış (anti-aliased) bir JPEG/PNG kaynak (yaklaşık 300 PPI). Ben şu yöntemi uyguladım: görselden otomatik olarak birkaç baskı rengi çıkardım, her renk için 508 PPI'da, 45 lpi civarında yarım ton (tram) noktalı kanal ürettim, ayrıca tramsız bir yedek kanal ve beyaz zemin (underbase) kanalı oluşturdum. Konunun bilen bir kişisi dosyayı görünce bunun iyi bir iş olmadığını, bu tür bir tasarımın TRAMSIZ (düz renk) ayrılması gerektiğini söyledi. Neden öyle olduğunu ve doğru yöntemin ne olduğunu anlamak istiyorum.

CEVAPLANMASI GEREKEN SORULAR:
1. Temel kavramlar: tramlı/tramsız, spot, tramlı spot, simüle proses, CMYK proses, index, stokastik tram farkları; Türkiye'deki atölye jargonu (film, kalıp, ipek, ışıklama, tram, lap/dolgu, kontur).
2. Hangi görsel türünde hangi yöntem (düz renkli illüstrasyon/logo/tipografi; süslemeli mandala; fotoğraf; degrade; açık ve koyu tekstil).
3. Tramın sorun çıkardığı durumlar: moiré, nokta büyümesi, elek-lpi ilişkisi (sayısal), küçük noktaların elekte kalmaması, ince detay/kontur kaybı, lekeli görünüm, renk sayısı ve maliyet.
4. Kenar yumuşatma ve renk sayısı: ara tonlar, renk indirgeme yöntemleri, kaç renk, ne zaman vektöre çevirme şart.
5. İyi çalışan iş akışı (Photoshop ve Illustrator ayrı ayrı), ayrım yazılımları/RIP'ler.
6. Beyaz zemin (underbase) ve koyu tekstil: ne zaman gerekir, tramlı mı tramsız mı, choke, yaygın hatalar.
7. Karar tablosu (görsel türü → yöntem → renk sayısı → dikkat edilecek hata) ve benim yöntemimin dürüst değerlendirmesi.
8. Karşı görüşler ve uzmanlar arasında anlaşmazlık olan noktalar; belirsizleri "belirsiz" işaretle.

ÇIKTI BİÇİMİ: Türkçe, başlıklı; başta 10 maddelik özet; her soru için ayrı bölüm; sonda karar tablosu ve atölyeye sorulabilecek 10 somut soru; tüm kaynaklar link ile.
```
