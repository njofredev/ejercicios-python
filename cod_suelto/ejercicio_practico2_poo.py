"""
Ejercicio práctico - Lección 2 n°2
njofre

- Crear una clase llamada "Cuenta bancaria"
    - Atributos: numero_cuenta, titular, saldo
    - Métodos: depositar(), retirar(), mostrar_saldo()

- Crear dos instancias de la clase "cuenta_bancaria"

cuenta1 = CuentaBancaria("123456789", "Juan Pérez", 1000)
cuenta2 = CuentaBancaria("987654321", "María López", 500)

- Realizar las siguientes operaciones: 
    - Depositar 500 euros en la cuenta 1.
    - Retirar 200 euros en la cuenta 2.
    - Mostrar el saldo en ambas cuentas
"""
# Clase cuenta bancaria
class Cuenta_bancaria:

    def __init__ (self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad ):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print ("No tiene saldo ")

    def mostrar_saldo (self):
        print(f"El saldo de {self.titular} es: {self.saldo}")

# Instancias de la clase
cuenta1 = Cuenta_bancaria("123456789", "Juan Pérez", 1000)
cuenta2 = Cuenta_bancaria("987654321", "María López", 500)

# Operaciones
# Datos de inicio
print(f"Los datos de inicio de la cuenta 1 son: Cuenta: {cuenta1.numero_cuenta}, nombre titular: {cuenta1.titular}, saldo de cuenta: {cuenta1.saldo}")
print(f"Los datos de inicio de la cuenta 2 son: Cuenta: {cuenta2.numero_cuenta}, nombre titular: {cuenta2.titular}, saldo de cuenta: {cuenta2.saldo} \n")

# Deposito
print("Se depositan $500 euros en la cuenta1")
cuenta1.depositar(500)

# Retiro
print("Se retiran $200 euros de la cuenta 2\n")
cuenta2.retirar(200)

# Se muestran los saldos
print("Se muestran los saldos actuales de la cuenta 1 y 2\n")
cuenta1.mostrar_saldo()
cuenta2.mostrar_saldo()