@echo off
chcp 65001 > nul
title WoW 5.5e Reference Guide - Local Server

cd /d "%~dp0"

echo ===================================================================
echo   World of Warcraft 5.5e • D&D 2024 Reference Guide
echo ===================================================================
echo.
echo [1/2] Запуск сервера тестирования...

python start_server.py 2>nul || py start_server.py 2>nul || (
    echo [!] Python не обнаружен в PATH.
    echo [*] Запуск страницы index.html напрямую в браузере...
    start "" "index.html"
)

pause
