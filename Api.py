from utils import *

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


cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
for table in cur.fetchall():  
    Tablas.append(str(table).replace("'", "").replace(",", "").replace("(", "").replace(")", ""))

     
#operaciones GET 
@app.get('/', include_in_schema=False)
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

@app.get('/tables')
def getTables():
    return Tablas

@app.get('/tables/{id}')
def getTablaInfo(id:int):
    data = sp.table(Tablas[id]).select("*").execute()
    tableInfo = data.model_dump_json()
    jsonUsers = json.loads(tableInfo)
    return jsonUsers

  
#operaciones POST