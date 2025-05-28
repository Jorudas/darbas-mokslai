# UZDUOTIS 
# Sukurkite while ciklą, kuris atspausdintų skaičius nuo 1 iki 10
# skaicius = 1
# while skaicius <=10:
#     print(skaicius)
#     skaicius +=1
# REZULTATAS TERMINALE 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10





# UZDUOTIS 
# Sukurkite while ciklą kuris atspausdintų žodyje esančias raides po vieną
# zodis = "NAMAS"
# indeksas = 0
# while indeksas < len(zodis):
#     print(zodis[indeksas])
#     indeksas +=1
# # REZULTATAS TERMINALE 
# # N
# # A
# # M
# # A
# # S






# #  UZDUOTIS 
# # Sukurkite for ciklą, kuris veikia tol kol sąraše randa žodį "labas" ir tada nutraukia savo veikla
# sarasas = ["lape", "namas", "lopas", "labas", "suo"]
# for zodis in sarasas:
#     print("tikrinam zodi: ", zodis)
#     if zodis == "labas":
#         print(" radome zodi - LABAS ir stabdome cikla")
#         break
# REZULTATAS TERMINALE 
# tikrinam zodi:  lape
# tikrinam zodi:  namas
# tikrinam zodi:  lopas
# tikrinam zodi:  labas
#  radome zodi - LABAS ir stabdome cikla



# # UZDUOTIS 
# # Atspausdinkite su for ciklu visas žodyno reikšmių poras (panaudokite items)
# zmones = { "Kestutis": "Jorudas", "Ernesta": "Jorude" }
# for vardas, pavarde in zmones.items():
#     print(vardas, "-", pavarde)
# REZULTATAS TERMINALE 
# Kestutis - Jorudas
# Ernesta - Jorude




# UZDUOTIS 
# Sukurkite tuple su trimis elementais ir išveskite antrą elementą.
# tuple = ("NAMAS", "MEDIS", "TVORA")
# print("antras elementas", tuple[1])
# REZULTATAS TERMINALE 
# antras elementas MEDIS



# UZDUOTIS 
# Sukurkite set ir išveskite jo ilgį 
# setas = {"obuolys", "kriause", "lenta","obuolys"}
# print("seto ilgis", len(setas))
# REZULTATAS TERMINALE 
# seto ilgis 3


# UZDUOTIS 
# Paprašykite įvesti skaičių ir atspausdinkite „Sveikas, pasauli!“ tiek kartų, kiek buvo įvestas skaičius, panaudokite while
# vartotojas = int(input("iveskite skaiciu koki norite, kad kiek kartu atsispausdintu „Sveikas, pasauli! "))
# kiek = 0
# while kiek < vartotojas:
#     print("Sveikas pasauli!")
#     kiek += 1
# REZULTATAS TERMINALE 
# iveskite skaiciu koki norite, kad kiek kartu atsispausdintu „Sveikas, pasauli! 5
# Sveikas pasauli!
# Sveikas pasauli!
# Sveikas pasauli!
# Sveikas pasauli!
# Sveikas pasauli!



# UZDUOTIS 
# Parašykite programą, kuri suskaičiuoja skaičių nuo 1 iki n sumą naudodama while ciklą.




# UZDUOTIS 
# Parašykite programą, kuri priima tris kampų dydžius ir patikrina, ar jie gali sudaryti trikampį (suma lygi 180°).
                                                                                                 

# UZDUOTIS 
# Parašykite programą, kuri išves didžiausia skaičių sąraše (be max)

# UZDUOTIS 
# Parašyti programą, kuri:
# •Leistų vartotojui įvesti skaičių.
# •Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# •Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break


# UZDUOTIS 
# Sukurti programą, kuri:
# •Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# •Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# •Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break