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