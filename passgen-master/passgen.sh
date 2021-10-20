#!/bin/bash

# Password generator with wordlist 
name="Passgen.sh"
ver="0.2.1"
author="Gianni 'guelfoweb' Amato"

#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# guelfoweb@gmail.com wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Gianni 'guelfoweb' Amato
# ----------------------------------------------------------------------------
#

CONFIG="passgen.cfg"

wordlist=`grep "^wordlist=" $CONFIG | cut -d"=" -f2`
newwordlist=`grep "^newwordlist=" $CONFIG | cut -d"=" -f2`

usage(){
	echo "$name v.$ver by $author"
	echo "https://github.com/guelfoweb/passgen/"
	echo
	echo "Password generator through a simple wordlist. You can use this tool to create a new wordlist with numbers and special characters."
	echo
	echo "You must to configure the parameters of the file [passgen.cfg]"
	echo
	echo "USAGE"
	echo "   $0"
	echo "   $0 -i <file input> -o <file output> "
	echo
	echo "OPTION"
	echo "   -h   this help"
	echo "   -i   file input"
	echo "   -o   file output"
	exit
}

ARGC=$#
if [ "$ARGC" -eq 1 ] || [ "$ARGC" -gt 4 ]; then
	usage
fi
if [ "$ARGC" -eq 2 ] && [ "$1" == "-i" ]; then
	wordlist="$2"
fi
if [ "$ARGC" -eq 2 ] && [ "$1" == "-o" ]; then
	newwordlist="$2"
fi
if [ "$ARGC" -eq 4 ]  && [ "$1" == "-i" ] && [ "$3" == "-o" ]; then
	wordlist="$2"
	newwordlist="$4"
fi
if [ "$ARGC" -eq 4 ]  && [ "$1" == "-o" ] && [ "$3" == "-i" ]; then
	wordlist="$4"
	newwordlist="$2"
fi
if [ ! -f "$wordlist" ]; then
	echo "File not exist: $wordlist"
	exit
fi

chars=`grep "^chars=" $CONFIG | cut -d"=" -f2`
u=`grep "^u=" $CONFIG | cut -d"=" -f2`
nstart=`grep "^nstart=" $CONFIG | cut -d"=" -f2`
nend=`grep "^nend=" $CONFIG | cut -d"=" -f2`
specialchar=(`grep "^specialchar\[[0-9]*\]=" $CONFIG | cut -d"=" -f2`)
format=`grep "^format=" $CONFIG | cut -d"=" -f2`

nelements=`grep "^.\{$chars\}$" "$wordlist" | grep -v "à\|è\|é\|ì\|ò\|ù\|'" | wc -l | cut -d " " -f1 | sed 's/ //'`
nspecials=`grep -c "^specialchar\[[0-9]*\]=" $CONFIG`

echo "[+] Ready for $(( $nelements * $nspecials * ($nend - $nstart + 1) )) passwords"

if $u; then u="."; else u="^"; fi
echo "[+] Password format: $format"
echo -n "[+] Password Type: "
case $format in
	wns) head -n1 "$wordlist" | sed "s/\b\($u\)/\u\1/" | sed "s/$/$nstart/" | sed "s/$/$specialchar/" ;;
	wsn) head -n1 "$wordlist" | sed "s/\b\($u\)/\u\1/" | sed "s/$/$specialchar/" | sed "s/$/$nstart/" ;;
	nws) head -n1 "$wordlist" | sed "s/\b\($u\)/\u\1/" | sed "s/^/$nstart/" | sed "s/$/$specialchar/" ;;
	swn) head -n1 "$wordlist" | sed "s/\b\($u\)/\u\1/" | sed "s/$/$nstart/" | sed "s/^/$specialchar/" ;;
	nsw) head -n1 "$wordlist" | sed "s/\b\($u\)/\u\1/" | sed "s/^/$specialchar/" | sed "s/^/$nstart/" ;;
	snw) head -n1 "$wordlist" | sed "s/\b\($u\)/\u\1/" | sed "s/^/$nstart/" | sed "s/^/$specialchar/" ;;
	*) echo "error.."
	exit
esac

echo "[+] File output: $newwordlist"

echo
read -p "Press [Enter] key to start or [Ctrl+C] key to stop..."
echo

# Initialize new wordlist
cat /dev/null > $newwordlist

wns(){
grep "^.\{$chars\}$" "$wordlist" | grep -v "à\|è\|é\|ì\|ò\|ù\|'" | sed "s/\b\($u\)/\u\1/" | sort | while read word;
	do {
		for n in $(seq $nstart $nend)
		do
			for s in "${specialchar[@]}"
			do
				echo $word$n$s >> $newwordlist
			done
		done
	}
	done
}

wsn(){
grep "^.\{$chars\}$" "$wordlist" | grep -v "à\|è\|é\|ì\|ò\|ù\|'" | sed "s/\b\($u\)/\u\1/" | sort | while read word;
	do {
		for n in $(seq $nstart $nend)
		do
			for s in "${specialchar[@]}"
			do
				echo $word$s$n >> $newwordlist
			done
		done
	}
	done
}

nws(){
grep "^.\{$chars\}$" "$wordlist" | grep -v "à\|è\|é\|ì\|ò\|ù\|'" | sed "s/\b\($u\)/\u\1/" | sort | while read word;
	do {
		for n in $(seq $nstart $nend)
		do
			for s in "${specialchar[@]}"
			do
				echo $n$word$s >> $newwordlist
			done
		done
	}
	done
}

swn(){
grep "^.\{$chars\}$" "$wordlist" | grep -v "à\|è\|é\|ì\|ò\|ù\|'" | sed "s/\b\($u\)/\u\1/" | sort | while read word;
	do {
		for n in $(seq $nstart $nend)
		do
			for s in "${specialchar[@]}"
			do
				echo $s$word$n >> $newwordlist
			done
		done
	}
	done
}

nsw(){
grep "^.\{$chars\}$" "$wordlist" | grep -v "à\|è\|é\|ì\|ò\|ù\|'" | sed "s/\b\($u\)/\u\1/" | sort | while read word;
	do {
		for n in $(seq $nstart $nend)
		do
			for s in "${specialchar[@]}"
			do
				echo $n$s$word >> $newwordlist
			done
		done
	}
	done
}

snw(){
grep "^.\{$chars\}$" "$wordlist" | grep -v "à\|è\|é\|ì\|ò\|ù\|'" | sed "s/\b\($u\)/\u\1/" | sort | while read word;
	do {
		for n in $(seq $nstart $nend)
		do
			for s in "${specialchar[@]}"
			do
				echo $s$n$word >> $newwordlist
			done
		done
	}
	done
}

started=`date`
echo "Started: $started"
case $format in
	wns) wns ;;
	wsn) wsn ;;
	nws) nws ;;
	swn) swn ;;
	nsw) nsw ;;
	snw) snw ;;
	*) echo "error.."
	exit
esac
stopped=`date`

echo "Stopped: $stopped"
