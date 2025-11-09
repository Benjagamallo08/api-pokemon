import os
from typing import Generator
import psycopg

from dotenv import load_dotenv

load_dotenv ()

Password_Supabase = os.getenv ("Supabase_password")

url= f"postgresql://postgres.ctwqgmrlkhfuirnbangi:{Password_Supabase}@aws-1-us-east-2.pooler.supabase.com:6543/postgres"
def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")

    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()