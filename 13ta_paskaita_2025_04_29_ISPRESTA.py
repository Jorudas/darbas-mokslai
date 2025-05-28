

# ----------------------------UZDUOTIS NR 1---------------------------------------------

# Parašyk funkciją, kuri tikrina, ar žodis yra palindromas (tas pats skaitomas iš priekio ir iš galo).
# Pvz., ar_palindromas("savas") turėtų grąžinti True.

# def ar_palindromas(zodis):
#     return zodis == zodis [::-1]  #Ar zodis lygus pats sau tik is kitos puses / start stop step

# Vart_ivestis =input("iveskite zodi: ")

# if ar_palindromas(Vart_ivestis):
#     print("tai yra PALINDROMAS")
# else:
#     print("tai ne PALINDROMAS")

# REZULTATAS TERMINALE:
# iveskite zodi: savas    #TRUE
# tai yra PALINDROMAS

# iveskite zodi: labas
# tai ne PALINDROMAS   #FALSE





# -------------------------------------UZDUOTIS NR 2-----------------------------------------------------
# Skaičių suma: Sukurkite funkciją, kuri priima sąrašą skaičių ir grąžina jų sumą. Panaudokite for ciklą.

# def skaiciu_suma(sarasas):              #(saras) reiksme kuria perduosiu funkcijai
#     suma = 0                         #Sukuria pradzia (nuo 0)
#     for skaicius in sarasas:       # eina per kiekviena skaiciu saraše
#         suma += skaicius              #prideda skaičių prie bendros sumos
#     return suma                    #grazina galutine suma

# vart_ivestis = input("iveskite skaicius: ")
# sarasas = [int(x) for x in vart_ivestis.split()]   #int(x) (pavercia texta i skaiciu);  # for x in ... #(Einama per kiekvieną žodį) # ivestis.split() (Padalina tekstą į žodžius)
# rezultatas = skaiciu_suma(sarasas)
# print("Suma yra:", rezultatas)

# REZULTATAS TERMINALE
# iveskite skaicius: 2 4 5 6 7 8 9 10
# Suma yra: 51



# ------------------------------# UZDUOTIS NR 3---------------------------------------
# Žodžių skaičius sakinyje: Parašykite funkciją, kuri priima sakinį ir grąžina žodžių skaičių jame.

# def zodziu_skaicius(sakinys):
#     zodziai = sakinys.split()   #padalina tekstą pagal tarpus → gaunu žodžių sąrašą
#     return len(zodziai)          #suskaičiuoja ir grazina, kiek žodžių yra sąraše
# ivestis = input("iveskite sakini: ")
# kiekis = zodziu_skaicius(ivestis)
# print("Zodziu skaicius sakinyje yra: ", kiekis)

# REZULTATAS TERMINALE 
# iveskite sakini: Sportas yra gerai, valgyti sveika maista taip pat yra sveika.
# Zodziu skaicius sakinyje yra:  10



#------------------------------- UZDUOTIS NR 4-------------------------------------
# Sukurkite funkciją, kuri priima prekių žodyna su kainomis ir grąžina bendra sumą.
# Papildomai, jei bendra suma viršija 100€, suteikiama 10% nuolaida.

# def apskaiciuoti_suma (prekes):
#     suma = sum(prekes.values())        # suskaičiuojam visų prekių kainas
#     if suma > 100:
#         suma *=0.9
#     return suma

# prekiu_zodynas = {"kede" : 30, "stalas" : 80, "lentyna" : 100}

# galutine_suma = apskaiciuoti_suma(prekiu_zodynas)
# print ("Galutine suma: ",galutine_suma, "EUR")

# REZULTATAS TERMINALE 
# Galutine suma:  189.0 EUR