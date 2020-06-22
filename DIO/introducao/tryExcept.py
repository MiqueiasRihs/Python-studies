lista = [1, 10]
arquivo = open('notas.txt', 'r')


try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possivel realizar divisao por 0')
except ArithmeticError:
    print('Houve um erro ao tentar realizar uma operacao aritmetica')
except IndexError:
    print("Erro ao acessar um indece invalido da lista")
except Exception as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando nao ocorre execao')

finally:
    print("Sempre executar")
    print('Fechando o arquivo')
    arquivo.close()
