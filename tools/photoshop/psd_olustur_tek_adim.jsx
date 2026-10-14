#target photoshop
// Betikle ayni klasordeki kanallar_hibrit.json ve Acik_Tisort/ filmlerini tek bir Multichannel belgede kanal olarak toplar.
// Ardindan film_renk_ata.jsx calistirilir (Spot Color + mürekkep renkleri).
app.displayDialogs = DialogModes.NO;
var root = new File($.fileName).parent;
var jf = new File(root.fsName + "/kanallar_hibrit.json"); jf.encoding = "UTF-8"; jf.open("r");
var meta = eval("(" + jf.read() + ")"); jf.close();
var list = meta.sets.Acik_Tisort;
function openGray(name) {
  var d = app.open(new File(root.fsName + "/Acik_Tisort/" + name));
  if (d.mode == DocumentMode.BITMAP) d.changeMode(ChangeMode.GRAYSCALE);
  return d;
}
var target = openGray(list[0][1]);
target.changeMode(ChangeMode.MULTICHANNEL);
target.channels[0].name = list[0][0];
for (var i = 1; i < list.length; i++) {
  var src = openGray(list[i][1]);
  src.selection.selectAll(); src.selection.copy();
  src.close(SaveOptions.DONOTSAVECHANGES);
  app.activeDocument = target;
  var ch = target.channels.add();
  ch.name = list[i][0];
  target.activeChannels = [ch];
  target.paste();
  target.selection.deselect();
}

var doc = app.activeDocument;
for (var i = 0; i < doc.channels.length && i < list.length; i++) {
  var ch = doc.channels[i];
  try { ch.kind = ChannelType.SPOTCOLOR; } catch (e) {}
  try { var c = new SolidColor(); c.rgb.red = list[i][2][0]; c.rgb.green = list[i][2][1]; c.rgb.blue = list[i][2][2]; ch.color = c; } catch (e) {}
  try { ch.opacity = 100; } catch (e) {}
}
for (var j = 0; j < doc.channels.length; j++) { try { doc.channels[j].visible = true; } catch (e) {} }
var out = new File(root.fsName + "/Ayicik_v53_Kanallar.psd");
var o = new PhotoshopSaveOptions(); o.spotColors = true; o.alphaChannels = true; o.layers = false;
doc.saveAs(out, o, true, Extension.LOWERCASE);
