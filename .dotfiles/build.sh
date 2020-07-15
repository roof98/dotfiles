#! /bin/sh

#script to build config files into a their proper places
cd dotfiles

mv .bashrc .bash_aliases ~

cp .config/* ~/.config

