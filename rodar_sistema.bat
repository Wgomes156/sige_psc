@echo off
REM Inicia o servidor Django com um único comando
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ================================
echo   🚀 SIGE PSC - Servidor Local
echo ================================
echo.

set DJANGO_SETTINGS_MODULE=sige_psc.settings_dev
echo ⚙️  Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo.
echo 📍 Acesse: http://127.0.0.1:8000/
echo.
echo python manage.py runserver
python manage.py runserver

pause
