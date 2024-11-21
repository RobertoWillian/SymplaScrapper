from fastapi import FastAPI
import scrapper
from fastapi.middleware.cors import CORSMiddleware

#Define a varíavel app com a biblioteca do FastAPI
app = FastAPI()

#Define o Cross-origin para livre acesso
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#EndPoint para o front acessar os eventos
@app.get("/eventos")
def get_eventos():
    json = scrapper.get_eventos_scrapper()
    return json
