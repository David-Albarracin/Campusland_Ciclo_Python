@echo off
SETLOCAL EnableDelayedExpansion
set condition=true
git config --global user.name "David-Albarracin" 
git config --global user.email "90213684+David-Albarracin@users.noreply.github.com"
git config --global core.editor “code --wait”
git config --global init.defaultBranch main
ENDLOCAL
