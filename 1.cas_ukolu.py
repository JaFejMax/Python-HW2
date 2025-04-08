""" 1. část
zeptat se na IČO, sestavit URL s tímto IČ
získat data z API, převést odpověď na JSON
vytáhnout a vypsat jeho adresu"""
import requests
#Třída pro subjekt
class Subjekt:
    def __init__(self, ico, jmeno, adresa):
        self.ico = ico
        self.jmeno = jmeno
        self.adresa = adresa
    def zobrazit_udaje(self):
        #vytiskne informace o subjektu
        print(f"\n{self.jmeno}")
        print(self.adresa) 
#Funkce pro získání dat z API podle IČO
def najdi_subjekt_podle_ico(ico):
        url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico
        odpoved = requests.get(url)
        data = odpoved.json()
        #pokud odpověď obsahuje vše
        if "obchodniJmeno" in data and "sidlo" in data and "textovaAdresa" in data["sidlo"]:
             jmeno = data["obchodniJmeno"]
             adresa = data["sidlo"]["textovaAdresa"]
             #novy objekt typu Subjekt
             subjekt = Subjekt(ico, jmeno, adresa)
             return subjekt
        else:
             print("Subjekt nebyl nalezen nebo nemá kompletní údaje.")
             return None
#Hlavni cast
zadane_ico = input("Zadej IČo subjektu: ").strip()

subjekt = najdi_subjekt_podle_ico(zadane_ico)

if subjekt:
     subjekt.zobrazit_udaje()



