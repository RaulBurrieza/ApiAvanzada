from utils import *
from models import *
     
app = FastAPI(
    title="Api Avanzada"
)
   
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
    jsonTables = json.loads(tableInfo)
    return jsonTables


@app.get('/usuarios')
def getTablaInfo():
    data = sp.table('Usuarios').select("*").execute()
    userInfo = data.model_dump_json()
    jsonUsers = json.loads(userInfo)
    return jsonUsers

@app.get('/usuarios/{id}')
def getTablaInfo(id:int):
    data = sp.table(Tablas[id]).select("*").execute()
    userInfo = data.model_dump_json()
    jsonUsers = json.loads(userInfo)
    return jsonUsers


@app.get('/infousuarios')
def getTablaInfo():
    data = sp.table('infoUsuarios').select("*").execute()
    userInfo = data.model_dump_json()
    jsonUsers = json.loads(userInfo)
    return jsonUsers

@app.get('/infousuarios/{id}')
def getTablaInfo(id:int):
    data = sp.table('infoUsuarios').select("*").execute()
    userInfo = data.model_dump_json()
    jsonUsers = json.loads(userInfo)
    return jsonUsers


@app.get('/cancion')
def getTablaInfo():
    data = sp.table('cancion').select("*").execute()
    tableInfo = data.model_dump_json()
    jsonUsers = json.loads(tableInfo)
    return jsonUsers

@app.get('/cancion/{id}')
def getTablaInfo(id:int):
    data = sp.table(Tablas[id]).select("*").execute()
    tableInfo = data.model_dump_json()
    jsonUsers = json.loads(tableInfo)
    return jsonUsers


@app.get('/post/')
def getTablaInfo():
    data = sp.table('post').select("*").execute()
    tableInfo = data.model_dump_json()
    jsonUsers = json.loads(tableInfo)
    return jsonUsers

@app.get('/post/{id}')
def getTablaInfo(id:int):
    data = sp.table(Tablas[id]).select("*").execute()
    tableInfo = data.model_dump_json()
    jsonUsers = json.loads(tableInfo)
    return jsonUsers
def getTablaInfo(id: int):
    if id < 0 or id >= len(Tablas):
        raise HTTPException(status_code=404, detail="Tabla no encontrada")

    try:
        data = sp.table(Tablas[id]).select("*").execute()
        tableInfo = data.model_dump_json()
        jsonUsers = json.loads(tableInfo)
        return jsonUsers
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al obtener información de la tabla")

  
#operaciones POST

@app.post('/usuarios')
def createUser(user:User):
    user = sp.from_('Usuarios')\
            .insert({"id": user.id, "Contraseña": user.email, "NombreUsu": user.name })\
            .execute()
            

@app.post('/infousuarios')
def createUserInfo(userInfo:userInfo):
    userInfo = sp.from_('infoUsuarios')\
            .insert({"Nombre": userInfo.name, "Email": userInfo.email, "Telefono": userInfo.phoneNum })\
            .execute()


@app.post('/cancion')
def createSong(song:Song):
    song = sp.from_('cancion')\
            .insert({"id_cancion": song.id, "Nombre": song.id, "Genero": song.genre, "Artista": song.artist, "Album": song.album })\
            .execute()


@app.post('/post')
def createPost(post:Post):
    post = sp.from_('post')\
            .insert({"Nombre_Usu": post.userName, "id_cancion": post.song_id})\
            .execute()
            
       
#operaciones delete

@app.delete('/usuarios')
def deleteUser(user:User):
    user = sp.from_("Usuarios")\
                .delete().eq("id", user.id)\
                .execute()

@app.delete('/infousuarios')
def deleteUserInfo(userInfo:userInfo):
    userInfo = sp.from_("infoUsuarios")\
                .delete().eq("Nombre", userInfo.name)\
                .execute()


@app.delete('/cancion')
def deleteSong(song:Song):
    song = sp.from_("cancion")\
                .delete().eq("id_cancion", song.id)\
                .execute()


@app.delete('/post')
def deletePost(post:Post):
    post = sp.from_("post")\
                .delete().eq("Nombre_Usu", post.userName)\
                .execute()
                
 #operaciones Update               
@app.put('/usuarios')
def deleteUser(user:User):
    user = sp.from_("users")\
                .update({"id": user.id, "Contraseña": user.email, "NombreUsu": user.name })\
                .eq("id", user.id).execute()

@app.put('/infousuarios')
def deleteUserInfo(userInfo:userInfo):
    userInfo = sp.from_("users")\
                .update({"Nombre": userInfo.name, "Email": userInfo.email, "Telefono": userInfo.phoneNum })\
                .eq("Nombre", userInfo.id).execute()


@app.put('/cancion')
def deleteSong(song:Song):
    song = sp.from_("users")\
                .update({"id_cancion": song.id, "Nombre": song.id, "Genero": song.genre, "Artista": song.artist, "Album": song.album })\
                .eq("id_cancion", song.id).execute()


@app.put('/post')
def updatePost(post:Post):
    post = sp.from_("users")\
                .update({"Nombre_Usu": post.userName, "id_cancion": post.song_id})\
                .eq("Nombre_Usu", post.userName).execute()