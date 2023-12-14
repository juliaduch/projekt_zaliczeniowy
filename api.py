import requests
from datetime import date
from unidecode import unidecode
from datetime import timedelta
from funkcje import nowyFolder
from funkcje import zapiszDane
import json
import os


def kursyWalut30dni():

    #nowyFolder('kursy')
    tabele = ['A', 'B', 'C']
    data = date.today()
    kursy = []

    for i in range(1, 31):

        dataKursow = data - timedelta(days=i)
        for tabela in tabele:
            url = f'https://api.nbp.pl/api/exchangerates/tables/{tabela}/{dataKursow}/'
            res = requests.get(url)
            if res.status_code == 200:
                output = res.json()
                for waluta in output[0]['rates']:
                    waluta['currency'] = unidecode(waluta['currency'])

                kursy.extend(output[0]['rates'])

        #zapiszDane(kursy, dataKursow, 'kursy')
    return kursy


def cenaZlota():
    url = 'https://api.nbp.pl/api/cenyzlota/'
    res = requests.get(url)
    if res.status_code == 200:
        output = res.json()
        return output[0]['cena']


def kursyWalut():

    tabele = ['A', 'B', 'C']
    data = date.today() - timedelta(days=1)
    kursy = []

    for tabela in tabele:
        url = f'https://api.nbp.pl/api/exchangerates/tables/{tabela}/{data}/'
        res = requests.get(url)
        if res.status_code == 200:
            output = res.json()
            for waluta in output[0]['rates']:
                waluta['currency'] = unidecode(waluta['currency'])

            kursy.extend(output[0]['rates'])

    return kursy

def aktualnyKurs(waluta):
    kursy = kursyWalut()
    for i in range(len(kursy)):
        if (kursy[i]["code"] == waluta.upper()):
            return kursy[i]



