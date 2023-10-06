#calculadora 1.1
class calculadora:
    def __init__ (self):
        self.valor_uno = 0
        self.valor_dos = 0
    
    def ingreso_de_valores(self):
        self.valor_uno = int(input('ingrese el primer numero entero que a de ser operado: '))
        self.valor_dos = int(input('ingrese el segundo numero entero que a de ser operado: '))

    def suma(self):
        return self.valor_uno + self.valor_dos

    def resta(self):
        return self.valor_uno - self.valor_dos

    def multiplicacion(self):
        return self.valor_uno * self.valor_dos
    
    def division(self):
        if self.valor_dos <= 1:
            return 'no se puede dividir entre cero'
        else:
            return self.valor_uno / self.valor_dos
        
la_calculadora = calculadora()

la_calculadora.ingreso_de_valores()

print('la suma de los dos numeros es =', la_calculadora.suma())
print('la resta de los dos numeros es =', la_calculadora.resta())
print('la multiplicacion de los dos numeros es =', la_calculadora.multiplicacion())
print('la division de los dos numeros es =', la_calculadora.division())
