
# ------------------------1.Gražinti trijų paduotų skaičių sumą.---------------------

# def skaiciu_suma(a, b, c):
#     suma = a + b + c
#     return suma

# a = int(input("iveskite pirmaji skaiciu: "))
# b = int(input("iveskite antraji skaiciu: "))
# c = int(input("iveskite treciaji skaiciu: "))

# rezultatas = skaiciu_suma(a, b, c)
# print("skaiciu suma yra: ", rezultatas)
# REZULTATAS TERMINALE
# iveskite pirmaji skaiciu: 10
# iveskite antraji skaiciu: 20
# iveskite treciaji skaiciu: 30
# skaiciu suma yra:  60




#-------------------------- 2.Gražintų paduoto sąrašo iš skaičių, sumą.----------------------------------
# def skaiciu_suma(sarasas):
#     suma = 0                    # pradedam nuo 0 – čia kaupsime bendrą sumą
#     for skaicius in sarasas:   # einame per kiekvieną skaičių sąraše
#         suma += skaicius       # pridedame skaičių prie sumos (suma = suma + skaicius)
#     return suma                  # grąžiname galutinį rezultatą

# ivestis = input("Iveskite skaicius: ")
# skaiciai_kaip_tekstas = ivestis.split()  # Padalijame tekstą į atskirus žodžius (tekstinius skaičius), pvz. ["5", "8", "10"]
# sarasas = [int(x) for x in skaiciai_kaip_tekstas]  # Paverčiame kiekvieną tekstą į skaičių (int) ir sukuriame sąrašą, pvz. [5, 8, 10]
# rezultatas = skaiciu_suma(sarasas)                   # Paduodame sąrašą į funkciją ir išsaugome rezultatą
# print("skaiciu suma yra: ", rezultatas)            #isvedam atsakyma i terminala

# RZULTATAS TERMINALE 
# Iveskite skaicius: 10 20 30 40 50 10
# skaiciu suma yra:  160



# ---------------------------3.Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).----------------------
# def didziausias_skaicius (*skaiciai):   #Funkcija priims bet kiek skaičių (nežinomą jų kiekį), kaip vieną sąrašą.
#     print("Didziausias skaicius yra: ", max(skaiciai))   #su max randme didziausia skaiciu sarase

# ivestis = input("Iveskite skaicius: ")
# sarasas = [int(x) for x in ivestis.split()]  ## Paverčiame kiekvieną tekstą į skaičių (int) ir padaliname texta i atskirus textinius skaicius
# didziausias_skaicius(*sarasas)
# REZULTATAS TERMINALE
# Iveskite skaicius: 20 100 500 800 1000
# Didziausias skaicius yra:  1000



# -----------------------4.Gražintų paduotą stringą atbulai.--------------------------------
# def atbulai (textas):
#     apverstas = textas[::-1]    # naudojam slicing – nuo pradžios iki galo atgal
#     return apverstas
# ivestis = input("iveskite texta: ")
# rezultatas = atbulai(ivestis)
# print("atbulai ivestas textas yra: ", rezultatas)

# REZULTATAS TERMINALE
# iveskite texta:  geri metai   
# atbulai ivestas textas yra:  iatem ireg 




# # --------------5.Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių----------------------
# def analizuoti_texta(textas):
#     zodziu_kiekis = len(textas.split())  # skaičiuoja žodžius pagal tarpą
#     didziosios = 0  # pradinis skaičius
#     mazosios = 0
#     skaiciai = 0
#     for simbolis in textas:
#         if simbolis.isupper():        # jeigu didžioji raidė
#             didziosios += 1
#         elif simbolis.islower():   # jeigu mažoji raidė
#             mazosios += 1
#         elif simbolis.isdigit():   # jeigu skaičius
#             skaiciai += 1
#     return zodziu_kiekis, didziosios, mazosios, skaiciai  # grąžina viską

# ivestis=input("iveskite texta: ")
# zodziu_kiekis, didziosios, mazosios, skaiciai = analizuoti_texta(ivestis)

# print("zodziu kiekis: ", zodziu_kiekis)
# print("didziosios raides", didziosios)
# print("mazuju raidziu:", mazosios)
# print("skiaciu yra:", skaiciai)

# REZULTATAS TERMINALE
# iveskite texta: lietuvoje gyvena 5 zmones su 4 SUNIMIS
# zodziu kiekis:  7
# didziosios raides 7
# mazuju raidziu: 23
# skiaciu yra: 2




#--------------------- 6.Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.------------------------
# def unikalus_elementai(sarasas):
#     unikalus = []  # naujas sąrašas, kuriame laikysime tik vienetinius elementus
    
#     for elementas in sarasas:
#         if elementas not in unikalus:      # tikriname, ar elemento dar nėra sąraše
#             unikalus.append(elementas)        # jei nėra – pridedame / append prideda tik naujus elementus
#     return unikalus  # grąžiname galutinį sąrašą su unikalais

# vart_ivestis = input("iveskite elementus: ")
# sarasas = vart_ivestis.split()  # padalina tekstą į elementų sąrašą (pvz. žodžiai arba skaičiai kaip tekstas)
# rezultatas = unikalus_elementai(sarasas)
# print("unikalus elementai yra: ", rezultatas)

# Rezultatas Terminale:
# iveskite elementus: 1 2 4 Kaunas vyras &
# unikalus elementai yra:  ['1', '2', '4', 'Kaunas', 'vyras', '&']



# ----------------------# 7.Gražintų, ar paduotas skaičius yra pirminis.--------------------------------
# PASTABA Jei skaičius turi 3 ar daugiau daliklių → jis ne pirminis

def ar_pirminis(skaicius):
    if skaicius < 2:
        return False  # netiesa 0 ir 1 nėra pirminiai






# 8.Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
# 9.Gražina, ar paduoti metai yra keliamieji, ar ne.
# 10.Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
 



# 1.Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
# 2.Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).
 




# 1.Sukurti funkciją, kuri grąžintų True reikšmę, jei įvesto skaičiaus pirma skaitmenų pusė yra lygi antrąjai, priešingu atveju grąžintų False. # 1569 | 1+5 = 6 ir 6+9 = 15
# 2.Parašyti funkciją, kuri grąžintų, kiekvieno elemento gretimą skaičių. Pvz:
#       Input: 56789
#       Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79, 9 - 8
 
