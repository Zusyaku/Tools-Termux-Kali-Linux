import os
import sys
import time
cy = '\033[92m'
cyy = '\033[96m'
lg = '\033[92m'
w  = '\033[97m'
lr = '\033[91m'
yl = '\033[93m'
h = '\033[95m'
x  = '\033[0m'
os.system ("clear")
print " "
print " "
print (cyy+" TUNGGU BENTAR COEG !*")
os.system ("sleep 5")
os.system ("clear")

print (h+"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~     PEMBUAT SCRIPT DEFACE      ~~
~~    AUTHOR : RISKI DARMAWAN     ~~
--   DIBUAT : 27 JANUARI 2019     ~~
~~   WHATSAPP : 085836465872      ~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
os.system ("sleep 2")
print (cyy+" ")
title = raw_input("Masukkan judul : ")
nick = raw_input("Hacked by : ")
team = raw_input("Nama team : ")
img = raw_input("Link gambar : ")
print
print (cyy+"~~ Dibawah ini pesan halaman awal ya ~~")
pesan = raw_input("Pesan 1 : ")
pesan2 = raw_input("Pesan 2 : ")
pesan3 = raw_input("Pesan 3 : ")
pesan4 = raw_input("Pesan 4 : ")
print
print (cyy+"~~ Yang ini pesan untuk adminnya ~~")
kata = raw_input("Kata 1 : ")
kata2 = raw_input("Kata 2 : ")
kata3 = raw_input("Kata 3 : ")
greetz = raw_input("Thanks to : ")
print
print (cyy+"~~ Nama file ( contoh: index.html ) ~~")
namafile = raw_input("Nama file : ")
m1 = """<!DOCTYPE html>
<html>
<head>
    <title>"""
m2 = title
m3 = """</title>
    <meta charset="UTF-8">
    <meta name="Author" content="Seorang Tersakiti<3"/>
    <meta name="copyright" content="Penjelajah <3"/>
    <meta name="description" content="Website Owned by Penjelajah"/>
    <link href='http://fonts.googleapis.com/css?family=Iceland:400,700' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Iceland:400,700' rel='stylesheet' type='text/css'>
    <meta property="og:image" content="">
        <style type="text/css">
            body {
                overflow:hidden;
                background-image:url('https://s22.postimg.org/lq5lty0gx/yh8t9em_VAe_Vw3kh1.jpg');
                background-color: #000000;
                background-repeat:no-repeat;
                background-size: 100% ;
                background-position:top center;
                margin: 0px;
                cursor:none;
                font-family: Iceland, sans-serif;
            }
            a{
                text-decoration: none;
            }
            h1{
            font-family: Iceland, sans-serif;
            font-size:90px;
            color:#fff;
            margin:0px 0px 0px;
            
            }
            h2{
            font-family: Iceland, sans-serif;
            font-size:40px;
            color:#000;
            margin: 0px;
            text-shadow: 0 0 3px #fff;
            
            }
            p{
            color:#000;
            font-size:25px;
            margin: 0px;
            text-shadow: 0 0 3px #fff;
            }
            .fot{

font-family: Iceland, sans-serif;
            font-size:14px;
            color:#fff;
            margin: 0px;
            text-shadow: 0 0 3px #000, 0px 0px 5px #000;
            }
             h1{
            color:#000;
            text-shadow: 0 0 5px #fff;
        }
        .greets{
    font-family: Arial, sans-serif;
    line-height: 24px;
    font-size: 11px;
    width: 50%;
    background: #000;
    opacity: 0.9;
    text-transform: uppercase;
    z-index: 9999;
    border-radius:10px;
    -moz-box-shadow: 1px 0px 2px #000;
    -webkit-box-shadow: 1px 0px 2px #000;
    box-shadow: 1px 0px 2px #000;
}
        </style>
    </head> 
    <div id="I301_html">
<script type="text/javascript" src="http://code.jquery.com/jquery.min.js"></script>
<script type="text/javascript">setTimeout("$('#loading').fadeOut(5000);", 10000);  </script>
<style type="text/css">#loading{position:fixed;top:0;left:0;padding-top:0px;background-color:#000;width:100%;height:100%;color:black;z-index:9000;overflow:hidden;}</style>
<div id="loading">
<body onload="document.f.p.focus()" topmargin="0" leftmargin="0" bgcolor="#000000" marginheight="0" marginwidth="0">
<table border="0" cellpadding="2" cellspacing="0" width="100%">
<tbody><tr> 
</tr>
    
<tr>
</tr>
</tbody></table> 
<font id="ResponseData" color="#ff99cc">
<pre><script type="text/javascript">
TypingText = function(element, interval, cursor, finishedCallback) {
  if((typeof document.getElementById == "undefined") || (typeof element.innerHTML == "undefined")) {
    this.running = true;    // Never run.
    return;
  }
  this.element = element;
  this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });
  this.interval = (typeof interval == "undefined" ? 100 : interval);
  this.origText = this.element.innerHTML;
  this.unparsedOrigText = this.origText;
  this.cursor = (cursor ? cursor : "");
  this.currentText = "";
  this.currentChar =0;
  this.element.typingText = this;
  if(this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex++;
  TypingText.all.push(this);
  this.running = false;
  this.inTag = false;
  this.tagBuffer = "";
  this.inHTMLEntity = false;
  this.HTMLEntityBuffer = "";
}
TypingText.all = new Array();
TypingText.currentIndex = 0;
TypingText.runAll = function() {
  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();
}
TypingText.prototype.run = function() {
  if(this.running) return;
  if(typeof this.origText == "undefined") {
    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);    // We haven't finished loading yet.  Have patience.
    return;
  }
  if(this.currentText == "") this.element.innerHTML = "";
//  this.origText = this.origText.replace(/<([^<])*>/, "");     // Strip HTML from text.
  if(this.currentChar < this.origText.length) {
    if(this.origText.charAt(this.currentChar) == "<" && !this.inTag) {
      this.tagBuffer = "<";
      this.inTag = true;
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == ">" && this.inTag) {
      this.tagBuffer += ">";
      this.inTag = false;
      this.currentText += this.tagBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inTag) {
      this.tagBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == "&" && !this.inHTMLEntity) {
      this.HTMLEntityBuffer = "&";
      this.inHTMLEntity = true;
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == ";" && this.inHTMLEntity) {
      this.HTMLEntityBuffer += ";";
      this.inHTMLEntity = false;
      this.currentText += this.HTMLEntityBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inHTMLEntity) {
      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else {
      this.currentText += this.origText.charAt(this.currentChar);
    }
    this.element.innerHTML = this.currentText;
    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) : "");
    this.currentChar++;
    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);
  } else {
    this.currentText = "";
    this.currentChar = 0;
        this.running = false;
        this.finishedCallback();
  }
}
</script>
<script>
function disableselect(e){return false}
function reEnable(){return true}
//if IE4+
document.onselectstart=new Function ("return false")
//if NS6
if (window.sidebar){
document.onmousedown=disableselect
document.onclick=reEnable
}
</script>
<script>
var message="";
function clickIE()
{if (document.all)
{(message);return false;}}
function clickNS(e) {
if
(document.layers||(document.getElementById&&!document.all))
{
if (e.which==2||e.which==3) {(message);return false;}}}
if (document.layers)
{document.captureEvents(Event.MOUSEDOWN);document.  onmousedown=clickNS;}
else
{document.onmouseup=clickNS;document.oncontextmenu  =clickIE;}
document.oncontextmenu=new Function("return false")
</script>
<table style=" background-repeat: no-repeat;"  align="right" border="0" width="100%" >
<br>
<tbody><tr>
<td  valign="top"><p id="hack" >
<br />
<br>
<font color="Green">     <b>"""
m4 = pesan
m5 = """</font> <br>
<font color="Green">     <b>"""
m6 = pesan2
m7 = """</font><br>
<font color="Green">     <b>"""
m8 = pesan3
m9 = """</font><br>
<font color="Green">     <b>"""
m10 = pesan4
m11 = """</font>
</p></tr>
</tbody></table>                 </div> 
<br>
<script type="text/javascript">
new TypingText(document.getElementById("hack"), 50, function(i){ var ar = new Array("_",""); return " " + ar[i.length % ar.length]; });
TypingText.runAll();
</script>
    <style> 
      td
      {
        background-color: #000000;
        font-family: Courier New;
        font-size:20px;
        color:#000000;
        border-color: #000000;
        border-width:1pt;
        border-style:solid;
        border-collapse:collapse;
        padding:0pt 3pt;
        vertical-align:top;
      }
      table
      {
        border-color: #88aace;
        border-width:0pt 1pt;
        border-style:dash;
      }
      A:Link, A:Visited
      {
        color: #88aace;
      }
      A.no:Link, A.no:Visited
      {
color: #88aace;
        text-decoration: none;
      }
      A:Hover, A:Visited:Hover , A.no:Hover, A.no:Visited:Hover
      {
        color: #88aace;
        background-color:#2e2e2e;
        text-decoration:
        overline underline;
      }
      .style1
      {
        color: #88aace
      }
      .style2
      {
        color: 1f1f1f
      }
      body
      {
        color:white;
         
        background-position:right;
        background-attachment:fixed;
        </div>
      }
    </style>
        
</div>
</div>
<body oncontextmenu="return false" onkeydown="return false">
<center>
<h2 class="glow">"""
m12 = team
m13 = """</h2>
<img src="""
t1 = img
t2 = """ width="250"height="250">
<h2 class="glow2" >.::Hacked By::.<br> <span style="color:#000;font-family:Iceland;text-shadow:SkyBlue 0px 0px 10px">./</span><span style="color:#000;font-family:Iceland;text-shadow:red 0px 0px 10px">"""
t3 = nick
t4 = """</span></b></h2>
<p><b><font color="blue"> """
t5 = kata
t6 = """.</font><span style="font-family:Iceland;color:red;text-shadow:#000 0px 0px 3px"> """
t7 = kata2
t8 = """.</span> <font color="blue"> """
tt = kata3
t9 = """</font><font style="color:red;text-shadow:#000 0px 
0px 3px"></font><br>#*#*#*#
            </p>
        </span>
            <div style="font-size:10px;color:gold;text-shadow:grey 0px 0px 3px">
        <span style="font-family:Iceland;font-weight:bold;color:#ffffff"><p>~"""
t10 = team
t11 = """~</p></span>
    </div>
<div class="greets">
<table align=center border="0">
<tr>
<td width=100% id=CROOTZ>
<marquee behavior="scroll" direction="left" scrollamount="4" scrolldelay="55" width="100%">
<font size="5px" style="font-family: Iceland, sans-serif;color:black;text-shadow: 0 0 3px red, 0px 0px 5px red" >
<b>-=|"""
t12 = greetz
t13 = """=-</font>
</marquee>
</td>
</table></div> 
<div class="fot">
DUNIA HACKER INDONESIA [+] ANONYMOUS INDONESIA [+]"""
l1 = team
l2 = """</div>
</center>
</body>
<object data="http://flash-mp3-player.net/medias/player_mp3.swf" width="0" height="0" type="application/x-shockwave-flash"><param value="#ffffff" name="bgcolor"><param value="mp3=http://zizka.free.fr/_muisc/04-kanye_west-amazing_ft._young_jeezy-(HHKingz.net).mp3&loop=1&autoplay=1&volume=125" name="FlashVars"></object>
</body>
</html>"""
file = open(namafile, "w")
file.write(m1)
file.write(m2)
file.write(m3)
file.write(m4)
file.write(m5)
file.write(m6)
file.write(m7)
file.write(m8)
file.write(m9)
file.write(m10)
file.write(m11)
file.write(m12)
file.write(m13)
file.write(t1)
file.write(t2)
file.write(t3)
file.write(t4)
file.write(t5)
file.write(t6)
file.write(t7)
file.write(t8)
file.write(tt)
file.write(t9)
file.write(t10)
file.write(t11)
file.write(t12)
file.write(t13)
file.write(l1)
file.write(l2)
os.system ("clear")
print
print "~~ SCRIPT BERHASIL DIBUAT ~~"
print "~~ LIHAT SCRIPT ANDA BERNAMA", namafile
print "~~ TERIMA KASIH SUDAH MEMAKAI TOOL SAYA ~~"
print
print " BYE... BYE..."

file.close()
