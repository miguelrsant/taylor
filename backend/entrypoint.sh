#!/bin/bash

echo "📌 Iniciando entrypoint do backend..."

# ================================
# 1. Verifica se as variáveis existem
# ================================
: "${POSTGRES_HOST:?POSTGRES_HOST não definido}"
: "${POSTGRES_PORT:?POSTGRES_PORT não definido}"
: "${POSTGRES_USER:?POSTGRES_USER não definido}"
: "${POSTGRES_DB:?POSTGRES_DB não definido}"

echo "🔧 Banco configurado para: $POSTGRES_USER@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"

# ================================
# 2. Espera o Postgres ficar pronto
# ================================
echo "⏳ Aguardando Postgres iniciar..."

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" >/dev/null 2>&1; do
    echo "⌛ Ainda aguardando o banco..."
    sleep 1
done

echo "✅ Postgres está pronto!"

# ================================
# 3. Rodar migrações automaticamente
# ================================
echo "🚀 Aplicando migrations..."

pdm run flask --app main.py db upgrade -d database/migrations

if [ $? -ne 0 ]; then
    echo "❌ Erro ao rodar migrations!"
    exit 1
fi

echo "✅ Migrations aplicadas com sucesso!"

# ================================
# 4. Iniciar o Gunicorn
# ================================
echo "🔥 Iniciando backend com Gunicorn..."

exec pdm run gunicorn main:app -b 0.0.0.0:8000 --workers 4 --timeout 180
