from fastapi import FastAPI

app = FastAPI()


@app.get("/") # url raiz
def root():
    return {'mensagem': 'Olá mundo'}


@app.get("/home")
def home():
    return {'mensagem': 'home'}


@app.get("/cadastro")
def cadastro():
    return {'mensagem': 'cadastro'}


@app.get("/login")
def login():
    return {'mensagem': 'login'}