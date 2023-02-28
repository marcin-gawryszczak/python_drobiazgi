import requests
from requests.exceptions import HTTPError
import json

class Cinkciarz:
    def __init__(self):
        print('Cinkciarz działa')

    def przelicz_na_PLN(self, kod, ile):
        try:
    # dokumentację API dla NBP znajdziesz pod adresem http://api.nbp.pl/
            url = f'http://api.nbp.pl/api/' \
                f'exchangerates/rates/a/' \
                f'{kod}/' \
                f'?format=json'
            response = requests.get(url)
        except HTTPError as http_error:
            print(f'HTTP error: {http_error}')
        except Exception as e:
            print(f'Other exception: {e}')
        else:
            if response.status_code == 200:
                response = response.json()
                kurs = response['rates'][0]['mid']
        total_PLN = ile*kurs
        print(total_PLN, 'zł')
        
    def zapytaj_o_kurs(self, kod):
        try:
    # dokumentację API dla NBP znajdziesz pod adresem http://api.nbp.pl/
            url = f'http://api.nbp.pl/api/' \
                f'exchangerates/rates/a/' \
                f'{kod}/' \
                f'?format=json'
            response = requests.get(url)
        except HTTPError as http_error:
            print(f'HTTP error: {http_error}')
        except Exception as e:
            print(f'Other exception: {e}')
        else:
            if response.status_code == 200:
                response = response.json()
                kurs = response['rates'][0]['mid']
                print(kurs, 'zł')
    
# przykładowe zastosowanie
# stworzenie klasy
cinkciarz = Cinkciarz() 

#prośba o kurs
kurs = cinkciarz.zapytaj_o_kurs('nok')

#prośba o przeliczenie
przeliczenie = cinkciarz.przelicz_na_PLN('GBP', 6000)


