#target photoshop
// Emprime ayrimi: klasordeki 1-bit PNG kanallarini tek bir Multichannel belgede toplar.
app.displayDialogs = DialogModes.NO;
var base = new File($.fileName).parent.fsName;
var list = [
  ["TRAM | BEYAZ FON - 0.15 mm daraltılmış", "TRAM_00_BEYAZ_FON.png"],
  ["YEDEK | BEYAZ FON - 0.15 mm daraltılmış", "YEDEK_00_BEYAZ_FON.png"],
  ["TRAM | Siyah", "TRAM_01_Siyah.png"],
  ["YEDEK | Siyah", "YEDEK_01_Siyah.png"],
  ["TRAM | Mavi 1", "TRAM_02_Mavi_1.png"],
  ["YEDEK | Mavi 1", "YEDEK_02_Mavi_1.png"],
  ["TRAM | Mavi 2", "TRAM_03_Mavi_2.png"],
  ["YEDEK | Mavi 2", "YEDEK_03_Mavi_2.png"],
  ["TRAM | Kırmızı", "TRAM_04_Kirmizi.png"],
  ["YEDEK | Kırmızı", "YEDEK_04_Kirmizi.png"]
];

function openGray(name) {
  var d = app.open(new File(base + "/" + name));
  if (d.mode == DocumentMode.BITMAP) d.changeMode(ChangeMode.GRAYSCALE);
  return d;
}

var target = openGray(list[0][1]);
target.changeMode(ChangeMode.MULTICHANNEL);
target.channels[0].name = list[0][0];

for (var i = 1; i < list.length; i++) {
  var src = openGray(list[i][1]);
  src.selection.selectAll();
  src.selection.copy();
  src.close(SaveOptions.DONOTSAVECHANGES);

  app.activeDocument = target;
  var ch = target.channels.add();
  ch.name = list[i][0];
  target.activeChannels = [ch];
  target.paste();
  target.selection.deselect();
}
target.activeChannels = [target.channels[0]];
alert("Bitti: " + list.length + " kanal oluşturuldu.");
