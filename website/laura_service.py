import os
import google.generativeai as genai

# Configuração do prompt de sistema para dar a personalidade da Laura
LAURA_SYSTEM_PROMPT = """
Você é a Laura, uma assistente de IA amigável e natural da PSC Service.
Sua função é conversar com os visitantes do site de forma humanizada, fluida e espontânea.

O foco de atuação da PSC Service é:
1. Consultoria de Negócios (BP / RH)
2. Gerenciamento de Projetos
3. Investigação Empresarial
4. Treinamento e Capacitação
5. Consultoria de Implementação de Compliance

Diretrizes de Conversação:
- Evite se apresentar novamente ou dar boas-vindas nas respostas seguintes (isso já é feito na primeira mensagem da janela de chat).
- Converse de forma natural e informal, como uma pessoa real conversando por chat. Evite listas longas e estruturadas em todas as respostas; prefira parágrafos curtos e um bate-papo dinâmico.
- Caso o usuário precise de uma proposta ou especialista, oriente-o a usar a seção de Contato ou dê os dados (E-mail: psc.servicebr@gmail.com, Tel: 55 (21) 998054530).
"""

def get_laura_response(user_message, chat_history=None):
    """
    Obtém uma resposta da Laura usando a API do Gemini com suporte a histórico de chat.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key or api_key == "sua_chave_do_gemini_aqui":
        return (
            "Olá! Eu sou a Laura. Para que eu possa conversar de verdade com você, "
            "é necessário configurar a variável `GEMINI_API_KEY` no arquivo `.env` do projeto. "
            "Por favor, configure sua chave de API para iniciarmos!"
        )

    try:
        # Configura a API
        genai.configure(api_key=api_key)
        
        # Usamos o modelo gemini-3.6-flash
        model = genai.GenerativeModel(
            model_name="gemini-3.6-flash",
            system_instruction=LAURA_SYSTEM_PROMPT
        )
        
        # Formata o histórico recebido para o formato esperado pelo SDK do Gemini
        formatted_history = []
        if chat_history:
            for msg in chat_history:
                # O SDK do Gemini usa 'user' e 'model' para as roles
                role = "user" if msg.get("sender") == "user" else "model"
                formatted_history.append({
                    "role": role,
                    "parts": [msg.get("text", "")]
                })
        
        # Inicia a sessão de chat com o histórico
        chat = model.start_chat(history=formatted_history)
        response = chat.send_message(user_message)
        return response.text
    except Exception as e:
        return f"Ops! Tive um problema ao processar sua mensagem. Erro: {str(e)}"
