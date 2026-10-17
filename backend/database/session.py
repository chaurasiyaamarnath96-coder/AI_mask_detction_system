from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

Database_URL = "sqlite:///./test.db"  # Replace with your actual database URL
engine = create_engine(Database_URL, connect_args={"check_same_thread": False})  # For SQLite only
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)