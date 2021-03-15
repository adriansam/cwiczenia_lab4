# plik = open(nazwa,tryb,bufor)
#
# znaki = plik.read(10)
# print(znaki)
#
# linia = plik.readline()
# print(linia)
#
# linie=plik.readlines()
# print(linie)
# print(type(linie))

# import sys
# plik = open('dane.txt','w+',encoding='utf8')
#
# print("Podaj kierunek studow, rok i specjazlizację")
# dane = sys.stdin.readline()
#
# plik.write(dane)
#
# plik.close()
#
# lista = []
# for x in range(6):
#     lista.append(x)
#
# plik = open('dane.txt','a+',encoding='utf8')
#
# plik.writelines(str(lista))

# with open('tekst.txt','r') as plik:
#     for linie in plik:
#         print(linie,end='')
#         print(type(linie))
#
# class NazwaKlasy:

# class PierwszaKlasa:
#     """Pierwsza klasa w python"""
#     atrybut = 54321
#     def __init__(self):
#     def pierwsza_metoda(self):
#         return "Teraz działa pierwsza metoda"
#
# obiekt = PierwszaKlasa()
# print(obiekt)
# print(obiekt.atrybut)
# print(obiekt.pierwsza_metoda())
# obiekt.tekst = 'xyz'
# print(obiekt.tekst)
#
# nowy_obiekt = PierwszaKlasa()
# print(nowy_obiekt.tekst) nie mozna sie odwolac do tekst

class Ksztalt:
    __zmienna__ = "xyz"
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        self.opis = "To bedzie klasa do ogolnych ksztaltow"
    def pole(self):
        return self.x * self.y
    def obwod(self):
        return 2*self.x + 2*self.y
    def dodaj_opis(self,text):
        self.opis = text
    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik
    def zmien_tekst(self,tekst):
        tekst += "to jest napis"
        return tekst

prostokat = Ksztalt(10, 30)
# print(prostokat.pole())
# print(prostokat.obwod())
# prostokat.dodaj_opis("To jest prostokat")
# print(prostokat.opis)
# prostokat.skalowanie(0.5)
# print(prostokat.x)
# print(prostokat.y)
# print(prostokat.pole())

print(prostokat.__zmienna__)

prostokat.__zmienna__ = "na na na"
print(prostokat.__zmienna__)

print(prostokat.zmien_tekst(prostokat.__zmienna__))

