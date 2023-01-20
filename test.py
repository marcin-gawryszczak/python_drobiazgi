import requests
from requests.exceptions import HTTPError
import json

class Cinkciarz:
    def __init__(self):
        print('Cinciarz stworzony')

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
kurs = cinkciarz.zapytaj_o_kurs('chf')

#prośba o przeliczenie
przeliczenie = cinkciarz.przelicz_na_PLN('eur', 6000)


# hej dorzucam jeszcze parę słów o mnie. Z pythonem spotkałem się pierwszy raz parę miesięcy temu. Mam zrobiony  kurs na udemy i parę tutoriali. W listopadzie dostałem się na staż w IT (akurat bez pythona, lecz z js), który niedawno dobiegł końca (ale mega dużo się tam nauczyłem). Mam zatem sporo czasu na pracę w ciekawym projekcie. Moją cechą charakterystyczną w programowaniu jest to, że zawsze walczę do końca przy szukaniu optymalnych rozwiazań :) Znam gita, scruma i parę innych technologii przydatnych w projektach. W razie chęci kontaktu piszcie na maila: gawryszczakmarcin@gmail.com lub na FB :) Pozdrowienia