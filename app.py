#Importa as bibliotecas necessárias
import pandas as pd
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#Acessa a planilha e filtra os dados de acordo com o pagamento em atraso
df = pd.read_excel('dados.xlsx')

atrasados = df[df['pagamento'].str.contains('atraso', case=False, na=False)]

#repassa a apikey do serviço do SendGrid presente nas variáveis de ambiente
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
if not SENDGRID_API_KEY:
    print("Erro: A variável de ambiente 'SENDGRID_API_KEY' não está definida ou está vazia.")
    exit(1)
else:
    print("API Key carregada com sucesso.")

#logica para o envio dos emails
def enviar_email(destinatario, nome):
    message = Mail(
        from_email='ordabelem@hotmail.com',
        to_emails=destinatario,
        subject='Aviso de pagamento em atraso',
        html_content=f"""
        <p>Olá {nome},</p>
        <p>Verificamos que há um pagamento em atraso em seu cadastro. Por favor, regularize sua situação o mais breve possível.</p>
        <p>Atenciosamente,<br>RODNEYCOM LTDA</p>
        """
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f'E-mail enviado para {nome} - {destinatario}')
    except Exception as e:
        print(f'Falha ao enviar e-mail para {nome} - {destinatario}: {e}')
        
for index, row in atrasados.iterrows():
    nome = row['nome']
    email = row['email']
    enviar_email(email, nome)
    
