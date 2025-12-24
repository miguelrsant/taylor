from core.email_client import email_client

def send_email_waitingline(to: str, name: str):
    html = f"""
        <h1>Obrigado por se inscrever no Taylor!</h1>
        <p>Olá <strong>{name}</strong>,</p>
        <p>Recebemos sua inscrição com sucesso. Você receberá novidades e atualizações por e-mail — fique de olho na sua caixa de entrada.</p>
        <p>— Equipe Taylor</p>
        """
    subject="Você está na lista de espera do TAYLOR"
    
    email_client.send_email(to, subject, html)
    return {"ok": True, "to": to}

def send_email_register(to: str, name: str):
    html = f"""
        <h1>Obrigado por se registrar no Taylor!</h1>
        <p>Olá <strong>{name}</strong>,</p>
        <p>Seu cadastro foi realizado com sucesso. Em breve você receberá novidades e atualizações diretamente no seu e-mail.</p>
        <p>— Equipe Taylor</p>
        """
    subject="Você agora está no TAYLOR"
    
    email_client.send_email(to, subject, html)
    return {"ok": True, "to": to}

def send_email_recover_password(to: str, name: str, token: str, expires_minutes: int):

    html = f"""
        <h1>Recuperação de Senha</h1>
        <p>Olá <strong>{name}</strong>,</p>
        <p>Recebemos uma solicitação para redefinir sua senha. Se você não fez essa solicitação, por favor, ignore este e-mail.</p>
        <p>Para redefinir sua senha, clique no link abaixo:</p>
        <p><a href="https://taylorhub.com.br/reset-password?token={token}">Redefinir Senha</a></p>
        <p>Este link expirará em {expires_minutes} minutos.</p>
        <p>— Equipe Taylor</p>
        """
    subject="RECUPERAÇÃO DE SENHA - TAYLOR"

    email_client.send_email(to, subject, html)

def send_email_reset(to: str, name: str):
    html = f"""
        <h1>Senha Redefinida com Sucesso</h1>
        <p>Olá <strong>{name}</strong>,</p>
        <p>Sua senha foi redefinida com sucesso.</p>
        <p>— Equipe Taylor</p>
        """
    subject = "SENHA REDEFINIDA - TAYLOR"
    
    email_client.send_email(to, subject, html)