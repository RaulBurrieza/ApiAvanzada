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
import hashlib
import requests as rq
from fastapi.responses import RedirectResponse
import pandas as pd
import httpx
from fastapi import HTTPException
from fastapi import Depends

#Endpoint Supabase API
URL = "https://jpztuzgyiluqazttymmb.supabase.co"
#Public Key
KEY =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpwenR1emd5aWx1cWF6dHR5bW1iIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY4NTI4NTcsImV4cCI6MjAxMjQyODg1N30.R1ppxbGbX0pJ2rDysdlqdJ3QXiDvvjOtV-d5WuepWVQ"
#Creación cliente
sp: Client = create_client(URL,KEY)

conn = psyc.connect(host = "db.jpztuzgyiluqazttymmb.supabase.co",port="5432",database="postgres",user="postgres",password= "qlJb4WrwJc5UdzF1")
cur = conn.cursor()

Tablas = []

cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
for table in cur.fetchall():  
    Tablas.append(str(table).replace("'", "").replace(",", "").replace("(", "").replace(")", ""))