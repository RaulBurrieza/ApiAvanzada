from utils import *
from models import *
import utils

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

if utils.UsuarioRol in ('Reader', 'Admin'):
    @app.get('/tables/{id}')
    def getTablaInfo(id: int):
        if id < 0 or id >= len(Tablas):
            raise HTTPException(status_code=404, detail="Tabla no encontrada")
        try:
            data = sp.table(Tablas[id]).select("*").execute()
            tableInfo = data.model_dump_json()
            jsonUsers = json.loads(tableInfo)
            return jsonUsers
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener información de la tabla: {e}")

if utils.UsuarioRol in ('Admin'):   
    #operaciones POST
    @app.post('/usuarios')
    def createUser(user: User, userInfo: userInfo):
        try:
            userInfo_insert = sp.from_('infoUsuarios')\
                        .insert({"Nombre": userInfo.name, "Email": userInfo.email, "Telefono": userInfo.phoneNum, "Fecha_nacimiento": userInfo.Date})\
                        .execute()
            
            user_insert = sp.from_('Usuarios')\
                .insert({"NombreUsu": user.userName, "Contraseña": user.password})\
                .execute()

            return {"message": "Usuario y su información creados correctamente"}
        except Exception as e:
            return {"error": f"No se pudo crear el usuario: {e}"}

    @app.post("/cancion")         
    def createSong(song: Song):
        try:
            song_insert = sp.from_('cancion')\
                .insert({"id_cancion": song.id, "Nombre": song.name, "Genero": song.genre, "Artista": song.artist, "Album": song.album })\
                .execute()

            return {"message": "Canción creada correctamente"}
        except Exception as e:
            return {"error": f"No se pudo crear la canción: {e}"}

    @app.post('/post')
    def createPost(post: Post):
        try:
            post_insert = sp.from_('post')\
                .insert({"Nombre_Usu": post.userName, "id_cancion": post.song_id})\
                .execute()

            return {"message": "Publicación creada correctamente"}
        except Exception as e:
            return {"error": f"No se pudo crear la publicación: {e}"}
                
        
    #operaciones delete
    @app.delete('/usuarios/{user_name}')
    def deleteUser(user_name: str):
        try:
            sp.from_('Usuarios').delete().eq('NombreUsu', user_name).execute()
            sp.from_('infoUsuarios').delete().eq('Nombre', user_name).execute()

            return {"message": f"Usuario '{user_name}' y su información han sido eliminados correctamente"}
        except Exception as e:
            return {"error": f"No se pudo eliminar el usuario: {e}"}
        
   
    @app.delete('/cancion/{song_id}')
    def deleteSong(song_id: str):
        try:
            sp.from_("cancion").delete().eq("id_cancion", song_id).execute()
                
            return {"message": "Canción borrada correctamente"}
        except Exception as e:
            return {f"error: {e}"}


    @app.delete('/post/{nombre_usu}')
    def deletePost(nombre_usu: str):
        try:
            sp.from_("post")\
                        .delete().eq("Nombre_Usu", nombre_usu)\
                        .execute()   
            return {f"Publicación eliminada con exito"}
        except Exception as e:
            return {f"error: {e}"}
                    
    #operaciones Update               
@app.put('/usuarios/{user_name}')
def updateUser(user_name: str, user: User, userInfo: userInfo):
    try:
        # Actualizar información en la tabla 'infoUsuarios'
        updated_info = sp.from_("infoUsuarios")\
            .update({"Email": userInfo.email, "Telefono": userInfo.phoneNum, "Fecha_nacimiento": userInfo.Date})\
            .eq("Nombre", user_name).execute()
        
        # Actualizar información en la tabla 'Usuarios'
        updated_user = sp.from_("Usuarios")\
            .update({"Contraseña": user.password })\
            .eq("NombreUsu", user_name).execute()
        
        return {"message": "Usuario y su información actualizados correctamente"}
    except Exception as e:
        return {"error": f"No se pudo actualizar el usuario y su información: {str(e)}"}
