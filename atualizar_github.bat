@echo off
echo ========================================
echo Atualizando o sistema no GitHub
echo ========================================

git add .

set /p commit_msg="Digite a mensagem para esta atualizacao (ou aperte Enter para usar 'Atualizacao do sistema'): "
if "%commit_msg%"=="" set commit_msg=Atualizacao do sistema

git commit -m "%commit_msg%"
git push

echo ========================================
echo Atualizacao enviada com sucesso!
echo ========================================
pause
