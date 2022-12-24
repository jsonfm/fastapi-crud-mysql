from sqlalchemy import create_engine, MetaData
from config import config

# Load variables
DB_USER = config.get("DB_USER", "")
DB_NAME = config.get("DB_NAME", "")
DB_PASSWORD = config.get("DB_PASSWORD", "")
DB_PORT = config.get("DB_PORT", "")
DB_HOST = config.get("DB_HOST", "localhost")

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create a connection
engine = create_engine(DB_URL)
meta = MetaData()
conn = engine.connect()