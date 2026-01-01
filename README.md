# Instagram Automation SaaS

A powerful automation tool leveraging Meta APIs to streamline Instagram interactions and management.

## 🚀 Features

- **Authentication**: Secure user authentication using JWT (JSON Web Tokens).
- **Health Checks**: Monitoring endpoints for system status.
- **Database Integration**: Robust data management with PostgreSQL and SQLAlchemy.
- **Scalable Architecture**: Built on FastAPI for high performance and easy scalability.

## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: Python 3.x
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: Python-Jose (JWT), Passlib, Bcrypt
- **Server**: Uvicorn

## 📂 Project Structure

```
Meta_API_Based_Automation/
├── backend/
│   ├── app/
│   │   ├── api/        # API Routes (Auth, Health)
│   │   ├── core/       # Core Config (DB, Security)
│   │   ├── models/     # Database Models
│   │   ├── services/   # Business Logic
│   │   └── main.py     # Application Entry Point
│   ├── requirements.txt
│   └── .env
└── frontend/           # (Planned/In Development)
```

## ⚡ Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd Meta_API_Based_Automation
    ```

2.  **Backend Setup**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Configuration**
    Create a `.env` file in the `backend` directory with your database credentials and secret keys:
    ```env
    DATABASE_URL=postgresql://user:password@localhost/dbname
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

4.  **Run the Application**
    ```bash
    uvicorn app.main:app --reload
    ```

    The API will be available at `http://localhost:8000`.
    Access the interactive API docs at `http://localhost:8000/docs`.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
