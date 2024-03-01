"""def operaciones():
    print("\n1. Operaciones: ")
    print("2. Salir del programa: ")
    opcion = int(input("Ingrese una opción: "))

    while True: 
        if opcion == 2:
            break
        elif opcion == 1:
            while True:
                print("\nBienvenido a las operaciones de tu cuenta: ")
                print("1. Depositar")
                print("2. Retirar")
                print("3. Mostrar saldo")
                print("4. Salir del programa")
                op = int(input("Ingrese una opción: "))

                if op == 1:
                    cuenta1.depositar(500)
                elif op == 2:
                    pass
                elif op == 3:
                    pass
                elif op == 4:
                    print("Gracias por participar!")
                    break
                else:
                    print("ERROR: Ingrese un valor correcto.")
        else:
            print("Ingrese el 1 o el 2")

# Ejecución de métodos
cuenta1 = Cuenta_bancaria("123456789", "Juan Pérez", 1000)
numero_cuenta1 = cuenta1.numero_cuenta
titular_cuenta1 = cuenta1.titular
saldo_cuenta1 = cuenta1.saldo

cuenta2 = Cuenta_bancaria("987654321", "María López", 500)
numero_cuenta2 = cuenta2.numero_cuenta
titular_cuenta2 = cuenta2.titular
saldo_cuenta2 = cuenta2.saldo

print("Bienvenido/a! ")
cuenta = input("Ingrese su número de cuenta: ")

if cuenta == numero_cuenta1 :
    print("Tus datos son: \n")
    print(f"Tu nombre es: {titular_cuenta1}")
    print(f"Tu número de cuenta es: {numero_cuenta1}")
    print(f"Tu saldo es: {saldo_cuenta1}")
    operaciones()
    
else:
    print("Tus datos son: \n")
    print(f"Tu nombre es: {titular_cuenta2}")
    print(f"Tu número de cuenta es: {numero_cuenta2}")
    print(f"Tu saldo es: {saldo_cuenta2}")
    operaciones()

#sum: Establecer métodos de la clase principal y arreglar menú de operaciones"""