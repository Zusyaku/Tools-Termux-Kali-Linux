### README


Password generator through a simple wordlist.
You can use this tool to create a **new wordlist** with **numbers** and **special characters**.

### FORMAT TYPE
<pre>
wns -> Word + Number + Special Char -> password0!
wsn -> Word + Special Char + Number -> password!0
nws -> Number + Word + Special Char -> 0password!
nsw -> Number + Special Char + Word -> 0!password
snw -> Special Char + Number + Word -> !0password
swn -> Special Char + Word + Number -> !password0
</pre>

### USAGE

You must to configure the parameters of the file <a href="https://github.com/guelfoweb/passgen/blob/master/passgen.cfg">passgen.cfg</a><br />
Start passgen with:
<pre>
./passgen.sh
</pre>
or
<pre>
./passgen.sh -i [file input] -o [file output]
</pre>
<pre>
[+] Ready for 367920 passwords
[+] Password format: wns
[+] Password Type: Adamo0!
[+] File output: output.txt

Press [Enter] key to start or [Ctrl+C] key to stop...

Started: gio 14 mar 2013, 20.14.19, CET
Stopped: gio 14 mar 2013, 20.14.52, CET
</pre>
It took a few seconds to generate 367.920 password. Now you can verify the file with the password you just created.
<pre>
cat output.txt
</pre>
<pre>
Adamo1970!
Adamo1970@
Adamo1970$
Adamo1970%
::
Adamo2013!
Adamo2013@
Adamo2013$
Adamo2013%
::
Zuckerberg1970!
Zuckerberg1970@
Zuckerberg1970$
Zuckerberg1970%
::
Zuckerberg2013!
Zuckerberg2013@
Zuckerberg2013$
Zuckerberg2013%
</pre>

### MD5 WORDLIST

<pre>
cat output.txt | while read word; do echo $word | md5sum | sed "s/  -/:$word/"; done
</pre>
<pre>
c60c5d16ea78a5bffdb6de806a1691a7:Adamo1970!
c3f756875a106300873961571a8f4810:Adamo1970@
13f296e5f7427bc9d9f564fd66cba93b:Adamo1970$
00bc8d1a13859e8d5c0141555f99867e:Adamo1970.
::
</pre>

### OTHER

This script is currently maintained by Gianni 'guelfoweb' Amato, who can be contacted at guelfoweb@gmail.com. Suggestions and criticism are welcome.

Enjoy!
