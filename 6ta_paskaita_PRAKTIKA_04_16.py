# UZDUOTIS 
# RAIDZIU ISSKAIDYMAS
# Paprašykite naudotojo įvesti trumpą žodį arba frazę.
# Panaudokite for ciklą, kad išvestumėte kiekvieną įvesto teksto simbolį (raidę, tarpą) naujoje eilutėje.

# textas = input("įveskite trumpą žodį arba frazę.")
# print("Jusu fraze", textas)

# print("Simboliai po vieną:")
# for simbolis in textas:
#     print(simbolis)

# REZULTATAS TERMINALE
# Jusu fraze lauke lyja
# Simboliai po vieną:
# l
# a
# u
# k
# e

# l
# y
# j
# a





# UZDUOTIS
# SKAICIU PAKLEIMAS LAIPSNIU
# Paprašykite naudotojo įvesti du skaičius: pagrindą (base) ir laipsnį (power) (pvz., 2 ir 3).
# Sukurkite ciklą, kuris dauginimo būdu apskaičiuotų base^power (nereikėtų naudoti integruotos ** operacijos).
# Išveskite gautą rezultatą.
# Pavyzdys: Jei naudotojas įveda 2 ir 3, rezultatas: 2^3 = 8.

# base = int(input("iveskite pagrindini skaiciu (base)! "))
# power = int(input("pakelkite savo ivesta skaiciu laipsniu (power)! "))







# UZDUOTIS
# SIMBOLIU PAIESKA
# Paprašykite naudotojo įvesti sakinį.
# Tuomet leiskite įvesti raidę (ar kitą simbolį), kurio bus ieškoma sakinyje.
# Naudodami for ciklą suskaičiuokite, kiek kartų ši raidė pasikartoja sakinyje, ir išveskite rezultatą.






# UZDUOTIS
# ZODZIU ISSKAIDYMAS IR SPAUSDINIMAS
# Paprašykite naudotojo įvesti sakinio ilgį (kiek žodžių planuoja įvesti).
# Tegul naudotojas įveda kiekvieną žodį atskirai. Visus žodžius išsaugokite sąraše.
# Naudodami for ciklą išveskite žodžius atvirkštine tvarka (nuo paskutinio iki pirmo).





# UZDUOTIS
# ZODZIO APSUKIMAS
# Paprašykite naudotojo įvesti žodį ar trumpą frazę.
# Sukurkite programą, kuri, naudodama for ciklą, atspausdintų šį žodį (pvz., "Kava" → "avaK"). Nenaudokite [::-1] ar reverse
# Išveskite gautą apsuktą tekstą.





# UZDUOTIS
# Didžiausios reikšmės radimas be max
# Susikurkite sąrašą, pvz. [3, 7, 1, 12, 9].
# Naudodami for ciklą raskite didžiausią elementą sąraše (nenaudokite max() funkcijos).
# Išveskite rastą reikšmę.






# LENGVA UZDUOTIS
# Sukurkite ciklą kuris atspausdintų visus skaičius nuo 10 iki 1
# for skaicius in range(10, 0, -1):
#     print(skaicius)
# #REZULTATAS TERMINALE 
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1




# # LENGVA UZDUOTIS
# # Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki -100
# for skaicius in range(0, 101, 1):
#     print(skaicius)
# #REZULTATAS TERMINALE 
# 0
# 1
# 2
# 3
# 4
# 5
# .....
# 91
# 92
# 93
# 94
# 95
# 96
# 97
# 98
# 99
# 100




# LENGVA UZDUOTIS
# Sukurkite ciklą kuris atspausdintų skaičius nuo naudotojo įvesto skaičiaus iki naudotojo įvesto skaičiaus 
# ivestis_nuo = int(input("iveskite skaiciu! "))
# ivestis_iki = int(input("iveskite skaiciu! "))

# for skaicius in range(ivestis_nuo, ivestis_iki +1 ):
#     print(skaicius)

# # REZULTATAS TERMINALE
# iveskite skaiciu! 1
# iveskite skaiciu! 5
# 1
# 2
# 3
# 4
# 5





# LENGVA UZDUOTIS
# Sukurkite žodyną kuriame saugosite Žmonių pavardes, naudotojui įvedus vardą pasisveikinkite su juo jo vardu ir Pavarde
# zmones = {
#     "Kęstutis": "Jorudas", 
#         "Patricija": "Jorudaite", 
#         "Ernesta": "Jorude",
#         "Leonardas": "Jorudas"
#         }
# vardas = input("koks Jusu vardas?" )
# print("labas", vardas, zmones[vardas])
# REZULTATAS TERMINALE
# koks Jusu vardas?Kęstutis
# labas Kęstutis Jorudas






# # UZDUOTIS
# # LYGINIU SKAICIU ATSPAUSDINIMAS
# # Sukurkite ciklą, kuris spausdina visus lyginius skaičius nuo 2 iki 20.
# for skaicius in range(2, 21, (skaicius %2=0)]:







# UZDUOTIS
# MEGSTAMU GYVUNU SARASAS
# Sukurkite sąrašą su penkiais mėgstamiausiais gyvūnų pavadinimais.
# Naudokite ciklą, kad kiekvieno gyvūno pavadinimą išvestumėte kartu su prierašu, pvz., " - yra nuostabus."





# UZDUOTIS
# SKAICIU CHARAKTERISTIKOS
# Paprašykite vartotojo įvesti 5 skaičius, įrašykite juos į sąrašą, o tada ciklo pagalba patikrinkite kiekvieną skaičių:
# Jei skaičius teigiamas – išveskite, kad jis teigiamas.
# Jei neigiamas – praneškite, kad jis neigiamas.
# Jei lygus nuliui – nurodykite, kad jis lygus nuliui.


# UZDUOTIS
# SPALVU SARASO TRANSFORMACIJA
# Sukurkite sąrašą su keliomis spalvų reikšmėmis
#  (pvz., „raudona“, „žalia“, „mėlyna“). Naudokite ciklą, kad kiekvieną spalvą konvertuotumėte į mažąsias raides ir išveskite naują sąrašą.



# UZDUOTIS
# VARTOTOJO SVEIKINIMAS PAGAL VARDA IR AMZIU 
# Paprašykite vartotojo įvesti savo vardą ir amžių. Jei amžius yra 18 metų ar daugiau, išveskite sveikinimą, pvz.:
# "Sveikas, [vardas]! Tu jau pilnametis."
# Priešingu atveju, informuokite, kad dar nesieki pilnametystės.



#  UZDUOTIS
# Miestų gyventojų filtravimas
# Sukurkite žodyną, kuriame saugomi keli miestai ir jų gyventojų skaičiai. 
# Naudodami ciklą spausdinkite tik tuos miestus, kuriuose gyventojų skaičius viršija 100 000.



# SUNKI UZDUOTIS 
# RAIDZIU DAZNUMO SKAICIAVIMAS TEKSTE
# Paprašykite vartotojo įvesti tekstą. Naudodami žodyną ir ciklą, suskaičiuokite, kiek kartų kiekviena raidė pasikartoja, ir išveskite rezultatą.



# SUNKI UZDUOTIS 
# STUDENTU PAZYMIU ZODYNAS
# Sukurkite žodyną, kuriame raktai yra studentų vardai, 
# o reikšmės – jų pažymių vidurkiai. Naudodami ciklą išveskite studentų vardus ir vidurkius tik tiems, kurių vidurkis yra virš 8.












