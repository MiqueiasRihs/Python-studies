from datetime import date, time, datetime, tim

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.hour)
    print(data_atual.date())
    print(data_atual.weekday())
    
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada.strftime('%c'))

    # Transformando data string para date
    data_str = '01/01/2019'
    data_convertida = datetime.strptime(data_str, '%d/%m/%Y')
    print('Data convertida = {}' .format(data_convertida))
    print('Weekday da Data convertida = {}' .format(data_convertida.weekday()))



def trabalhando_Date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y \n'))
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_Time():
    horario = time(hour=15, minute=10, second=30)
    print(horario.strftime('%H:%M:%S'))





if __name__ == "__main__":
    # trabalhando_Date()
    # trabalhando_Time()
    trabalhando_datetime()
