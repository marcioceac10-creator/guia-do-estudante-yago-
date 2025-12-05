@echo off
echo Iniciando servidor Flask...
start "" python alice.py

timeout /t 2 >nul

echo Abrindo navegador...
start "" http://127.0.0.1:5000
