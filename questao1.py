maior, contador = 1, 1
numero = int(input("Informe um número: "))

while contador < 3:
     numero = int(input("Informe um número: "))
     contador += 1
     if numero > maior:
         maior = numero
print(maior)