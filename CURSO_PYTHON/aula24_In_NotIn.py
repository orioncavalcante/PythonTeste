#Operadores in e not in
#Strings são interáveis (Pode navegar item por item)
#  0 1 2 3 4 
#  O r i o n 
# -5-4-3-2-1

#nome = 'Orion'
#print(nome[2])
#print('ion' in nome)
#print('z' in nome)
#print(10 * '-')
#print('ion' not in nome)
#print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')