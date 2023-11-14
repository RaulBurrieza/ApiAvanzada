from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import supabase as sp
from supabase import create_client, Client
import psycopg2 as psyc
import uvicorn as uvi
import asyncio

#Modelos
class User(BaseModel):
    id:Optional[str]
    name:Optional[str]
    password:Optional[str]
    
app = FastAPI(
    title="Api Avanzada"
)
#Conexiones
URL = "https://jpztuzgyiluqazttymmb.supabase.co"
KEY =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpwenR1emd5aWx1cWF6dHR5bW1iIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY4NTI4NTcsImV4cCI6MjAxMjQyODg1N30.R1ppxbGbX0pJ2rDysdlqdJ3QXiDvvjOtV-d5WuepWVQ"
sp: Client = create_client(URL,KEY)
conn = psyc.connect(host = "db.jpztuzgyiluqazttymmb.supabase.co",port="5432",database="postgres",user="postgres",password= "qlJb4WrwJc5UdzF1")
cur = conn.cursor()
Tablas = []

cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
for table in cur.fetchall():  
    print(table)
    Tablas.append(str(table).replace("'", "").replace(",", "").replace("(", "").replace(")", "")) 

async def main():
    config = uvi.Config("main:app", port=5000, log_level="info")
    server = uvi.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())

#CRUD
@app.get('/')
def greeting():
    return "hola"

@app.get('/tables')
def getTables():
    return Tablas

@app.get('/users')
def getUsers():
    
    return "hola"