# 🧾 Facturación API con FastAPI

API backend profesional para gestión de facturas con autenticación JWT y base de datos PostgreSQL.

## 🚀 Tecnologías

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Passlib (bcrypt)

## 🔐 Funcionalidades

- Registro y login de usuarios
- Autenticación con JWT
- Protección de rutas
- Creación de facturas
- Actualización de estado (`pending`, `paid`, `cancelled`)
- Métricas de facturación (total pagado)
- Relación usuario → facturas

## 📦 Endpoints principales

### Auth
- POST /auth/register
- POST /auth/login

### Facturas
- GET /invoices/
- POST /invoices/
- PUT /invoices/{id}
- GET /invoices/total

## 🧪 Ejemplo de uso

```bash
curl -X GET http://127.0.0.1:8000/invoices/ \
-H "Authorization: Bearer TOKEN"

## Instalacion
- git clone <repo>
- cd factura_api
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- uvicorn app.main:app --reload