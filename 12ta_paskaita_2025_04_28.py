
# UZDUOTIS NR 1
# Sukurkite funkciją, kuri priima skaičių sąrašą ir grąžina jų kvadratų sąrašą.


# def pakelta_kvadratu_sarasas(sarasas):
#     return [skaicius ** 2 for skaicius in sarasas]

# ivestis = input("Iveskite skaicius: ")
# sarasas = [int(x) for x in ivestis.split()]

# rezultatas = pakelta_kvadratu_sarasas(sarasas)
# print("Skaiciu pakeltu kvadratu:", rezultatas)

# REZULTATAS TERMINALE
# Iveskite skaicius: 10 20 30 40 50 60 70 80 
# Skaiciu pakeltu kvadratu: [100, 400, 900, 1600, 2500, 3600, 4900, 6400]


# ----------------------------------------------------------------

# UZDUOTIS NR 2
# Parašykite funkciją, kuri priima vartotojo vardą ir spausdina sveikinimo žinutę, pvz., "Labas, Jonas!".

# def vartotojo_vardas(vardas):
#     return f"Labas, {vardas}!"

# ivestis = input("Iveskite varda: ")

# rezultatas = vartotojo_vardas(ivestis)
# print(rezultatas)

# REZULTATAS TERMINALE
# Iveskite varda: Kestutis 
# Labas, Kestutis !

# -----------------------------------------------------------

# UZDUOTIS NR 3
# Sukurkite funkcija, kuri turi
#  ciklą for, kuris atspausdina skaičius nuo 1 iki 10.
# def spausdinti_skaicius():
#     for skaicius in range(1, 11):
#         print(skaicius)

# spausdinti_skaicius()

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

# -------------------------------------------------------

# UZDUOTIS NR 4
# Parašyk funkciją, kuri tikrina, ar duotas skaičius yra teigiamas, neigiamas, ar lygus nuliui.

# def skaiciu_tikrinimas(skaicius):
#     if skaicius > 0:
#         return "Skaičius yra teigiamas."
#     elif skaicius < 0:
#         return "Skaičius yra neigiamas."
#     else:
#         return "Skaičius yra nulis."
    
# ivestis = input("Įveskite skaičių: ")
# skaicius = int(ivestis)
# rezultatas = skaiciu_tikrinimas(skaicius)
# print(rezultatas)

# REZULTATAS TERMINALE
# Įveskite skaičių: 2
# Skaičius yra teigiamas.
# ------------------
# Įveskite skaičių: -2
# Skaičius yra neigiamas. 
# ------------- 
# Įveskite skaičių: 0
# Skaičius yra nulis.


# -------------------------------------------

# UZDUOTIS NR 5
# Parašyk funkciją, kuri gauna sąrašą ir grąžina sąrašo elementų kiekį.
# def elementu_kiekis(sarasas):
#     return len(sarasas)

# ivestis = (input("iveskite skaiciu sarasa nuo 1 iki 5: "))
# sarasas = [int(x) for x in ivestis.split()]
# kiekis = elementu_kiekis(sarasas)
# print("Sąraše yra", kiekis, "elementai/elementu.")
# REZULTATAS TERMINALE:
# iveskite skaiciu sarasa nuo 1 iki 5: 1 2 3 4 5
# Sąraše yra 5 elementai/elementu.

# ------------------------------------------------------------

# # UZDUOTIS NR 6
# # Sukurk funkciją, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių tame sąraše.

# def didziausias_skaicius(sarasas):
#     didziausias = sarasas[0]  #paimamas pirmas elementas is saraso
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
# vartotojo_ivestis = input("iveskite skiacius: ")
# ivesti_tekstai = vartotojo_ivestis.split()  #split padalina sarase esancius elementus i dalis.

# sarasas = []
# for x in ivesti_tekstai:
#     skaicius = int(x)
#     sarasas.append(skaicius) #prideda skaiciu i saraso gala


# rezultatas = didziausias_skaicius(sarasas) #randu didziausia skaiciu


# print("Didžiausias skaičius sąraše yra:", rezultatas)

# REZULTATAS TERMINALE
# iveskite skiacius: 10 20 40 50 60 80 90 100
# Didžiausias skaičius sąraše yra: 100

# ---------------------------------------------------------

