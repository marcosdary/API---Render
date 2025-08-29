from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Configurações internas para conexão com banco de dados PostgreSQL 
URL = "postgresql+psycopg2://postgres:VUqNHCvXRZBPrd3P@db.lqvnmtcbsidpeorqjcme.supabase.co:5432/postgres?sslmode=require"
ENGINE = create_engine(
    URL
)

session_fab = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
)

session = session_fab()
