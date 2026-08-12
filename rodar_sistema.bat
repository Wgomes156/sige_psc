@echo off
echo Iniciando o servidor do SIGE PSC...
set DJANGO_SETTINGS_MODULE=sige_psc.settings_dev
call venv\Scripts\activate.bat
python manage.py runserver
pause
