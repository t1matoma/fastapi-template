# FastAPI Basic Template

A basic template for FastAPI projects with a predefined project structure and JWT authentication using RS256.:

## Package structure:
```
.

├── docker-compose.yml
├── pyproject.toml
├── README.md
├── src
│   ├── api
│   │   ├── auth.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   └── ── auth.cpython-312.pyc
│   │       ├── dependencies.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── apps
│   │   ├── auth
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   └── user.py
│   │   │   ├── repositories
│   │   │   │   ├── __init__.py
│   │   │   │   └── user.py
│   │   │   ├── schemas
│   │   │   │   ├── __init__.py
│   │   │   │   ├── token.py
│   │   │   │   └── user.py
│   │   │   └── services
│   │   │       ├── __init__.py
│   │   │       └── user.py
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── settings
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── __init__.py
│   └── utils
│       ├── __init__.py
│       ├── jwt.py
│       ├── password.py
└── uv.lock
```

## How to run:

### Create the `certs/` directory and generate RSA keys:

```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private.pem -out public.pem
```

### Install uv (Follow the official installation instructions for the uv package and project manager).

### Run your project:

```bash
uv run uvicorn src.main:app --reload
```


