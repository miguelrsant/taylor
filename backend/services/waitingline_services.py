from database.connection import db
from database.models.waitingline import Waitingline
from sqlalchemy.exc import IntegrityError
from jobs.queue import queue
from jobs.tasks import send_email_waitingline
from rq import Retry


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


    try:

        job = queue.enqueue(
            send_email_waitingline,
            email,
            name,
            job_timeout=120,
            retry=Retry(max=3, interval=[10, 60, 300])
        )
    
    except Exception as email_error:
        print(f"Erro ao enviar email: {email_error}")

    return {
        "status": "success",
        "message": "Adicionado à fila.",
        "id": new_entry.id,
        "email_job_id": job.id if 'job' in locals() else None
    }
