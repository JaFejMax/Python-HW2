"""Durhá část
zeptat se uživatele na název subjektu (nebo alespoň část názvu)
odeslat POST požadavek na ARES API
získat z ARES seznam sůbjektů a u nich vypsat informace jmeno, ico, nenalezeno """
import requests
import json
#použiju class z první části úkolu class Subjekt
class Subjekt:
    def __init__(self, ico, jmeno, adresa):
        self.ico = ico
        self.jmeno = jmeno
        self.adresa = adresa

    def zobrazit_udaje(self):
        #vytiskne informace o subjektu
        print(f"{self.jmeno}, {self.ico}")

#Funkce pro více subjektů dle názvu
def najdi_subjekty_podle_nazvu(nazev):
    #Hlavičky požadavku
    headers = {"accept": "application/json", 
               "Content-type": "application/json"}
    
    #použijeme převod na json a kódování
    data = json.dumps({"obchodniJmeno": nazev})
    data = data.encode("utf-8")

    #Odeslání
    odpoved = requests.post(
        "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", 
        headers=headers, 
        data=data)
    
    vysledky = odpoved.json()

    #Ověření, že odpověď obsahuje seznam subjektů
    if "ekonomickeSubjekty" in vysledky:
        seznam_subjektu = vysledky["ekonomickeSubjekty"]
        objekty = []

        for subjekt in seznam_subjektu:
            jmeno = subjekt.get("obchodniJmeno", "Neznámý název")
            ico = subjekt.get("ico", "Neznámé IČO")
            adresa = None #adresu ziskame jenom pokud existuje
            if "sidlo" in subjekt and "textovaAdresa" in subjekt["sidlo"]:
                adresa = subjekt["sidlo"]["textovaAdresa"]

            objekty.append(Subjekt(ico, jmeno, adresa))
        return objekty
    else:
        print("Subjekty nenalezeny.")
        return[]
    
#Dotazovaci cast programu
nazev = input("Zadej název subjektu pro vyhledání: ").strip()

nalezene_subjekty = najdi_subjekty_podle_nazvu(nazev)

print(f"\n🔎 Nalezeno subjektů: {len(nalezene_subjekty)}")
for subjekt in nalezene_subjekty:
    subjekt.zobrazit_udaje()
    print("-" * 40) #oddělí výpisy od sebe graficky