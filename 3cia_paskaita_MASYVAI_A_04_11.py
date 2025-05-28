# # # Sukurti norimą sąrašą  ir jame:
# # # •Atspausdinti vieną norimą įrašą
# # # •Pridėti įrašą
# # # •Ištrinti įrašą
# # # •pakeisti įrašą

# # # Sukuriam sąrašą su norimais elementais
# automobiliai = ["audi", "opelis", "bmw", "citroen"]

# # # Atspausdinam vieną konkretų įrašą (pvz., 3-čią automobilį)
# print("Vienas automobilis iš sąrašo:", automobiliai[2])  # indeksai prasideda nuo 0

# # # Pridedam naują automobilį į sąrašo pabaigą
# automobiliai.append("opelis")
# print("Po pridėjimo:", automobiliai)

# # # Ištrinam konkretų automobilį (pvz., "audi")
# automobiliai.remove("audi")
# print("Po ištrynimo:", automobiliai)

# # # Pakeičiam konkretų įrašą (pvz., vietoj 'audi' rašom 'džipas')
# automobiliai[0] = "džipas"
# print("Po pakeitimo:", automobiliai)


# #UŽDUOTIS___________________________________________________________________________
# # Leiskite naudotojui ivesti tris skaicius sudekite juos i sarasa ir atspausdinkite sarasa

# # Leidžiam naudotojui įvesti 3 skaičius
# skaicius1 = int(input("Įveskite pirmą skaičių: "))
# skaicius2 = int(input("Įveskite antrą skaičių: "))
# skaicius3 = int(input("Įveskite trečią skaičių: "))

# # Sudedam skaičius į sąrašą
# skaiciai = [skaicius1, skaicius2, skaicius3]

# # Atspausdinam visą sąrašą
# print("Sąrašas su įvestais skaičiais:", skaiciai)

# #REZULTATAS TERMINALE
# # Įveskite pirmą skaičių: 20
# # Įveskite antrą skaičių: 30
# # Įveskite trečią skaičių: 30
# # Sąrašas su įvestais skaičiais: [20, 30, 30]
