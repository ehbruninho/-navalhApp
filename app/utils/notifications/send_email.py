import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_token(receiver,verified_code):
    server_smtp = 'mail.migrasolucoesti.com.br'
    port_smtp = 587
    email_sender = 'bruno.santos@migrasolucoesti.com.br'
    password = 'Mainframe@2024'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = receiver
    msg['Subject'] = 'Confirmação de cadastro'

    body = f"""
    <html>
      <body>
        <h2>Recebemos sua solicitação de cadastro.</h2>
        <h2>Esse é o seu código de confirmação: {verified_code} .</h2>
        <h2>Se não foi você, ignore este e-mail.</h2>
      </body>
    </html>
    """

    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(server_smtp, port_smtp)
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, receiver, msg.as_string())
        server.quit()
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar email! Erro {e}')