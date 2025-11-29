import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MAIL_HOST: str
    MAIL_PORT: int
    MAIL_USER: str
    MAIL_PASS: str
    MAIL_FROM: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()


class EmailClient:
    def __init__(self):
        self.host = settings.MAIL_HOST
        self.port = settings.MAIL_PORT
        self.user = settings.MAIL_USER
        self.password = settings.MAIL_PASS
        self.sender = settings.MAIL_FROM

    def send_email(self, to: str, subject: str, html: str):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = to

        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.sendmail(self.sender, to, msg.as_string())

        return True


email_client = EmailClient()
