idade = 0
anoTrabalho = 0

idade = int(input("digite a sua idade: "))
anoTrabalho = int(input("digite quantos anos voce trabalhou: "))

if idade >= 65:
    print("pode se aposentar")
elif anoTrabalho >= 30:
    print("pode se aposentar")
elif idade >= 60 and anoTrabalho >= 25:
    print("pode se aposentar")
else:
    print("nao pode se aposentar")


