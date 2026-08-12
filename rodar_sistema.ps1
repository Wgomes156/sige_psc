# Script para rodar o SIGE PSC com um único comando
$env:DJANGO_SETTINGS_MODULE = "sige_psc.settings_dev"
Write-Host "🚀 Iniciando o servidor SIGE PSC..." -ForegroundColor Green
Write-Host "⚙️  Configuração: $env:DJANGO_SETTINGS_MODULE" -ForegroundColor Cyan
Write-Host "📍 Acesse: http://127.0.0.1:8000/" -ForegroundColor Blue
Write-Host ""
python manage.py runserver
