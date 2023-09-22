class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria, subordinados):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = subordinados

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono):
        super().__init__(nombre, edad)
        self.telefono = telefono

# Solicitar nombre de la empresa
nombre_empresa = input("Ingrese el nombre de la empresa: ")
empresa = Empresa(nombre_empresa)

# Solicitar datos de empleados
num_empleados = int(input("Ingrese el número de empleados: "))

for i in range(num_empleados):
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    edad_empleado = int(input("Ingrese la edad del empleado: "))
    sueldo_bruto = float(input("Ingrese el sueldo bruto del empleado: "))

    empleado = Empleado(nombre_empleado, edad_empleado, sueldo_bruto)
    empresa.empleados.append(empleado)

# Solicitar datos del directivo
nombre_directivo = input("Ingrese el nombre del directivo: ")
edad_directivo = int(input("Ingrese la edad del directivo: "))
sueldo_bruto_directivo = float(input("Ingrese el sueldo bruto del directivo: "))
categoria_directivo = input("Ingrese la categoría del directivo: ")

num_subordinados = int(input("Ingrese el número de subordinados del directivo: "))

subordinados = []
for i in range(num_subordinados):
    nombre_subordinado = input("Ingrese el nombre del subordinado: ")
    edad_subordinado = int(input("Ingrese la edad del subordinado: "))
    sueldo_bruto_subordinado = float(input("Ingrese el sueldo bruto del subordinado: "))

    subordinado = Empleado(nombre_subordinado, edad_subordinado, sueldo_bruto_subordinado)
    subordinados.append(subordinado)

directivo = Directivo(nombre_directivo, edad_directivo, sueldo_bruto_directivo, categoria_directivo, subordinados)
empresa.empleados.append(directivo)

# Solicitar datos de clientes
num_clientes = int(input("Ingrese el número de clientes: "))

for i in range(num_clientes):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    edad_cliente = int(input("Ingrese la edad del cliente: "))
    telefono_cliente = input("Ingrese el teléfono del cliente: ")

    cliente = Cliente(nombre_cliente, edad_cliente, telefono_cliente)
    empresa.clientes.append(cliente)

# Mostrar los datos de empleados y clientes
print("Datos de empleados:")
for empleado in empresa.empleados:
    print("Nombre:", empleado.nombre)
    print("Edad:", empleado.edad)
    print("Sueldo bruto:", empleado.sueldo_bruto)
    if isinstance(empleado, Directivo):
        print("Categoría:", empleado.categoria)
        print("Subordinados:")
        for subordinado in empleado.subordinados:
            print("-", subordinado.nombre)
    print()

print("Datos de clientes:")
for cliente in empresa.clientes:
    print("Nombre:", cliente.nombre)
    print("Edad:", cliente.edad)
    print("Teléfono:", cliente.telefono)
    print()
