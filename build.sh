#!/usr/bin/env bash
# Salir inmediatamente si un comando falla
set -o errexit

# 1. Instalar dependencias de Python
pip install -r requirements.txt

# 2. Instalar dependencias de Node y compilar Tailwind
npm install
npm run build:css

# 3. Crear explícitamente la carpeta staticfiles
mkdir -p staticfiles

# 4. Recopilar archivos estáticos de Django
python manage.py collectstatic --no-input

# 5. Aplicar migraciones automáticamente en producción
python manage.py migrate

# 6. (Opcional) Poblar la base de datos automáticamente si está vacía
python manage.py poblar_portfolio