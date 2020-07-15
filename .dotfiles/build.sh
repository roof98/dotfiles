#! /bin/sh

#script to build config files into a their proper places
cd dotfiles

mv .bashrc .bash_aliases ~

cp .config/* ~/.config

if ! command -v pfetch &> /dev/null
then
    echo "INSTALL PFETCH FOR MEMES AND RICING"
    exit
fi
