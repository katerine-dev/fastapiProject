import requests

retorno = requests.get("http://127.0.0.1:8000/usuarios", params={"nome": "caio"})

print(type(retorno.json()))

#print(retorno.json()['mensagem'])

