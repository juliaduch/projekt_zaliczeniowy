from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Transakcje

router = APIRouter()
## POST
@router.post("/dodaj_transakcje", response_description="Dodaj nowa transakcje", status_code=status.HTTP_201_CREATED, response_model=Transakcje)
def Dodaj_transakcje(request: Request, transakcja: Transakcje = Body(...)):
    transakcja = jsonable_encoder(transakcja)
    nowa_transakcja = request.app.database["pythonproject"].insert_one(transakcja)
    dodana_transakcja = request.app.database["pythonproject"].find_one(
        {"_id": nowa_transakcja.inserted_id}
    )

    return dodana_transakcja

## GET ALL
@router.get("/transakcje", response_description="Wszystkie transakcje", response_model=List[Transakcje])
def wszystkie_transakcje(request: Request):
    transakcje = list(request.app.database["pythonproject"].find(limit=100))
    return transakcje

## GET by ID
@router.get("/transakcje/{id}", response_description="Znajdz transakcje po id", response_model=Transakcje)
def znajdz_transakcje(id: str, request: Request):
    if (transakcja := request.app.database["pythonproject"].find_one({"_id": id})) is not None:
        return transakcja
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transakcja z ID {id} niezostala znaleziona")

## PUT  
@router.put("/transakcje/zaktualizuj_transakcje/{id}", response_description="Zaktualizuj transakcję o podanym ID", response_model=Transakcje)
def aktualizuj_transakcje(id: str, request: Request, nowe_dane: Transakcje = Body(...)):
    aktualne_dane = request.app.database["pythonproject"].find_one({"_id": id})

    if aktualne_dane:
        aktualizowane_dane = jsonable_encoder(nowe_dane)
        request.app.database["pythonproject"].update_one({"_id": id}, {"$set": aktualizowane_dane})
        return aktualne_dane
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transakcja z ID {id} nie została znaleziona")

## DELETE
@router.delete("/transakcje/usun_transakcje/{id}", response_description="Usuń transakcję o podanym ID", response_model=dict)
def usun_transakcje(id: str, request: Request):
    usunieta_transakcja = request.app.database["pythonproject"].find_one_and_delete({"_id": id})

    if usunieta_transakcja:
        return {"status": "success", "message": f"Transakcja o ID {id} została usunięta"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Transakcja z ID {id} nie została znaleziona")

