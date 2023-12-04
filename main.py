from utils import *

def create_Table():
    nombreTabla = input("Introduzca el nombre de la tabla: ")
    cantColumns = input("¿Cuantas columnas quieres meter?")
    
    Columnas = []
    
    for i in range(int(cantColumns)):
        print("Columna " + str(i))
        if i == 0:
            nombreColumna = input("Introduzca el nombre de la Primary Key: ")
            Columna = (nombreColumna + " SERIAL PRIMARY KEY")    
        else:
            nombreColumna = input("Introduzca el nombre de la columna ")
            TipoDato = input("Introduzca el tipo de dato de la columna ")
            Columna = (nombreColumna + " " + TipoDato) 

        Columnas.append(Columna)
       
    cur.execute("CREATE TABLE " + nombreTabla + str(tuple(Columnas)).replace("'", "") + ";")
    conn.commit()
    
def delete_Table():
    show_Tables()
    nombreTabla = input("Introduzca el nombre de la tabla que quiere borrar: ")
    cur.execute("DROP TABLE " + nombreTabla + ";")
    
def show_Tables():
    count = 1
    print("######\nTablas\n#####")
    for Tabla in Tablas:
        print(str(count) + ". " +  Tabla)
        count = count + 1
        
        
def sign_up(User, Password):
    print("#####\nRegister\n#####")
    usuario = sp.auth.sign_up({"email": User ,"password": Password})
    print(usuario)
    
 
def sign_in(User, Password):
    print("#####\nLOGIN\n#####")
    usuario = sp.auth.sign_in_with_password({"email": User, "password": Password})
    print(usuario)
    

print("""Bienvenido!!!""")

elec = input("""  
¿Qué quiere hacer?            
###########################################
    1. Logarse con un ususario de la BD
    2. Registrarse en la BD
###########################################      
""")

if elec == 1:
    User = input("Nombre de usuario: ")
    Password = input("Contraseña: ")
    sign_in(User, Password)
    
elif elec == 2:
    User = input("Nombre Usuario: ")
    Password = input("Contraseña: ")
    sign_up()

  
#Selección Operacion a realizar    
elec = input("""  
¿Qué quiere hacer?            
###########################################
    1. Iniciar FastApi
    2. Crear Tabla 
    3. Borrar Tabla
    4. Gestionar Roles
    5. Crear Usuarios para la base de Datos
###########################################      
""")


if elec == '1':
    async def main():
        config = uvi.Config("Api:app", port=5000, log_level="info")
        server = uvi.Server(config)
        await server.serve()

    if __name__ == "__main__":
        asyncio.run(main())
        
if elec == '2':
    create_Table()

if elec == '3':
    delete_Table()
    
if elec == '4':
    print("Desarrollo")

if elec == '5':
    print("Desarrollo")
