from utils import *

#Funciones

#Crear Tabla
def create_Table():
    nombreTabla = input("Introduzca el nombre de la tabla: ")
    cantColumns = input("¿Cuantas columnas quieres meter? ")

    try:
        cantColumns = int(cantColumns)
    except ValueError:
        print("Por favor, ingrese un número válido para la cantidad de columnas.")
        return

    Columnas = []

    for i in range(cantColumns):
        print("Columna " + str(i))
        if i == 0:
            nombreColumna = input("Introduzca el nombre de la Primary Key: ")
            Columna = (nombreColumna + " SERIAL PRIMARY KEY")
        else:
            nombreColumna = input("Introduzca el nombre de la columna ")
            TipoDato = input("Introduzca el tipo de dato de la columna ")
            Columna = (nombreColumna + " " + TipoDato)

        Columnas.append(Columna)

    try:
        cur.execute("CREATE TABLE " + nombreTabla + str(tuple(Columnas)).replace("'", "") + ";")
        conn.commit()
        print("Tabla creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

#Borrar Tabla
def delete_Table():
    show_Tables()
    nombreTabla = input("Introduzca el nombre de la tabla que quiere borrar: ")

    try:
        cur.execute("DROP TABLE IF EXISTS " + nombreTabla + ";")
        conn.commit()
        print("Tabla eliminada exitosamente.")
    except Exception as e:
        print(f"Error al eliminar la tabla: {e}")


#Mostrar Tablas
def show_Tables():
    print("######\nTablas\n#####")
    for tabla in Tablas:
        print(tabla)

#Registrarase en la API de supabase
def sign_up(User, Password):
    print("#####\nRegister Suapabase API\n#####")
    try:
        usuario = sp.auth.sign_up({"email": User + "@gmail.com", "password": Password})
        print("Usuario registrado exitosamente.")
        return usuario
    except Exception as e:
        print(f"Error al registrar el usuario: {e}")
        return None

#Logarse en la API de supabase
def sign_in(User, Password):
    print("#####\nLOGIN Supabase API\n#####")
    try:
        usuario = sp.auth.sign_in_with_password({"email": User + "@gmail.com", "password": Password})
        print("Inicio de sesión exitoso.")
        return usuario
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
     
#Logarse en la BD
def login(Usuario, Password):
    print("#####\nLOGIN\n#####")
    try:
        Password = hashPassword(Password)
        print(Password)
        cur.execute(f"""SELECT rol FROM "Usuarios_BD" WHERE nombre = '{Usuario}' AND contraseña = '{Password}' """)
        rol = str(cur.fetchall())
        print(rol)
        return rol.replace("'", "").replace(",", "").replace("(", "").replace(")", "").replace("]", "").replace("[", "")
    except Exception as e:
        print(f"{e}")
        return ''
        
#Registrarse en la BD
def register(Usuario, Password):
    print("#####\nRegister\n#####")
    Password = hashPassword(Password)
    print(Password)
    try:
        cur.execute(f"""INSERT INTO "Usuarios_BD"(nombre,contraseña,rol) VALUES('{Usuario}', '{Password}', 'User'); """)
        conn.commit()
        print("Ejecutado")
    except Exception as e:
        print(f"{e}")
        return '' 

#Iniciar fastApi  
def initFastApi():
    async def main():
        config = uvi.Config("Api:app", port=5000, log_level="info")
        server = uvi.Server(config)
        await server.serve()

    if __name__ == "__main__":
        asyncio.run(main())
        
#Hashear contraseña
def hashPassword(password):
    hash_object = hashlib.md5(password.encode())
    return hash_object.hexdigest()

print("Bienvenido!!!")

elec_login = input("""            
1. Logarse
2. Registrarse                  
""")
if elec_login == '1':
    nombre = input("Nombre: ")
    password = input("Contraseña: ")
    UsuarioRol =  login(nombre, password)
    

<<<<<<< HEAD
if elec == '5':
    print("Desarrollo")
=======
if elec_login == '2':
    print("Al registrarte serás un usuario con privilegios básicos")
    nombre = input("Nombre: ")
    password = input("Contraseña: ")
    register(nombre, password)
    UsuarioRol = login(nombre, password)
        
if UsuarioRol == 'User' or UsuarioRol=='Admin' or UsuarioRol=='Reader':
    while True:
        elec = input("""  
        ¿Qué quiere hacer?            
        ###########################################
            1. Iniciar FastApi
            2. Realizar operaciones en la BD
            3. Salir
        ###########################################      
        """)

        if elec == '1' and (UsuarioRol == 'Usuario' or UsuarioRol == 'Admin'):
            elec_login = input("""  
            ¿Qué quiere hacer?            
            ###########################################
                1. Logarse en la API de supabase
                2. Registrarse en la API de supabase
                3. Volver
            ###########################################      
            """)

            if elec_login == '1':
                User = input("Nombre de usuario: ")
                Password = input("Contraseña: ")
                user_info = sign_in(User, Password)
                if user_info:
                    initFastApi()
                    
            if elec_login == '2':
                User = input("Nombre de usuario: ")
                Password = input("Contraseña: ")
                user_info = sign_up(User, Password)
                if user_info:
                    sign_in(User, Password)
                    
        if elec == '2':
            elec_BD = input(""" 
                    ¿Qué quieres hacer?
                    
                    1. Crear Tabla
                    2. Borrar Tabla
                    3. Gestionar Roles
                            """)
            
            if elec_BD == '1' and UsuarioRol == 'Admin':
                create_Table()

            elif elec_BD == '2' and UsuarioRol == 'Admin':
                delete_Table()

            elif elec_BD == '3':
                elec_roles = input("""  
                ¿Qué quiere hacer?            
                ###########################################
                    1. Ver roles
                    2. Crear un rol
                    3. Borrar un rol
                    4. Modificar un rol
                    5. Volver
                ###########################################      
                """)

                if elec_roles == '1':
                    print("ROLES: ")
                    cur.execute("""SELECT * FROM "Rol";""")
                    roles = cur.fetchall()
                    df = pd.DataFrame(roles,  columns=['rolname'])
                    print(df)

            
        elif elec == '3':
            break 

        else:
            print("Por favor, seleccione una opción válida.")
            
else:
    print("No puedes acceder")
>>>>>>> 86f76ad503b701b51d004702568d65c4156460cd