# UZDUOTIS NR 7
# Parašyk funkciją, kuri tikrina, ar duotas skaičius yra lyginis ar nelyginis.
# def palyginimas (skaiciai):
#     if skaiciai %2 ==0:
#         return "lyginis"
#     else:
#         return "nelyginis"
# skaiciai = int(input("iveskite skaiciu: "))
# rezultatas = palyginimas (skaiciai)
# print("skaicius yra: ", rezultatas)
# REZULATAS TERMINALE:
# iveskite skaiciu: 8
# skaicius yra:  lyginis
# iveskite skaiciu: 3
# skaicius yra:  nelyginis

# --------------------------------------------


# UZDUOTIS NR 8
# Parašyk funkciją, kuri gauna skaičių n ir grąžina n daugybos lentelę nuo 1 iki 10.
# Pvz., daugybos_lentele(5) turėtų grąžinti 5 x 1 = 5, 5 x 2 = 10, ir t.t.

# def daugybos_lentele(n):
#     for i in range(1, 11):
#         rezultatas = n * i
#         print(f"{n} * {i} = {rezultatas}")
# vart_ivestis= int(input("iveskite skaiciu: "))
# daugybos_lentele(vart_ivestis)
# REZULTATAS TERMINALE:
# iveskite skaiciu: 8
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# 8 * 6 = 48
# 8 * 7 = 56
# 8 * 8 = 64
# 8 * 9 = 72
# 8 * 10 = 80

# ---------------------------------------------------------------

# UZDUOTIS NR 9
# Sukurk funkciją, kuri pašalina visus pasikartojančius elementus iš sąrašo. (galite naudoti set, jeigu mokate)

# def pasalinti_pasikartojimus(sarasas):
#     be_pasikartojimu_sarasas = []
#     [be_pasikartojimu_sarasas.append(z) for z in zodziai if z not in be_pasikartojimu_sarasas]
#     return be_pasikartojimu_sarasas
# vart_ivestis = input("iveskite texta kuriame butu pasikartojantys zodziai: ")
# zodziai = vart_ivestis.split()
# rezultatas = pasalinti_pasikartojimus(zodziai)
# print("textas be pasikartojanciu zodziu: ", rezultatas)
# REZULTATAS TERMINALE:
# iveskite texta kuriame butu pasikartojantys zodziai: labas labas jonai jonai kapitonai
# textas be pasikartojanciu zodziu:  ['labas', 'jonai', 'kapitonai']

# ----------------------------------------------------------

# UZDUOTIS NR 10
# Parašyk funkciją, kuri gauna sąrašą žodžių ir grąžina tik tuos žodžius, kurie yra ilgesni nei nurodytas ilgis.

# def filtruoti_ilgus_zodzius (zodziai, ilgis):
#     ilgi_zodziai = []
#     for zodis in zodziai:
#         if len(zodis) > ilgis:
#             ilgi_zodziai.append(zodis)
#     return ilgi_zodziai

# tekstine_ivestis = input("Įveskite žodžius atskirtus tarpais: ")
# zodziai = tekstine_ivestis.split()
# ilgis = int(input("Įveskite minimalų žodžio ilgį: "))
# rezultatas = filtruoti_ilgus_zodzius(zodziai, ilgis)
# print("Ilgesni žodžiai:", rezultatas)

# REZULTATAS TERMINALE:
# Įveskite žodžius atskirtus tarpais: Lietuva, Vilnius, Kaunas, rajonas, kiemas
# Įveskite minimalų žodžio ilgį: 4
# Ilgesni žodžiai: ['Lietuva,', 'Vilnius,', 'Kaunas,', 'rajonas,', 'kiemas']

# -------------------------------------------------------------

# UZDUOTIS NR 11
# Parašyk funkciją, kuri gauna du skaičius n ir m ir grąžina sumą visų skaičių nuo n iki m (įskaitant).
# Pvz., sekos_suma(3, 7) turėtų grąžinti 25 (3 + 4 + 5 + 6 + 7).

# def sekos_suma(n, m):
#     suma = 0
#     for skaicius in range(n, m + 1):
#         suma += skaicius
#     return suma

# n = int(input("Įveskite pradinį skaičių: "))
# m = int(input("Įveskite galutinį skaičių: "))

# rezultatas = sekos_suma(n, m)
# print("Suma nuo", n, "iki", m, "yra:", rezultatas)
# REZULTATAS TERMINALE:
# Įveskite pradinį skaičių: 2
# Įveskite galutinį skaičių: 15 
# Suma nuo 2 iki 15 yra: 119


