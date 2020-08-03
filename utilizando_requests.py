import requests


def retorna_dados_cep(cep):

    response = requests.get('http://viacep.com.br/ws/22041001/json/'.format(cep)) #busca dados em um endereço informado

    print(response.status_code)
    print(response.text) #Retorna os dados com string
    dados_cep = response.json()  # Retorna os dados como um dict para manipula-los
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])

    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url) 
    return response.text


if __name__ == '__main__':
    response = retorna_response('https://web.digitalinnovation.one/home')
    print(response)  # retorna o html da url
    #retorna_dados_cep('22041001')
    #dados_pokemon = retorna_dados_pokemon('charmander')
    #print(dados_pokemon)


    
    

    
