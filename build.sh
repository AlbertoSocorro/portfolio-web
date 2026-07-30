#!/usr/bin/env bash
# Salir inmediatamente si un comando falla
set -o errexit

# 1. Instalar dependencias de Python
pip install -r requirements.txt

# 2. Instalar dependencias de Node y compilar Tailwind v4
npm install
npm run dev:css & # O un script de compilación única si lo prefieres, pero para desarrollo usamos build

# 3. Recopilar archivos estáticos de Django (incluyendo Tailwind compilado)
python manage.py collectstatic --no-input

# 4. Aplicar migraciones a la base de datos
python manage.py makemigrations
python manage.py migrate
python manage.py poblar_portfolio