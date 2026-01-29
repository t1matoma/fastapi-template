# FastAPI Basic Template

A basic template for FastAPI projects with a predefined project structure and JWT authentication using RS256.:

## Package structure:

.

├── docker-compose.yml
├── pyproject.toml
├── uv.lock
├── README.md
└── src
├── main.py
├── api
│ ├── auth.py
│ ├── dependencies.py
│ └── init.py
├── apps
│ ├── auth
│ │ ├── models
│ │ │ ├── user.py
│ │ │ └── init.py
│ │ ├── repositories
│ │ │ ├── user.py
│ │ │ └── init.py
│ │ ├── schemas
│ │ │ ├── token.py
│ │ │ ├── user.py
│ │ │ └── init.py
│ │ ├── services
│ │ │ ├── user.py
│ │ │ └── init.py
│ │ └── init.py
│ └── init.py
├── settings
│ ├── config.py
│ ├── database.py
│ └── init.py
├── utils
│ ├── jwt.py
│ ├── password.py
│ └── init.py
└── init.py
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

