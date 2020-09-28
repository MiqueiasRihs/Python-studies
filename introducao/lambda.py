contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))


soma = lambda a, b: a + b 
subtra = lambda a, b: a - b 

print(soma(5, 10))
print(subtra(5, 10))


calculadora = {
    'sum': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multipli': lambda a, b: a * b,
    'divi': lambda a, b: a / b
}

soma = calculadora['sum']
subtra = calculadora['subtracao']

print(soma(2, 1))
print(subtra(5, 1))