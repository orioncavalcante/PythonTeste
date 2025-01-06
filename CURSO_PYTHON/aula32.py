"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero = input("Digite um número inteiro: ")
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é ímpar")

except:
    print("Escreva um número inteiro")

print(50*"=")
print("\n")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input("Digite a hora: ")
horario_int = int(horario)

if horario_int >= 0 and horario_int <= 11:
    print(f"Bom dia, agora são {horario_int} horas")
elif horario_int >= 12 and horario_int <= 17:
    print(f"Boa tarde, agora são {horario_int} horas")
elif horario_int >= 18 and horario_int <= 23:
    print(f"Boa noite, agora são {horario_int} horas")

print(50*"=")
print("\n")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva
"""
nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto")
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print("Seu nome é normal")
elif tamanho_nome > 6:
    print("Seu nome é muito grande")
