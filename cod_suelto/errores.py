# Clase que hereda de exception
class ContrasenaDebilError(Exception):
    def __init__(self, mensaje="La contraseña proporcionada es débil."):
        super().__init__(mensaje)

# Función para verificar la contraseña con la clase
def verificar_contrasena(contrasena):
    if len(contrasena) < 8:
        raise ContrasenaDebilError("La contraseña debe tener al menos 8 caracteres.")
    
while True:
    try:
        password = input("Ingrese su contrasena: ")
        contrasena = password
        verificar_contrasena(contrasena)
        print("Contraseña Valida")
        break
    except ContrasenaDebilError as e:
        print("Error de contraseña:", e)

class EmailInvalido(Exception):
    def __init__(self, mensajeError="Email invalido"):
        super().__init__(mensajeError)

def verificar_email(ingreseEmail):
    if "@gmail.com" in ingreseEmail:
        print("Email valido")
    else:
        raise EmailInvalido()

while True:
    try:
        ingreseEmail = input("Ingrese su Email: ")
        verificar_email(ingreseEmail)
        break
    except EmailInvalido as e:
        print("Tipo de Error: ", e)

class Usuario:
    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

crearNombre = input("Ingrese su nombre: ")

usuario = Usuario(crearNombre, ingreseEmail, contrasena)
listaUsuario = []
listaUsuario.append(usuario)

opcion = int(input("quiere ver el usuario registrado 1-Ver 2-Salir: "))

if opcion == 1:
    nombreUsuario = input("Ingrese el nombre del usuario a ver: ")
    existe = False
    for usuario in listaUsuario:
        if usuario.nombre == nombreUsuario:
            existe = True
            usuarioEncontrado = usuario
    if existe == True:
        contador = 0
        intentos = 0
        while contador < 3:
            contrasenaUsuario = input(f"Ingrese contrasena del usuario a ver intento {contador + 1}: ")
            if usuarioEncontrado.contrasena == contrasenaUsuario:
                print(f"Datos del Usuario {usuarioEncontrado.nombre} {usuarioEncontrado.email} {usuarioEncontrado.contrasena}")
            else:
                print("contrasena incorrecta")
                intentos += 1
            contador += 1
        if intentos == 3:
            print("Usuario Bloqueado")
elif opcion ==2:
    pass
else:
    print("Opcion incorrecta")
