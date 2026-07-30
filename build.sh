#!/usr/bin/env bash
set -o errexit

# 1. Instalar dependencias de Python
pip install -r requirements.txt

# 2. Instalar dependencias de Node y compilar Tailwind
npm install
npm run build:css

# 3. Crear carpetas necesarias
mkdir -p staticfiles

# 4. Recopilar estáticos
python manage.py collectstatic

# 5. Aplicar migraciones (Esto creará automáticamente el archivo db.sqlite3 si no existe)
python manage.py migrate

# 6. Poblar la base de datos con los datos de prueba
python manage.py poblar_portfolio