class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo = codigo

class Reserva:
    def __init__(self, cliente, coches, fecha_inicio, fecha_final):
        self.cliente = cliente
        self.coches = coches
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

# Solicitar datos al usuario
dni = input("Ingrese el DNI del cliente: ")
nombre = input("Ingrese el nombre del cliente: ")
direccion = input("Ingrese la dirección del cliente: ")
telefono = input("Ingrese el teléfono del cliente: ")
codigo = input("Ingrese el código único del cliente: ")

matricula = input("Ingrese la matrícula del coche: ")
modelo = input("Ingrese el modelo del coche: ")
color = input("Ingrese el color del coche: ")
marca = input("Ingrese la marca del coche: ")
garaje = input("Ingrese el garaje asignado al coche: ")

fecha_inicio = input("Ingrese la fecha de inicio de la reserva: ")
fecha_final = input("Ingrese la fecha de finalización de la reserva: ")

# Crear objetos con los datos ingresados por el usuario
cliente1 = Cliente(dni, nombre, direccion, telefono, codigo)
coche1 = Coche(matricula, modelo, color, marca, garaje)
coches_reserva = [coche1]
reserva1 = Reserva(cliente1, coches_reserva, fecha_inicio, fecha_final)

# Imprimir información de la reserva
print("Reserva de", reserva1.cliente.nombre)
print("Fecha de inicio:", reserva1.fecha_inicio)
print("Fecha final:", reserva1.fecha_final)
print("Coches reservados:")
for coche in reserva1.coches:
    print(coche.marca, coche.modelo, "(", coche.matricula, ")")