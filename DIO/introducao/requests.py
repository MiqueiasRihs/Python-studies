from requests import *

def retorna_dados(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    print(response.json())

    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api1/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response("https://globallabs.academy/")
    print(response)
    # retorna_dados_cep('32183180')
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon)