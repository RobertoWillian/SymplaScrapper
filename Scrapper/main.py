from fastapi import FastAPI
import scrapper
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"HELLO" : "WORD"}


@app.get("/eventos")
def get_eventos():
    json = scrapper.get_eventos_scrapper()
    return json
