#!/bin/sh

blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

clear
echo ""
echo -e "$cyan [$okegreen 1$cyan ]$white  Setup Desktop"
echo -e "$cyan [$okegreen 2$cyan ]$white  Setup Shell"
echo -e "$okegreen"
read -p " > " act;
if [ $act = 1 ]
then
    clear
    echo ""
    echo -e "$cyan [$okegreen 1$cyan ]$white  Themes"
    echo -e "$cyan [$okegreen 2$cyan ]$white  Wallpaper"
    echo -e "$okegreen"
    read -p " > " act;
    if [ $act = 1 ]
    then
        mkdir ~/.themes
        mkdir ~/.icons
        clear
        echo ""
        echo -e "$cyan [$okegreen 1$cyan ]$white  XFCE4"
        echo -e "$cyan [$okegreen 2$cyan ]$white  Openbox"
        echo -e "$cyan [$okegreen 3$cyan ]$white  Tint2"
        echo -e "$okegreen"
        read -p " > " act;
        if [ $act = 1 ]
        then
            clear
            echo ""
            echo -e "$cyan [$okegreen 1$cyan ]$white  MacOS Themes Pack"
            echo -e "$okegreen"
            read -p " > " act;
            if [ $act = 1 ]
            then
                clear
                echo ""
                echo -e "$cyan [$okegreen 1$cyan ]$white  MacOS Light"
                echo -e "$cyan [$okegreen 2$cyan ]$white  MacOS Dark"
                echo -e "$cyan [$okegreen 3$cyan ]$white  Yosemite"
                echo -e "$cyan [$okegreen 4$cyan ]$white  Cheetah"
                echo -e "$cyan [$okegreen 5$cyan ]$white  Leopard"
                echo -e "$cyan [$okegreen 6$cyan ]$white  Mavericks"
                echo ""
                echo -e "$cyan [$okegreen 9$cyan ]$white  MacOS Icon Pack"
                echo -e "$cyan [$okegreen 0$cyan ]$white  Install All"
                echo -e "$okegreen"
                read -p " > " act;
                if [ $act = 1 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Theme"
                    git clone https://github.com/B00merang-Project/macOS
                    mv MacOS ~/.themes/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
                if [ $act = 2 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Theme"
                    git clone https://github.com/B00merang-Project/macOS-Dark
                    mv MacOS-Dark ~/.themes/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
                if [ $act = 3 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Theme"
                    git clone https://github.com/B00merang-Project/OS-X-Yosemite
                    mv OS-X-Yosemite ~/.themes/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
                if [ $act = 4 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Theme"
                    git clone https://github.com/B00merang-Project/Mac-OS-X-Cheetah
                    mv Mac-OS-X-Cheetah ~/.themes/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
                if [ $act = 5 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Theme"
                    git clone https://github.com/B00merang-Project/OS-X-Leopard
                    mv OS-X-Leopard ~/.themes/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
                if [ $act = 6 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Theme"
                    git clone https://github.com/B00merang-Project/OS-X-Mavericks
                    mv OS-X-Mavericks ~/.themes/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
                if [ $act = 9 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Icon"
                    git clone https://github.com/keeferrourke/la-capitaine-icon-theme
                    mv la-capitaine-icon-theme ~/.icons/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
                if [ $act = 0 ]
                then
                    clear
                    echo ""
                    echo -e "$cyan [$yellow *$cyan ]$white  Downloading Themes"
                    mkdir themes
                    cd themes
                    git clone https://github.com/B00merang-Project/macOS
                    git clone https://github.com/B00merang-Project/macOS-Dark
                    git clone https://github.com/B00merang-Project/OS-X-Yosemite
                    git clone https://github.com/B00merang-Project/Mac-OS-X-Cheetah
                    git clone https://github.com/B00merang-Project/OS-X-Leopard
                    git clone https://github.com/B00merang-Project/OS-X-Mavericks
                    mv * ~/.themes/
                    git clone https://github.com/keeferrourke/la-capitaine-icon-theme
                    mv la-capitaine-icon-theme ~/.icons/
                    echo ""
                    echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
                fi
            fi
        fi
        if [ $act = 2 ]
        then
            clear
            echo ""
            echo -e "$cyan [$okegreen 1$cyan ]$white  OpenBox Theme Pack"
            echo -e "$okegreen"
            read -p " > " act;
            if [ $act = 1 ]
            then
                clear
                echo ""
                echo -e "$cyan [$yellow *$cyan ]$white  Downloading Themes"
                git clone https://github.com/addy-dclxvi/openbox-theme-collections
                rm openbox-theme-collections/*.jpg
                rm openbox-theme-collections/LIC*
                rm openbox-theme-collections/REA*
                mv openbox-theme-collections/* ~/.themes/
                rm -rf openbox-theme-collections
                echo ""
                echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
            fi
        fi
        if [ $act = 3 ]
        then
            clear
            echo ""
            echo -e "$cyan [$okegreen 1$cyan ]$white  Tint2 Theme Pack"
            echo -e "$okegreen"
            read -p " > " act;
            if [ $act = 1 ]
            then
                clear
                echo ""
                echo -e "$cyan [$yellow *$cyan ]$white  Downloading Themes"
                git clone https://github.com/addy-dclxvi/tint2-theme-collections
                rm tint2-theme-collections/*.jpg
                rm tint2-theme-collections/LIC*
                rm tint2-theme-collections/REA*
                mv tint2-theme-collections/* ~/.themes/
                rm -rf tint2-theme-collections
                echo ""
                echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
            fi
        fi
    fi
    if [ $act = 2 ]
    then
        mkdir ~/.Pictures
        clear
        echo ""
        echo -e "$cyan [$okegreen 1$cyan ]$white  Razer Wallpaper"
        echo -e "$cyan [$okegreen 2$cyan ]$white  ROG Wallpaper"
        echo -e "$cyan [$okegreen 3$cyan ]$white  Anime Wallpaper"
        echo -e "$okegreen"
        read -p " > " act;
        if [ $act = 1 ]
        then
            mkdir RazerWallpaper
            cd RazerWallpaper
            clear
            echo ""
            echo -e "$cyan [$yellow *$cyan ]$white  Downloading Wallpaper"
            wget -q https://assets2.razerzone.com/images/downloads-page/desktop-wallpapers/Quartz-Lair_1920x1080.png
            wget -q https://assets2.razerzone.com/images/downloads-page/desktop-wallpapers/Chroma-Lair_1920x1080.png
            wget -q https://assets2.razerzone.com/images/downloads-page/desktop-wallpapers/Quartz_1920x1080.png
            wget -q https://assets2.razerzone.com/images/downloads-page/desktop-wallpapers/MERRY_CHROMA_1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/Prism_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/1920x1080_Byte.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/1920x1080_Quartz.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/1920x1080_SnakePit.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/Forged-1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/House-Razer-1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/Leviathan-1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/Vice-City-1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/Graphite-1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/Wave-1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/RZR_Space_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/razer_construct_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/razer_disrupt_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/razer_hud_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/razer_slime_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/razer_vault_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/terra-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/fissure-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/cosmic-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/gravity-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/mobile-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/RazerChroma_1920x1080.png
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/irl-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/cny2013_1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/razer_design_labs-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/quad_damage-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/pyro-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/venom-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/team-razer-values-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/team-razer-swirl-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/team-razer-scratched-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/team-razer-panel-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/team-razer-brushed-1920x1080.jpg
            wget -q https://assets.razerzone.com/eedownloads/desktop-wallpapers/team-razer-1920x1080.jpg
            echo ""
            cd ..
            mv RazerWallpaper ~/.Pictures/
            echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
        fi
        if [ $act = 2 ]
        then
            mkdir ROGWallpaper
            cd ROGWallpaper
            clear
            echo ""
            echo -e "$cyan [$yellow *$cyan ]$white  Downloading Wallpaper"
            wget -q https://rog.asus.com/media/1539961014547.png
            wget -q https://rog.asus.com/media/1539690109131.jpg
            wget -q https://rog.asus.com/media/1536943462807.jpg
            wget -q https://rog.asus.com/media/1536943206441.jpg
            wget -q https://rog.asus.com/media/1536943100175.jpg
            wget -q https://rog.asus.com/media/1536942821305.jpg
            wget -q https://rog.asus.com/media/1536942638618.jpg
            wget -q https://rog.asus.com/media/1519319526145.jpg
            wget -q https://rog.asus.com/media/151931910958.jpg
            wget -q https://rog.asus.com/media/1515594166626.jpg
            wget -q https://rog.asus.com/media/1515594095292.jpg
            wget -q https://rog.asus.com/media/1512569211582.jpg
            wget -q https://rog.asus.com/media/1512569081127.jpg
            wget -q https://rog.asus.com/media/1510306048218.jpg
            wget -q https://rog.asus.com/media/1510305850559.jpg
            wget -q https://rog.asus.com/media/1503943716181.jpg
            wget -q https://rog.asus.com/media/1503942920591.jpg
            wget -q https://rog.asus.com/media/1496852673675.jpg
            wget -q https://rog.asus.com/media/1496852612205.jpg
            wget -q https://rog.asus.com/media/1499783496777.png
            wget -q https://rog.asus.com/media/1495474355876.png
            wget -q https://rog.asus.com/media/1495472672934.jpg
            wget -q https://rog.asus.com/media/1495471711745.jpg
            wget -q https://rog.asus.com/media/1495472146876.jpg
            wget -q https://rog.asus.com/media/1487177283646.jpg
            wget -q https://rog.asus.com/media/1487177343412.jpg
            wget -q https://rog.asus.com/media/1514453969724.jpg
            wget -q https://rog.asus.com/media/1514453928598.jpg
            wget -q https://rog.asus.com/media/1487177840962.jpg
            wget -q https://rog.asus.com/media/s/148717808265.jpg
            wget -q https://rog.asus.com/media/1487178221859.png
            wget -q https://rog.asus.com/media/148717842663.jpg
            wget -q https://rog.asus.com/media/1487178434532.jpg
            wget -q https://rog.asus.com/media/1487178443439.png
            wget -q https://rog.asus.com/media/148717847679.jpg
            wget -q https://rog.asus.com/media/1487178576109.jpg
            wget -q https://rog.asus.com/media/1487178583594.png
            wget -q https://rog.asus.com/media/1487178766640.jpg
            wget -q https://rog.asus.com/media/1487178881999.jpg
            wget -q https://rog.asus.com/media/1487178965573.jpg
            wget -q https://rog.asus.com/media/1487179065965.jpg
            wget -q https://rog.asus.com/media/1487179255999.jpg
            wget -q https://rog.asus.com/media/1487179264515.jpg
            wget -q https://rog.asus.com/media/1487179276327.jpg
            wget -q https://rog.asus.com/media/1487179279468.jpg
            wget -q https://rog.asus.com/media/1487179283953.jpg
            wget -q https://rog.asus.com/media/1487179289718.jpg
            wget -q https://rog.asus.com/media/148717962574.jpg
            wget -q https://rog.asus.com/media/1487179693495.jpg
            echo ""
            cd ..
            mv ROGWallpaper ~/.Pictures/
            echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
        fi
        if [ $act = 3 ]
        then
            echo -e "$cyan [$yellow *$cyan ]$white  Comingsoon !!"
        fi
    fi
fi
if [ $act = 2 ]
then
    clear
    echo ""
    echo -e "$cyan [$okegreen 1$cyan ]$white  Bash"
    echo -e "$cyan [$okegreen 2$cyan ]$white  Zsh"
    echo -e "$okegreen"
    read -p " > " act;
    if [ $act = 1 ]
    then
        clear
        echo ""
        echo -e "$cyan [$okegreen 1$cyan ]$white  Hax0r Theme"
        echo -e "$cyan [$okegreen 2$cyan ]$white  MacOS Theme"
        echo -e "$cyan [$okegreen 3$cyan ]$white  Aliases"
        echo -e "$okegreen"
        read -p " > " act;
        if [ $act = 1 ]
        then
            clear
            echo ""
            echo -e "$okegreen Preview$white :"
            echo ""
            echo ""
            echo -e "$okegreen[$cyan root.Hax0r$okegreen ]$white- on -$okegreen[$white ~/Directory$okegreen ]"
            echo -e "$red > "
            echo ""
            echo ""
            echo -e "$yellow Continue ?"
            echo -e "$cyan [$okegreen 1$cyan ]$white  Yes"
            echo -e "$cyan [$okegreen 2$cyan ]$white  No"
            echo -e "$okegreen"
            read -p " > " act;
            if [ $act = 1 ]
            then
                echo ""
                mv ~/.bashrc ~/.bashrc.bak
                cp bash/Hax0r.bashrc ~/.bashrc
                echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
            fi
            if [ $act = 2 ]
            then
                echo -e "$red Abort"
                exit
            fi
        fi
        if [ $act = 2 ]
        then
            clear
            echo ""
            echo -e "$okegreen Preview$white :"
            echo ""
            echo -e "$white"
            echo "MacBook-Pro-9:Directory putra$"
            echo ""
            echo ""
            echo -e "$yellow Continue ?"
            echo -e "$cyan [$okegreen 1$cyan ]$white  Yes"
            echo -e "$cyan [$okegreen 2$cyan ]$white  No"
            echo -e "$okegreen"
            read -p " > " act;
            if [ $act = 1 ]
            then
                echo ""
                mv ~/.bashrc ~/.bashrc.bak
                cp bash/Mac.bashrc ~/.bashrc
                echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
            fi
            if [ $act = 2 ]
            then
                echo -e "$red Abort"
                exit
            fi
        fi
        if [ $act = 3 ]
        then
            clear
            echo ""
            echo -e "$cyan [$okegreen 1$cyan ]$white  LS Aliases"
            echo -e "$cyan [$okegreen 2$cyan ]$white  AntiMistakes Aliases"
            echo -e "$cyan [$okegreen 3$cyan ]$white  My Aliases"
            echo -e "$okegreen"
            read -p " > " act;
            if [ $act = 1 ]
            then
                echo ""
                echo "" >> ~/.bashrc
                echo "export LS_OPTIONS='--color=auto'" >> ~/.bashrc
                echo "alias ls='ls $LS_OPTIONS'" >> ~/.bashrc
                echo "alias ll='ls $LS_OPTIONS -l'"  >> ~/.bashrc
                echo "alias l='ls $LS_OPTIONS -lA'"  >> ~/.bashrc
                echo "alias la='ls -a'"  >> ~/.bashrc
                echo "alias lla='ls -la'"  >> ~/.bashrc
                echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
            fi
            if [ $act = 2 ]
            then
                echo ""
                echo "" >> ~/.bashrc
                echo "alias rm='rm -i'" >> ~/.bashrc
                echo "alias cp='cp -i'" >> ~/.bashrc
                echo "alias mv='mv -i'" >> ~/.bashrc
                echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
            fi
            if [ $act = 3 ]
            then
                echo ""
                echo "" >> ~/.bashrc
                mkdir ~/.fuck
                mkdir ~/.fuck/.project
                echo "alias fuck='cd ~/.fuck && ls -la'" >> ~/.bashrc
                echo "alias project='cd ~/.fuck/.project && ls -la'" >> ~/.bashrc
                echo -e "$cyan [$okegreen *$cyan ]$white  Done !!"
            fi
        fi
    fi
    if [ $act = 2 ]
    then
    echo -e "$cyan [$yellow *$cyan ]$white  Comingsoon !!"
    fi
fi
