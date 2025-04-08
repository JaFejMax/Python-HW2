"""Durhá část
zeptat se uživatele na název subjektu (nebo alespoň část názvu)
odeslat POST požadavek na ARES API
získat z ARES seznam sůbjektů a u nich vypsat informace jmeno, ico, nenalezeno """
#použiju class z první části class Subjekt
class Subjekt:
    def __init__(self, ico, jmeno, adresa):
        self.ico = ico
        self.jmeno = jmeno
        self.adresa = adresa
    def zobrazit_udaje(self):
        #vytiskne informace o subjektu
        print(f"\n{self.jmeno}")