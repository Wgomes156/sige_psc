#!/bin/bash
# ═══════════════════════════════════════════════════════
# Script de configuração inicial - Ubuntu/Debian VPS
# ═══════════════════════════════════════════════════════

echo "Atualizando pacotes..."
sudo apt update && sudo apt upgrade -y

echo "Instalando dependências do sistema (Python, PostgreSQL, Nginx)..."
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl -y

echo "Instalando virtualenv..."
sudo -H pip3 install virtualenv

# ═══════════════════════════════════════════════════════
# IMPORTANTE: Configuração do Banco de Dados
# ═══════════════════════════════════════════════════════
# Para configurar o PostgreSQL, execute os seguintes comandos manualmente:
#
# sudo -u postgres psql
# CREATE DATABASE sige_psc;
# CREATE USER sige_user WITH PASSWORD 'senha_forte_do_banco';
# ALTER ROLE sige_user SET client_encoding TO 'utf8';
# ALTER ROLE sige_user SET default_transaction_isolation TO 'read committed';
# ALTER ROLE sige_user SET timezone TO 'UTC';
# GRANT ALL PRIVILEGES ON DATABASE sige_psc TO sige_user;
# \q
# ═══════════════════════════════════════════════════════

# Exemplo de criação de ambiente virtual (ajuste o diretório /var/www/sige_psc)
# cd /var/www/sige_psc
# virtualenv venv
# source venv/bin/activate
# pip install -r requirements.txt
# export DJANGO_SETTINGS_MODULE=sige_psc.settings_prod
# python manage.py migrate
# python manage.py collectstatic

# Para o Gunicorn e Nginx, mova os arquivos para os locais corretos e ative os serviços:
# sudo cp deploy/gunicorn.service /etc/systemd/system/
# sudo cp deploy/nginx_pscservice.conf /etc/nginx/sites-available/pscservice.site
# sudo ln -s /etc/nginx/sites-available/pscservice.site /etc/nginx/sites-enabled/
# sudo systemctl daemon-reload
# sudo systemctl start gunicorn
# sudo systemctl enable gunicorn
# sudo systemctl restart nginx

echo "Instalação concluída. Verifique os comentários neste arquivo para as configurações manuais."
