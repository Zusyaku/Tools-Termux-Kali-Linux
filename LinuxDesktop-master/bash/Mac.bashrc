# ~/.bashrc: executed by bash(1) for non-login shells.

# colors
darkgrey="$(tput bold ; tput setaf 0)"
white="$(tput bold ; tput setaf 7)"
red="$(tput bold; tput setaf 1)"
green="$(tput bold; tput setaf 2)"
yellow="$(tput bold; tput setaf 3)"
purple="$(tput bold; tput setaf 4)"
pink="$(tput bold; tput setaf 5)"
cyan="$(tput bold; tput setaf 6)"
nc="$(tput sgr0)"

export PS1="\[$white\]\H:\W \u\$ "
# umask 022
