# Idade em 2050

Programa em Python que pede informações do usuário e calcula quantos anos ele terá em 2050.  
Também mostra quantos anos faltam até 2050.

## Código principal
```python
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

O que foi aprendido

Variáveis (str, int, float, bool).
Entrada de dados com input().
Conversão de tipos (int() e float()).
Importação de módulos (import datetime).
Impressão formatada com f-strings.
Cálculos simples com datas.

Comentário pessoal

No Dia 2, já consegui criar um programa útil, que interage com o usuário.
Foi muito legal ver que em pouco tempo já dá para fazer algo prático e inteligente, usando datas reais e cálculos automáticos.
