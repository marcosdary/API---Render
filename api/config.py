from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Configurações internas para conexão com banco de dados PostgreSQL 
URL = getenv("url_postgree")
"&options=-c%20inet_family%3Dipv4"
ENGINE = create_engine(
    URL
)

session_fab = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
)

session = session_fab()
