from fastapi import FastAPI

app = FastAPI()

usuarios = [(1, 'caio', 'minhasenha1'), (2, 'joao', 'minhasenha2')]


@app.get('/usuario/{id}') # Parâmetros {}
def main(id):
    for i in usuarios:
        if i[0] == id:
            return i[0]

    return "Não existe esse usuário"


@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i

    return "Não existe esse usuário"

