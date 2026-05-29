# Flask + Supabase Portfolio App

A production-ready, blank-slate portfolio application built with **Flask** and **Supabase**.  Designed around industry-standard architecture patterns so you can start building immediately without fighting the scaffolding.

---

## ✨ Features

| Area | Choice |
|------|--------|
| Web framework | [Flask 3](https://flask.palletsprojects.com/) with Application Factory |
| Database / Auth | [Supabase](https://supabase.com/) (Postgres + Row-Level Security) |
| Config management | Environment variables via `python-dotenv` |
| Routing | Blueprints (`main`, `api/v1`) |
| Production server | [Gunicorn](https://gunicorn.org/) |
| Testing | [pytest](https://pytest.org/) with test client fixtures |
| Linting | [Ruff](https://docs.astral.sh/ruff/) |

---

## 🗂️ Project Structure

```
.
├── app/
│   ├── __init__.py          # Application factory (create_app)
│   ├── config.py            # Dev / Prod / Test configuration classes
│   ├── extensions.py        # Flask extension initialisation
│   ├── models/              # Python-side data models / dataclasses
│   ├── routes/
│   │   ├── main.py          # Server-rendered HTML routes (Blueprint)
│   │   └── api.py           # REST API routes – /api/v1 (Blueprint)
│   ├── services/
│   │   └── supabase_client.py  # Singleton Supabase client
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/main.js
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── errors/
│           ├── 404.html
│           └── 500.html
├── tests/
│   ├── conftest.py          # Shared pytest fixtures (app, client, runner)
│   ├── test_routes.py
│   ├── test_api.py
│   └── test_supabase_service.py
├── .env.example
├── .gitignore
├── pyproject.toml           # pytest + ruff config
├── requirements.txt
├── requirements-dev.txt
└── run.py                   # Dev server entry point
```

---

## 🚀 Quick Start

### 1. Clone & create a virtual environment

```bash
git clone https://github.com/alexandergshaw/template-python-database-app-.git
cd template-python-database-app-
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements-dev.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
# Edit .env and fill in your Supabase URL and anon key
```

### 4. Run the development server

```bash
python run.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🧪 Testing

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

---

## 🔍 Linting

```bash
ruff check .
```

---

## 🏭 Production Deployment

```bash
gunicorn "app:create_app()" \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --access-logfile - \
  --error-logfile -
```

Set `FLASK_ENV=production` and ensure all required environment variables are present (see `.env.example`).

---

## 🔐 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `SECRET_KEY` | ✅ | Long random string used for session signing |
| `SUPABASE_URL` | ✅ | Your Supabase project URL |
| `SUPABASE_ANON_KEY` | ✅ | Supabase anon/public API key |
| `SUPABASE_SERVICE_ROLE_KEY` | ⚠️ | Service-role key for admin ops – **never expose to the browser** |
| `FLASK_ENV` | – | `development` (default) or `production` |
| `FLASK_DEBUG` | – | `true` / `false` |
| `HOST` | – | Bind address (default: `127.0.0.1`) |
| `PORT` | – | Port number (default: `5000`) |

---

## 🛠️ Architecture Decisions

- **Application Factory** (`create_app`) – makes the app testable, configurable, and extensible without global state.
- **Blueprints** – clean separation between HTML pages and API routes; easy to add new resource modules.
- **Service layer** – `app/services/` keeps Supabase (or any future backend) behind a thin abstraction so routes stay lean.
- **Config classes** – one class per environment; production raises immediately on missing secrets.
- **12-factor compliant** – all configuration comes from environment variables, not hard-coded values.
