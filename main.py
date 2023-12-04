from utils import *

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
        print("Error al crear la tabla:", str(e))

    
def delete_Table():
    show_Tables()
    nombreTabla = input("Introduzca el nombre de la tabla que quiere borrar: ")

    try:
        cur.execute("DROP TABLE IF EXISTS " + nombreTabla + ";")
        conn.commit()
        print("Tabla eliminada exitosamente.")
    except Exception as e:
        print("Error al eliminar la tabla:", str(e))

def show_Tables():
    print("######\nTablas\n#####")
    for tabla in Tablas:
        print(tabla)


def sign_upApi(User, Password):
    print("#####\nRegister\n#####")
    try:
        usuario = sp.auth.sign_up({"email": User + "@gmail.com", "password": Password})
        print("Usuario registrado exitosamente.")
        return usuario
    except Exception as e:
        print("Error al registrar el usuario:", str(e))
        return None

def sign_inApi(User, Password):
    print("#####\nLOGIN\n#####")
    try:
        usuario = sp.auth.sign_in_with_password({"email": User + "@gmail.com", "password": Password})
        print("Inicio de sesión exitoso.")
        return usuario
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return None


print("Bienvenido!!!")

while True:
    elec = input("""  
    ¿Qué quiere hacer?            
    ###########################################
        1. Iniciar FastApi
        2. Crear Tabla 
        3. Borrar Tabla
        4. Gestionar Roles
        5. Salir
    ###########################################      
    """)

    if elec == '1':
        elec_login = input("""  
        ¿Qué quiere hacer?            
        ###########################################
            1. Logarse con un usuario de la API
            2. Registrarse en la API
            3. Volver
        ###########################################      
        """)

        if elec_login == '1':
            User = input("Nombre de usuario: ")
            Password = input("Contraseña: ")
            user_info = sign_inApi(User, Password)

            if user_info:
                config = uvi.Config("Api:app", port=5000, log_level="info")
                server = uvi.Server(config)
                uvi.start(server)

        elif elec_login == '2':
            User = input("Nombre Usuario: ")
            Password = input("Contraseña: ")
            user_info = sign_upApi(User, Password)

            if user_info:
                sign_inApi(User, Password)

    elif elec == '2':
        create_Table()

    elif elec == '3':
        delete_Table()

    elif elec == '4':
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
            cur.execute("SELECT * FROM pg_roles;")
            roles = cur.fetchall()
            df = pd.DataFrame(roles,  columns=['rolname', 'rolsuper', 'rolinherit', 'rolcreaterole', 
                                            'rolcreatedb', 'rolcanlogin', 'rolreplication', 'rolconnlimit', 
                                            'rolpassword', 'rolvaliduntil', 'rolbypassrls', 'rolconfig','oid'])
            print(df)

    elif elec == '5':
        break 

    else:
        print("Por favor, seleccione una opción válida.")