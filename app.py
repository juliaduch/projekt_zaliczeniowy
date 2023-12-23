from fastapi import FastAPI
from typing import Optional
from transakcje import transakcje
from api import kursyWalut, aktualnyKurs
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as T_router

app = FastAPI()
config = dotenv_values("passy.env")

@app.get("/")
def home():
    return [{"/kursy": "Wyświetl aktualne kursy dla wszystkich walut"},
            {"/kursy/usd": "Wyświetl aktualny kurs dla USD"},
            {"/transakcje": "Wyświetl wszystkie transakcje"},
            {"/transakcje?typ=sprzedaz": "Wyświetl wszystkie transakcje o typie sprzedaz"},
            {"/transakcje?waluta=eur": "Wyświetl wszystkie transakcje dla waluty eur"}]


@app.get("/kursy/")
def kursy():
    return kursyWalut()



@app.get("/kursy/{code}")
def kursy(code: str):
    kurs = aktualnyKurs(code)
    if (kurs != None):
        return kurs
    else:
        return {"błąd": "Nie znaleziono aktualnego kursu dla tej waluty"}
    
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(T_router, tags=["pythonproject"], prefix="/pythonproject")


