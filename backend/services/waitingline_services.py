from database.connection import db 
from database.models.waitingline import Waitingline
from sqlalchemy.exc import IntegrityError

def add_user_to_waiting_line(name: str, email: str):
    
    new_entry = Waitingline(name=name, email=email)
    
    try:
        db.session.add(new_entry)
        db.session.commit()
        db.session.refresh(new_entry) 
        
        return {"status": "success", "message": "Adicionado à fila.", "id": new_entry.id}
    
    except IntegrityError as e:
        db.session.rollback()
        return {"status": "error", "message": "O e-mail fornecido já está na lista de espera."}
        
    except Exception as e:
        db.session.rollback()
        return {"status": "error", "message": f"Erro inesperado: {str(e)}"}
