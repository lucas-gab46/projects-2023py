def altura_alta(altura):
    return altura >= 170

def altura_baixa(altura):
    return altura < 160

print('Olá, qual é seu nome?')
nome = input()

print('Que nome bonito,', nome)

print(nome, 'Qual é sua altura em centímetros?')
altura = float(input())

if altura_alta(altura):
    print('Que bacana,', nome + ', com', altura, 'cm você é considerado uma pessoa alta!')
elif altura_baixa(altura):
    print('Que bacana,', nome + ', com', altura, 'cm você é considerado uma pessoa baixa!')
else:
    print('Que bacana,', nome + ', com', altura, 'cm você tem uma altura média!')

