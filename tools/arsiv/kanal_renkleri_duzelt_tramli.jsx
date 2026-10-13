#target photoshop
// Aktif Multichannel belgedeki kanallari Spot Color yapar, mürekkep renklerini atar,
// sadece TRAM kanallarini gorunur birakir (YEDEK ve beyaz fon gizli).
app.displayDialogs = DialogModes.NO;
var doc = app.activeDocument;
// sira: TRAM beyaz, YEDEK beyaz, TRAM/YEDEK Siyah, Mavi 1, Mavi 2, Kirmizi
var rgb = [
  [255,255,255],[255,255,255],
  [24,25,47],[24,25,47],
  [9,43,121],[9,43,121],
  [59,113,158],[59,113,158],
  [231,47,15],[231,47,15]
];
var log = [];
for (var i = 0; i < doc.channels.length && i < rgb.length; i++) {
  var ch = doc.channels[i];
  var note = ch.name + ": ";
  if (i > 0) {
    try { ch.kind = ChannelType.SPOTCOLOR; note += "spot "; } catch (e) { note += "kind-HATA(" + e.message + ") "; }
  }
  try {
    var c = new SolidColor();
    c.rgb.red = rgb[i][0]; c.rgb.green = rgb[i][1]; c.rgb.blue = rgb[i][2];
    ch.color = c; note += "renk ";
  } catch (e) { note += "renk-HATA(" + e.message + ") "; }
  try { ch.opacity = 0; } catch (e) {}
  log.push(note);
}
// gorunurluk: sadece mürekkep TRAM kanallari
for (var j = 0; j < doc.channels.length; j++) {
  var isTram = doc.channels[j].name.indexOf("TRAM") == 0;
  var isWhite = doc.channels[j].name.indexOf("BEYAZ") >= 0;
  try { doc.channels[j].visible = (isTram && !isWhite); } catch (e) {}
}
alert(log.join("\n"));
