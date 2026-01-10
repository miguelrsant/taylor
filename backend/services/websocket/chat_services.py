import os
from openai import OpenAI
from database.connection import db
from database.models.conversations import Conversations
from database.models.messages import Messages
from database.models.user_memory import UserMemory

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "Você é o Taylor, um assistente útil, direto e técnico. "
    "Responda de forma prática e com passos claros."
)

HISTORY_LIMIT = 70


def _get_or_create_conversation(user_id: int, conversation_id: str | None) -> Conversations:
    if conversation_id:
        conv = Conversations.query.filter_by(
            id=conversation_id, user_id=user_id).first()
        if not conv:
            raise ValueError("CONVERSATION_NOT_FOUND")
        return conv

    conv = Conversations(user_id=user_id)
    db.session.add(conv)
    db.session.commit()
    return conv


def _get_user_memory_text(user_id: int) -> str:
    mem = UserMemory.query.filter_by(user_id=user_id).first()
    if not mem or not mem.memory_text:
        return ""
    return mem.memory_text.strip()


def _get_recent_messages(conversation_id: str, limit: int = HISTORY_LIMIT) -> list[dict]:
    rows = (
        Messages.query
        .filter_by(conversation_id=conversation_id)
        .order_by(Messages.created_at.desc())
        .limit(limit)
        .all()
    )
    rows.reverse()
    return [{"role": r.role, "content": r.content} for r in rows]


def chat_turn(user_id: int, conversation_id: str | None, user_message: str, file_path: str | None = None, original_filename: str | None = None,) -> dict:
    conv = _get_or_create_conversation(user_id, conversation_id)

    db.session.add(Messages(conversation_id=conv.id, role="user", content=user_message,
                   file_path=file_path, original_filename=original_filename))
    db.session.commit()

    memory_text = _get_user_memory_text(user_id)
    recent = _get_recent_messages(conv.id, limit=HISTORY_LIMIT)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if memory_text:
        messages.append(
            {"role": "system", "content": f"Contexto do usuário:\n{memory_text}"})
    messages.extend(recent)

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    reply = (resp.choices[0].message.content or "").strip()

    db.session.add(Messages(conversation_id=conv.id,
                   role="assistant", content=reply))
    db.session.commit()

    return {"conversation_id": conv.id, "reply": reply}
