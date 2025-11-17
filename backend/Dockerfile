FROM python:3.12-slim

WORKDIR /app

RUN pip install PDM

COPY pyproject.toml pdm.lock /app/

RUN pdm install --prod

COPY . /app

EXPOSE 8000

CMD ["pdm", "run", "gunicorn", "main:app", "-b", "0.0.0.0:8000"]
