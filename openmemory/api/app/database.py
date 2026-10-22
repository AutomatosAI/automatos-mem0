import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# load .env file (make sure you have DATABASE_URL set)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./openmemory.db")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in environment")

# Pin the psycopg2 dialect explicitly — requirements.txt only installs
# psycopg2-binary, but a bare "postgresql://" DSN lets SQLAlchemy pick its
# default driver, which varies by SQLAlchemy version and resolved to the
# (uninstalled) psycopg v3 driver here, crash-looping the service.
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)

# SQLAlchemy engine & session
# SQLAlchemy engine & session
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_size=int(os.getenv("SQLALCHEMY_POOL_SIZE", "20")),
    max_overflow=int(os.getenv("SQLALCHEMY_MAX_OVERFLOW", "30")),
    pool_pre_ping=True,
    pool_recycle=300,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
