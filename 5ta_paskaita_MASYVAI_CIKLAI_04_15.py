# UZDUOTIS
# Sukurkite sąrašą iš žodžių ir atspausdinkite kiekvieną žodį atskiroje eilutėje.
# sarasas = ["lape", "vilkas", "suo", "zuikis"]
# for zodis in sarasas:
#     print(zodis)
# # REZULTATAS TERMINALE
# lape
# vilkas
# suo
# zuikis




# # Sukurkite skaičių sąrašą ir pakelkite visu sąrašo skaičius
# #  naudotojo pasirnktu laipsniu, sąrašą sukursite patys, laipsnį pasirinks naudotojas.
# #  Kiekvieno elemento pakelta laipsniu reikšmę atspausdinkite.
# sarasas = [1, 2, 3, 4, 5, 6]
# laipsnis = int(input("Įveskite laipsnį, kuriuo pakelti skaičius: "))
# print("Pakelti skaičiai:")
# for skaicius in sarasas:
#     pakeltas = skaicius ** laipsnis
#     print(f"{skaicius} laipsniu {laipsnis} = {pakeltas}")
#  # REZULTATAS TERMINALE
#     Įveskite laipsnį, kuriuo pakelti skaičius: 2
# Pakelti skaičiai:
# 1 laipsniu 2 = 1
# 2 laipsniu 2 = 4
# 3 laipsniu 2 = 9
# 4 laipsniu 2 = 16
# 5 laipsniu 2 = 25
# 6 laipsniu 2 = 36




# UZDUOTIS
# Sukurti programą, kuri:
# 1)•Leistų vartotojui įvesti metus
# 2)Atspausdintų „Keliamieji metai“, jei taip yra
# 3)•Atspausdintų „Nekeliamieji metai“, jei taip yra
# 4)•Perdaryti užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.
# Šią programą jau darėte praeitą paskaitą, reikia pasiimti prieš tai darytą programą ir pritaikyti ketvirtą punktą.
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų

# # 1) Vartotojas iveda metus / 2)Atspausdintų „Keliamieji metai“, jei taip yra / 3)•Atspausdintų „Nekeliamieji metai“, jei taip yra
# metai = int(input("ibeskite metus: "))
# # Tikriname, ar tai keliamieji metai
# if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
#     print("Keliamieji metai")
# else:
#     print("Nekeliamieji metai")

# print("metai")
# REZULTATAS TERMINALE
# iveskite metus: 2024
# Keliamieji metai
# metai
# ________________
# ibeskite metus: 1890
# Nekeliamieji metai
# metai

# •Perdaryti užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.
# Spausdiname visus keliamuosius metus nuo 1900 iki 2100
# print("Keliamieji metai nuo 1900 iki 2100")
# for metai in range(1900, 2101):
#     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
#         print(metai)
# # REZULTATAS TERMINALE
# Keliamieji metai nuo 1900 iki 2100
# 1904
# 1908
# 1912
# 1916
# 1920
# 1924
# 1928
# 1932
# 1936
# 1940
# 1944
# 1948
# 1952
# 1956
# 1960
# 1964
# 1968
# 1972
# 1976
# 1980
# 1984
# 1988
# 1992
# 1996
# 2000
# 2004
# 2008
# 2012
# 2016
# 2020
# 2024
# 2028
# 2032
# 2036
# 2040
# 2044
# 2048
# 2052
# 2056
# 2060
# 2064
# 2068
# 2072
# 2076
# 2080
# 2084
# 2088
# 2092
# 2096




# UZDUOTIS
# Parašykite ciklą kuris skaičiuos visų nelyginių skaičių sumą esančiu nuo 10 iki 100
# suma = 0
# for skaicius in range (10, 101):
#     if skaicius % 2 !=0: 
#         suma += skaicius #suma = suma + skaicius
# print("Nelyginiu skaiciu suma nuo 10 iki 100", suma)
# REZULTATAS TERMINALE
# Nelyginiu skaiciu suma nuo 10 iki 100 2475  





# # UZDUOTIS
# # Leiskite naudotojui įvesti, kiek jis nori įvesti skaičių (pvz 7), tuomet leiskite jam įvesti tiek skaičių  kiek jis prašė ir suskaičiuokite jų vidurkį.

# # 1. Kiek skaičių vartotojas norės įvesti
# kiek = int(input("Iveskite kiek planuojate naudoti skaiciu, bet ne daugiau iki 10 vnt" ))

# # 2. Sukuriam tuščią sąrašą skaičiams
# skaiciu_sarasas = []

# # 3. Ciklas įvedimui
# for i in range(kiek):
#     skaicius = float(input(f"Iveskite skaiciu NR. {i+1}: "))
#     skaiciu_sarasas.append(skaicius)

# print("Jusu skaiciai", skaiciu_sarasas)

# suma = sum(skaiciu_sarasas)
# vidurkis = suma/kiek
# print("Skaiciu suma", suma)
# print("Vidurkis", vidurkis)

# REZULTATAS TERMINALE
# Iveskite kiek planuojate naudoti skaiciu, bet ne daugiau iki 10 vnt5
# Iveskite skaiciu NR. 1: 10
# Iveskite skaiciu NR. 2: 20
# Iveskite skaiciu NR. 3: 30
# Iveskite skaiciu NR. 4: 40
# Iveskite skaiciu NR. 5: 50
# Jusu skaiciai [10.0, 20.0, 30.0, 40.0, 50.0]
# Skaiciu suma 150.0
# Vidurkis 30.0