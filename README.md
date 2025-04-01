# sige psc


# Conectando Postgree pelo terminal e o acessando o banco de dados na minha máquina
# Digitar no terminal: - ssh -L 5432:localhost:5432 aws-vm-psc
# Entrar no Postgree local e escolher AWS-PSC

# Acessando a página local pelo terminal
# Comandos de acesso:-> $env:DJANGO_SETTINGS_MODULE = "sige_psc.settings_dev"
# Rodar a página: -> python manage.py runserver

# atualização do site do terminal do PC não pelo VSCODE para a AWS
# 1 - -> ssh aws-vm-psc
# 2 - -> Entrar no diretório -> cd sige_psc
# 3 - -> Atualização do repositório local -> git pull
# 4 - -> Ativar a venv -> source venv/bin/activate
# 5 - -> Aplicar a migração do banco de dados do Django no projeto -> python manage.py migrate
# 6 - -> Executando a aplicação (Gunicorn) -> /sige_psc$ /home/ubuntu/sige_psc/venv/bin/python3 /home/ubuntu/sige_psc/venv/bin/gunicorn sige_psc.wsgi --daemon
# 7 - -> Atualizar a pasta de imagens coletar as imagens static-> python manage.py collectstatic
# 8 - -> 



