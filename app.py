from fastapi import FastAPI
from typing import Optional
from transakcje import transakcje
from api import kursyWalut, aktualnyKurs

app = FastAPI()


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

@app.get("/transakcje")
def get_transakcje(typ: Optional[str] = None, waluta: Optional[str] = None):
    if typ == None and waluta == None:
        return transakcje
    else:
        lista = []
        if waluta != None: waluta=waluta.upper()
        for item in transakcje:
            if ((transakcje[item]["typ"] == typ) or (transakcje[item]["waluta"] == waluta)):
                lista.append(transakcje[item])
        if len(lista) > 0:
            return lista

    return {"błąd": "Nie znaleziono transakcji dla podanych parametrów"}
