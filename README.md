# sige psc

## Conectando Postgree pelo terminal e o acessando o banco de dados na minha máquina:

- Digitar no terminal: - ssh -L 5432:localhost:5432 aws-vm-psc
- Entrar no Postgree local e escolher AWS-PSC

## Acessando a página local pelo terminal

- Comandos de acesso:-> $env:DJANGO_SETTINGS_MODULE = "sige_psc.settings_dev"
- Rodar a página: -> python manage.py runserver

## Atualização do site do terminal do PC não pelo VSCODE para a AWS

1. ssh aws-vm-psc
2. Entrar no diretório -> cd sige_psc
3. Atualização do repositório local -> git pull
4. Ativar a venv -> source venv/bin/activate
5. Aplicar a migração do banco de dados do Django no projeto -> python manage.py migrate
6. Executando a aplicação (Gunicorn) -> /sige_psc$ /home/ubuntu/sige_psc/venv/bin/python3 /home/ubuntu/sige_psc/venv/bin/gunicorn sige_psc.wsgi --daemon
7. Atualizar a pasta de imagens coletar as imagens static-> python manage.py collectstatic

## Rodando projeto localmente

1. Clone o projeto

   ```sh
   git clone https://github.com/Wgomes156/sige_psc.git
   cd sige_psc
   ```

1. Crie e ative um ambiente virtual

   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

1. Instale as dependências

   ```sh
   pip install -r requirements.txt
   ```

1. Configure variãveis de ambiente

   Se o projeto usa .env ou settings.py separado por ambiente (ex: settings.dev, settings.prod), veja como ele está estruturado. Você pode ter que criar um arquivo .env com chaves como:

1. Ative o Ambiente Virtual (se estiver no Windows PowerShell):

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

1. Instale as dependências necessárias:

   ```sh
   pip install -r requirements.txt
   ```

1. Prepare as atualizações do banco de dados:

   ```sh
   python manage.py makemigrations
   ```

1. Aplique as migrações (cria as tabelas no SQLite):

   ```sh
   python manage.py migrate
   ```

1. Crie um super usuário (Administrador):

   ```sh
   python manage.py createsuperuser
   ```

1. Rode o servidor local:
   ```sh
   python manage.py runserver
   ```

## Acesso ao sistema pelo terminal

# 1 - Digite os comandos no terminal para ativação da venv:
(venv) PS D:\sige_psc-main> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& d:\sige_psc-main\venv\Scripts\Activate.ps1)

# 2 - python manage.py runserver

# 3 - Como fica no terminal:

# PS D:\sige_psc-main> Digitar: 
 (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& d:\sige_psc-main\venv\Scripts\Activate.ps1)

(venv) PS D:\sige_psc-main> python manage.py runserver

Após rodar o servidor, acesse o sistema no navegador pelo endereço:
**http://127.0.0.1:8000/**

---

## Formulário de Contato

O formulário de contato do site envia as mensagens diretamente para o e-mail da PSC Service.

### Como funciona

- O visitante preenche **Nome**, **E-mail**, **Assunto** e **Mensagem** na página de Contato.
- Ao enviar, o sistema dispara um e-mail para **psc.servicebr@gmail.com** contendo o nome e e-mail do remetente no corpo da mensagem.

### Arquivos envolvidos

| Arquivo | Descrição |
|---|---|
| `website/views.py` → função `contato()` | Lógica de envio do e-mail (usa `send_mail` do Django) |
| `website/templates/pages/contato.html` | Template HTML do formulário |
| `sige_psc/settings.py` | Configurações SMTP (`EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`) |
| `.env` | Variáveis de ambiente com credenciais do e-mail |

### Configuração SMTP (`.env`)

O envio de e-mails usa o Gmail via SMTP. As variáveis necessárias no `.env` são:

```
EMAIL_HOST_USER=psc.servicebr@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_de_app_aqui
```

> **Nota:** Para o Gmail, é necessário gerar uma **Senha de App** em [myaccount.google.com](https://myaccount.google.com/apppasswords) (a senha comum da conta não funciona com SMTP).

---

## Assistente Virtual Laura 🤖

A Laura é uma assistente de IA integrada ao site que conversa com os visitantes em tempo real, tirando dúvidas sobre os serviços da PSC Service.

### Tecnologia

- Usa a **API do Google Gemini** (modelo `gemini-3.6-flash`)
- Mantém contexto do histórico da conversa (multi-turno)
- Possui personalidade configurável via prompt de sistema

### Arquivos envolvidos

| Arquivo | Descrição |
|---|---|
| `website/laura_service.py` | Lógica da IA — contém o **prompt de treinamento** e a função de chamada à API |
| `website/views.py` → função `laura_chat()` | Endpoint que recebe mensagens do frontend e retorna respostas da Laura |
| `website/urls.py` → rota `laura/chat/` | URL da API de chat |
| `website/templates/layouts/laura_chat.html` | Widget de chat (HTML/CSS/JS) incluído no template base |
| `website/templates/layouts/base.html` | Template base que inclui o widget e o ícone flutuante da Laura |
| `.env` | Variável `GEMINI_API_KEY` com a chave da API do Gemini |

### Configuração da API (`.env`)

```
GEMINI_API_KEY=sua_chave_do_gemini_aqui
```

A chave pode ser obtida em [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

### 📌 Onde alimentar o treinamento da Laura

O "treinamento" da Laura fica na variável **`LAURA_SYSTEM_PROMPT`** no arquivo:

```
website/laura_service.py  (linhas 5–20)
```

Para adicionar informações sobre a PSC Service, basta editar o texto dentro das aspas triplas (`"""`). Exemplos do que incluir:

- **Descrição detalhada dos serviços** (Consultoria BP/RH, Gerenciamento de Projetos, etc.)
- **Diferenciais** e cases de sucesso
- **Perguntas Frequentes (FAQ)** dos clientes
- **Informações da equipe** e áreas de atuação
- **Processos** de contratação e prazos
- **Políticas de Compliance** que a empresa implementa

Exemplo de como expandir:

```python
LAURA_SYSTEM_PROMPT = """
Você é a Laura, uma assistente de IA amigável e natural da PSC Service.
...

Sobre nossos serviços:
- Consultoria de Negócios (BP/RH): Ajudamos empresas a estruturar seus processos
  de Recursos Humanos, incluindo recrutamento, avaliação de desempenho...
- Investigação Empresarial: Realizamos due diligence, análise de riscos corporativos...
...

Perguntas Frequentes:
- P: Como faço para contratar a PSC Service?
  R: Você pode entrar em contato pelo e-mail psc.servicebr@gmail.com ou pelo telefone...
"""
```

> **Importante:** Quanto mais detalhado for o prompt, mais precisa e útil a Laura será nas respostas. Tudo que estiver dentro desse prompt ela vai "saber" responder.
