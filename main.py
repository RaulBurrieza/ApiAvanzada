import os
import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import supabase as sp
from supabase import create_client, Client
import psycopg2 as psyc
import uvicorn as uvi
import asyncio
import json
import hashlib as hlb
import requests as rq
from fastapi.responses import RedirectResponse

#Modelos
class Usuario(BaseModel):
    id:Optional[str]
    NombreUsu:Optional[str]
    Contraseña:Optional[str]

class infoUsuario(BaseModel):
    Nombre:str
    Email:str
    Telefono:str
    Fecha_nacimiento:str
     
app = FastAPI(
    title="Api Avanzada"
)


#Conexiones
URL = "https://jpztuzgyiluqazttymmb.supabase.co"
KEY =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpwenR1emd5aWx1cWF6dHR5bW1iIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY4NTI4NTcsImV4cCI6MjAxMjQyODg1N30.R1ppxbGbX0pJ2rDysdlqdJ3QXiDvvjOtV-d5WuepWVQ"
sp: Client = create_client(URL,KEY)
conn = psyc.connect(host = "db.jpztuzgyiluqazttymmb.supabase.co",port="5432",database="postgres",user="postgres",password= "qlJb4WrwJc5UdzF1")
cur = conn.cursor()
Tables = []
cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
for table in cur.fetchall():  
    Tables.append(str(table).replace("'", "").replace(",", "").replace("(", "").replace(")", ""))
       
def initUvicorn():
    async def main():
        config = uvi.Config("main:app", port=5000, log_level="info")
        server = uvi.Server(config)
        await server.serve()

    if __name__ == "__main__":
        asyncio.run(main())
             
      
    @app.get('/', include_in_schema=False)
    async def docs_redirect():
        response = RedirectResponse(url='/docs')
        return response

    #operaciones GET

    @app.get('/tables')
    def getTables():
        return Tables
    
    @app.get('/tables/{id}')
    def getTablaInfo(id:int):
            data = sp.table(Tables[id]).select("*").execute()
            tableInfo = data.model_dump_json()
            jsonUsers = json.loads(tableInfo)
            return jsonUsers
    
    @app.get('/usuarios')
    def getUser():
        data = sp.table('cuenta').select("*").execute()
        tableInfo = data.model_dump_json()
        jsonUsers = json.loads(tableInfo)
        return jsonUsers
    
    @app.get('/usuarios/{id}')
    def getUser(id:int):
            data = sp.table('infousuario').select("*").execute()
            tableInfo = data.model_dump_json()
            jsonUser = json.loads(tableInfo)
            return jsonUser
            
        
    #operaciones POST
   

    
initUvicorn()