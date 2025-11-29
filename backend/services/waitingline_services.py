from database.connection import db
from database.models.waitingline import Waitingline
from sqlalchemy.exc import IntegrityError
from core.email_client import email_client


def add_user_to_waiting_line(name: str, email: str):

    new_entry = Waitingline(name=name, email=email)

    try:
        db.session.add(new_entry)
        db.session.commit()
        db.session.refresh(new_entry)

    except IntegrityError:
        db.session.rollback()
        return {"status": "error", "message": "O e-mail fornecido já está na lista de espera."}

    except Exception as e:
        db.session.rollback()
        return {"status": "error", "message": f"Erro ao salvar no banco: {str(e)}"}

    html_content = f"""
    <h1>Obrigado por se inscrever no Taylor!</h1>
    <p>Olá <strong>{new_entry.name}</strong>,</p>
    <p>Recebemos sua inscrição com sucesso. Você receberá novidades e atualizações por e-mail — fique de olho na sua caixa de entrada.</p>
    <p>— Equipe Taylor</p>
    """

    try:
        email_client.send_email(
            to=new_entry.email,
            subject="Você está na lista de espera do TAYLOR",
            html=html_content
        )
    except Exception as email_error:
        print(f"Erro ao enviar email: {email_error}")

    return {
        "status": "success",
        "message": "Adicionado à fila.",
        "id": new_entry.id
    }
