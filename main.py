from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()
comodo = Comodo(input('Qual a largura do cômodo? '), input("Qual a profundidade do cômodo? "))

print('A area das parede é:', calc.calcular_area_parede(comodo))
print('Area do teto é:', calc.calcula_area_teto(comodo))
print('A litragem de tinta nescessaria é:', calc.calcular_litragem_necessaria())