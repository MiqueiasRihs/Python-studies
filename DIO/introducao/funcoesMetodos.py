class Calculadora:
    def soma(self, valor_a, valor_b):
        return valor_a+valor_b
    
    def subtra(self, valor_a, valor_b):
        return valor_a-valor_b
    
    def multipli(self, valor_a, valor_b):
        return valor_a*valor_b
    
    def divisao(self, valor_a, valor_b):
        return valor_a/valor_b
    
calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtra(5, 3))
print(calculadora.multipli(100, 2))
print(calculadora.divisao(10, 5))
