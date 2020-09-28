from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Dente de Sabre', idade=57)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Wolverine').first()

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Wolverine').first()
    pessoa.nome = 'Dente de Sabre'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Dente de Sabre').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == "__main__":
    insere_usuario('miqueias', '1234')
    insere_usuario('tempestade', '4321')

    consulta_todos_usuarios()
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()