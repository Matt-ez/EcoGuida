@echo off
echo ============================
echo  Compilazione EcoGuida.exe
echo ============================
cd /d "%~dp0"

REM Pulisce la build precedente
rmdir /s /q build
rmdir /s /q dist

REM Compila usando lo .spec
pyinstaller --clean --noconfirm EcoGuida.spec

echo ============================
echo  Esecuzione EcoGuida.exe
echo ============================
start dist\EcoGuida.exe
pause
