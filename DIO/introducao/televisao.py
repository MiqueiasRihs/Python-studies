class Televisao:
    def __init__(self):
        self.ligada = False
    
    def power(self):
        if self.ligada:
            self.ligada == False
        else:
            self.ligada == True

    def aumenta_canal(self):
        self.canal += 1
    
    def diminui_canal(self):
        self.canal -= 1
    

televisao = Televisao()
print('Televisão está ligada: {}' .format(televisao.ligada))
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

print('canal: {}'.format(televisao.canal))