import yagmail
from datetime import datetime
import schedule
import time

# Configurações do e-mail
EMAIL_REMETENTE = 'remetente'
SENHA = 'senha'
DESTINATARIOS = ['xxxxxxxxxxx']
DESTINATARIOS_CC = ['xxxxxxxxx']

# Caminho para a planilha
CAMINHO_PLANILHA = 'C:\\Users\\raquel.guerreiro\\Documents\\testepy.xlsx'

def enviar_email_com_anexo():
    try:
        data_atual = datetime.now().strftime('%d-%m-%Y')
        print(f'[DEBUG] Data atual: {data_atual}')
        
        yag = yagmail.SMTP(EMAIL_REMETENTE, SENHA)
        print('[DEBUG] Conectado ao servidor de e-mail')

        yag.send(
            to=DESTINATARIOS,
            cc=DESTINATARIOS_CC,
            subject=f'Parte da Planilha - {data_atual}',
            contents='Por favor, veja a planilha em anexo.',
            attachments=CAMINHO_PLANILHA
        )
        print(f'E-mail enviado com sucesso em {data_atual}')
    except Exception as e:
        print(f'[ERRO] Ocorreu um erro ao enviar o e-mail: {e}')

# Agendar o envio do e-mail toda segunda-feira às 16:00
schedule.every().monday.at("16:00").do(enviar_email_com_anexo)

print("Agendamento configurado. Aguardando...")

# Manter o script em execução para verificar o agendamento
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto se há alguma tarefa pendente
