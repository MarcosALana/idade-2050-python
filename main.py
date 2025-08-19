import datetime

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano_atual = datetime.datetime.now().year
faltam = 2050 - ano_atual
idade2050 = idade + faltam
altura = float(input("Digite sua altura: "))
cidade = input("Digite sua cidade: ")

print(f"Olá {nome}! Hoje você tem {idade} anos, mede {altura:.2f}m e mora em {cidade}.")
print(f"Em 2050 você terá {idade2050} anos de idade.")
print(f"Faltam {faltam} anos para 2050.")
