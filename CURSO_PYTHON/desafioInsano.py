print("Adivinhador de idade")
print(20*"=")
ano = input ("Digite o ano que você nasceu: ")
print(f"A sua idade é: {2024 - ano.isdigit}")

pergunta = input("Você gostaria de adivinhar outra idade? (S/N)")
if pergunta.lower() == 's':
    idade = input ("Digite o ano de nascimento: ")
    anos = int(idade)
    print(f"A sua idade é: {2024 - ano}")
elif pergunta.lower() == 'n':
    print("Tudo bem, não vou mais adivinhar pra vc :(")
else:
    print('Você não digitou S ou N')

print('Adivinhação encerrada')
 