@echo off

net session >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Este script precisa ser executado como administrador!
    pause
    exit /b
)

if not exist "%~dp0Rick.exe" (
    echo Rick.exe nao encontrado na pasta atual!
    pause
    exit /b
)

if not exist "C:\Program Files\Rick" (
    mkdir "C:\Program Files\Rick"
)

copy /Y "%~dp0Rick.exe" "C:\Program Files\Rick\" >nul

for /f "tokens=2,*" %%A in ('reg query HKCU\Environment /v Path 2^>nul') do set "USER_PATH=%%B"

echo %USER_PATH% | find /I "C:\Program Files\Rick" >nul
if not errorlevel 1 (
    echo Pasta ja esta no PATH do usuario!
    pause
    exit /b
)

setx Path "%USER_PATH%;C:\Program Files\Rick" >nul
echo Pasta adicionada ao PATH do usuario!
pause
