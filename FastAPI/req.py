import requests

retorno = requests.get("http://127.0.0.1:8000/usuario", params={"id": 4, "nome": "roberta", "senha": "minhasenha4"})

print(type(retorno.json()))

#print(retorno.json()['mensagem'])

