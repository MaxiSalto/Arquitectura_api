# API Architecture

**API Architecture** es una plantilla base para construir APIs escalables y seguras utilizando FastAPI y MongoDB. Este proyecto está diseñado para adaptarse a diversas aplicaciones, desde gestión de negocios hasta soluciones personalizadas.

## 🚀 Características
- Autenticación segura con JWT.
- Gestión de usuarios y roles (incluyendo administrador).
- Modularidad para extender funcionalidades fácilmente.
- Conexión con MongoDB.
- Carga de configuración sensible desde `.env`.

## 🛠️ Instalación

1. Clona este repositorio:

2. Crea un entorno virtual
    python -m venv venv
    venv\Scripts\activate 

3. instala las dependencias 
    pip install -r requirements.txt

4. Configura las variables de entorno 
    SECRET_KEY=tu_clave_secreta_super_segura
    MONGO_URI=mongodb://usuario:contraseña@localhost:27017
    DB_NAME=api_database
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ALGORITHM=HS256

5. Ejecuta la aplicacion: 
    uvicorn main:app --reload


## 🧰 Endpoints Principales
 - GET /: Mensaje de bienvenida.
 -   POST /users/register: Registrar un usuario.
 -  POST /admin/add: Agregar datos (requiere token de administrador).
 -  GET /general?collection=nombre_coleccion: Obtener datos de una colección.

## 📁 Estructura del Proyecto
api_architecture/
├── auth/
│   ├── auth_handler.py   # Gestión de JWT y roles
│   └── auth_bearer.py    # Middleware de autorización
├── core/
│   ├── config.py         # Configuración global
│   └── database.py       # Conexión a MongoDB
├── models/
│   ├── base.py           # Modelo base genérico
│   └── users.py          # Modelo para usuarios
├── routers/
│   ├── users.py          # Endpoints para usuarios
│   ├── admin.py          # Endpoints administrativos
│   └── general.py        # Endpoints genéricos
├── utils/
│   ├── validators.py     # Validaciones específicas
│   └── helpers.py        # Funciones auxiliares
├── main.py               # Punto de entrada de la API
└── requirements.txt      # Dependencias del proyecto

## 📝 Notas
No olvides proteger tus claves sensibles configurando el archivo .env.
Revisa las dependencias en requirements.txt y actualízalas según sea necesario.

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
