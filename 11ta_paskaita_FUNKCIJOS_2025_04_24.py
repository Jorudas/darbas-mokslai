# UZDUOTIS NR 1
# Sukurkite 4 matematines funkcijas kurios gražina atsakymus (sudetis, atimtis, daugyba, dalyba)

# def sudetis (a, b):
#    return a + b

# def atimtis (a, b):
#    return a - b

# def daugyba (a, b):
#    return a * b

# def dalyba (a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Negalima dalinti is nulio!"

# a = int(input("iveskite pirma skaiciu: "))
# b = int(input("iveskite antra skaiciu: "))

# print("Sudetis:", sudetis(a, b))
# print("atimtis:", atimtis(a, b))
# print("daugyba:", daugyba(a, b))
# print("dalyba:", dalyba(a, b))

# REZULTATAS TERMINALE
# iveskite pirma skaiciu: 2
# iveskite antra skaiciu: 0
# Sudetis: 2
# atimtis: 2
# daugyba: 0
# dalyba: Negalima dalinti is nulio!




# UZDUOTIS NR 2
# Sukurkite Funkcija kuri grąžina didesnį iš dviejų paduotų skaičių.

# def kuris_didesnis (a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# a = int(input("iveskite A skaiciu: "))
# b = int(input("iveskite B skaiciu: "))

# rezultatas = kuris_didesnis (a, b)
# print ("Didesnis skaicius yra: ", rezultatas)

# REZULTATAS TERMINALE 
# iveskite A skaiciu: 4
# iveskite B skaiciu: 5
# Didesnis skaicius yra:  5




# UZDUOTIS NR 3 
# Funkcija kuri apskaičiuoja stačiakampio plotą.

# def staciakampio_plotis (ilgis, plotis):
#     return ilgis * plotis

# ilgis = int(input("iveskite staciakampio ilgi: "))
# plotis = int(input("iveskite staciakampio ploti: "))

# plots = staciakampio_plotis (ilgis, plotis)
# print("Staciakamio plotis yra: ", plots)

# REZULTATAS TERMINALE 
# iveskite staciakampio ilgi: 10
# iveskite staciakampio ploti: 20
# Staciakamio plotis yra:  200




# UZDUOTIS NR 4
# Funkcija kuri apskaičiuoja trijų skaičių vidurkį.
# def skaiciu_vidurkis(a, b, c):
#     return (a + b + c)/3

# a = int(input("iveskite A skaiciu: "))
# b = int(input("iveskite B skaiciu: "))
# c = int(input("iveskite C skaiciu: "))

# rezultatas = skaiciu_vidurkis(a, b, c)
# print("3ju skaiciu plotas yra: ", rezultatas)

# REZULTATAS TERMINALE 
# iveskite A skaiciu: 6
# iveskite B skaiciu: 8
# iveskite C skaiciu: 10
# 3ju skaiciu plotas yra:  8.0



# #  UZDUOTIS NR 4
# # Patikrinti ar skaičius lyginis
# def ar_skaicius_lyginis(a):
#     return a % 2 == 0

# Skaicius = int(input("iveskite skaiciu: "))
# if ar_skaicius_lyginis(Skaicius):
#     print("Skaicius yra lyginis")
# else:
#     print("Skaicius yra nelyginis")

# REZULTATAS TERMINALE
# iveskite skaiciu: 10
# Skaicius yra lyginis



    
#  UZDUOTIS NR 5
# Funkcija kuri suskaičiuoja, kiek kartų nurodyta raidė pasikartoja tekste.
# def skaiciuoti_raides_kieki(tekstas, raide):
#     return tekstas.count(raide)
# tekstas = input("Iveskite texta: ")
# raide = input("Iveskite raide, kuria norite suskaiciuoti: ")
# kiek = skaiciuoti_raides_kieki(tekstas, raide)
# print(f"Raidė '{raide}' tekste pasikartoja {kiek} kartus.")
# REZULTATAS TERMINALE:
# Iveskite texta: Labas vakaras
# Iveskite raide, kuria norite suskaiciuoti: a
# Raidė 'a' tekste pasikartoja 5 kartus.




# #  UZDUOTIS NR 6
# Sukurkite funkciją, kuri sveikina vartotoją. 
# Funkcija turi priimti vartotojo vardą kaip privalomą parametrą ir pasveikinimo tekstą kaip neprivalomą parametrą.
# Jeigu pasveikinimo tekstas nenurodytas, naudokite numatytąjį tekstą "Labas".

# def pasveikinti(vardas, pasveikinimas="LABAS"):
#     print(f"{pasveikinimas}, {vardas}!")

# vardas = input("Iveskite savo varda: ")
# pasveikinimas = input("Iveskite pasveikinimo texta (jei paliksite tuscia, bus 'LABAS'): ")
# if pasveikinimas == "":
#     pasveikinti(vardas)
# else:
#     pasveikinti(vardas, pasveikinimas)
# REZULTATAS TERMINALE:
# Iveskite savo varda: Kestutis
# Iveskite pasveikinimo texta (jei paliksite tuscia, bus 'LABAS'): 
# LABAS, Kestutis!



# UZDUOTIS NR 7
# Sukurkite funkciją, kuri apskaičiuoja prekės kainą su PVM. 
# Funkcija turi priimti prekės kainą kaip privalomą parametrą ir PVM tarifą kaip neprivalomą parametrą. 
# Jeigu PVM tarifas nenurodytas, naudokite 21%.
# def kaina_su_pvm (kaina, pvm=21):
#     return kaina + (kaina * pvm / 100)
# kaina = float(input("Iveskite prekes kaina be PVM: "))
# pvm_ivedimas = input("Iveskite PVM tarifa - jei paliksite tuščią, bus 21%): ")
# if pvm_ivedimas == "":
#     galutine_kaina = kaina_su_pvm(kaina)
# else:
#     pvm = float(pvm_ivedimas)
#     galutine_kaina = kaina_su_pvm(kaina, pvm)
# print(f"Kaina su PVM yra: {galutine_kaina} €")
# REZULTATAS TERMINALE:
# Iveskite prekes kaina be PVM: 10
# Iveskite PVM tarifa - jei paliksite tuščią, bus 21%): 
# Kaina su PVM yra: 12.1 €



# UZDUOTIS NR 8
# Sukurkite funkciją, kuri pakelia skaičių nurodytu laipsniu. 
# Funkcija turi priimti skaičių kaip privalomą parametrą ir laipsnį kaip neprivalomą parametrą. 
# Jeigu laipsnis nenurodytas, kelkite kvadratu.

# def kelti_laipsniu(skaicius, laipsnis=2):
#     return skaicius ** laipsnis

# skaicius = float(input("Įveskite skaičių, kurį norite kelti laipsniu: "))
# laipsnio_ivedimas = input("Įveskite laipsnį (jei paliksite tuščią, bus keliamas kvadratu): ")
# if laipsnio_ivedimas == "":
#     rezultatas = kelti_laipsniu(skaicius)
# else:
#     laipsnis = int(laipsnio_ivedimas)
#     rezultatas = kelti_laipsniu(skaicius, laipsnis)
# print(f"Rezultatas: {rezultatas}")
# REZULTATAS TERMINALE:
# Įveskite skaičių, kurį norite kelti laipsniu: 30
# Įveskite laipsnį (jei paliksite tuščią, bus keliamas kvadratu): 
# Rezultatas: 900.0




# UZDUOTIS NR 9
# Sukurkite funkciją, kuri suformuoja vartotojo pilną vardą. 
# Funkcija turi priimti vardą ir pavardę kaip privalomus parametrus ir
# kreipinį (p., dr., prof.) kaip neprivalomą parametrą.

# def pilnas_vardas(vardas, pavarde, kreipinys=""):
#     if kreipinys == "":
#         return f"{vardas} {pavarde}"
#     else:
#         return f"{kreipinys} {vardas} {pavarde}"

# vardas = input("Įveskite savo vardą: ")
# pavarde = input("Įveskite savo pavardę: ")
# kreipinys = input("Įveskite kreipinį (P., Dr., Prof.) arba palikite tuščią: ")

# rezultatas = pilnas_vardas(vardas, pavarde, kreipinys)
# print("Pilnas vardas:", rezultatas)
# REZULTATAS TERMINALE:
# Įveskite savo vardą: Kestutis
# Įveskite savo pavardę: Jorudas
# Įveskite kreipinį (P., Dr., Prof.) arba palikite tuščią: P.
# Pilnas vardas: P. Kestutis Jorudas





# UZDUOTIS NR 10
# Sukurkite funkciją, kuri apskaičiuoja atlyginimą atskaičius mokesčius. 
# Funkcija turi priimti atlyginimą "ant popieriaus" kaip privalomą parametrą ir mokesčių tarifą kaip neprivalomą parametrą.
# Jeigu mokesčių tarifas nenurodytas, naudokite 20%.
# def atlyginimas_i_rankas(ant_popieriaus, mokestis=20):
#     return ant_popieriaus - (ant_popieriaus * mokestis / 100)
# atlyginimas = float(input("Įveskite atlyginimą 'ant popieriaus': "))
# mokesciu_ivedimas = input("Įveskite mokesčių tarifą (jei paliksite tuščią, bus 20%): ")

# if mokesciu_ivedimas == "":
#     i_rankas = atlyginimas_i_rankas(atlyginimas)
# else:
#     mokestis = float(mokesciu_ivedimas)
#     i_rankas = atlyginimas_i_rankas(atlyginimas, mokestis)

# print(f"Atlyginimas 'į rankas' yra: {i_rankas} €")

# REZULTATAS TERMINALE:
# Įveskite atlyginimą 'ant popieriaus': 8000
# Įveskite mokesčių tarifą (jei paliksite tuščią, bus 20%): 21
# Atlyginimas 'į rankas' yra: 6320.0 €


# ---------------------------------------------


# UZDUOTIS NR 11
# Sukurkite funkciją, kuri generuoja sąrašą skaičių nuo pradžios iki pabaigos. 
# Funkcija turi priimti pabaigos skaičių kaip privalomą parametrą ir pradžios skaičių bei žingsnį kaip neprivalomus
# parametrus. 
# Jeigu pradžios skaičius nenurodytas, pradėkite nuo 0. Jeigu žingsnis nenurodytas, naudokite 1.

# def generuoti_sarasa(pabaiga, pradzia=0, zingsnis=1):
#     return list(range(pradzia, pabaiga, zingsnis))

# pabaiga = int(input("iveskite pabaigos skaiciu: "))
# pradzia = input("Iveskite pradzios skaiciu (galima palikti ir tuscia): ")
# zingsnis = input("Iveskite zingsni(galima palikti ir tuscia): ")

# if pradzia == "":
#     pradzia = 0
# else:
#     pradzia = int(pradzia)

# if zingsnis == "":
#     zingsnis = 1
# else:
#     zingsnis = int(zingsnis)

# sarasas = generuoti_sarasa(pabaiga, pradzia, zingsnis)
# print("Sugeneruotas sąrašas:", sarasas)

# REZULTATAS TERMINALE
# iveskite pabaigos skaiciu: 10
# Iveskite pradzios skaiciu (galima palikti ir tuscia): 1
# Iveskite zingsni(galima palikti ir tuscia): 2
# Sugeneruotas sąrašas: [1, 3, 5, 7, 9]



# -----------------------------------------------------------------


# UZDUOTIS NR 12
# Sukurkite funkciją, kuri apkerpa tekstą iki nurodyto ilgio.
# Funkcija turi priimti tekstą kaip privalomą parametrą ir maksimalų ilgį bei pabaigos simbolius 
# kaip neprivalomus parametrus. 
# Jeigu maksimalus ilgis nenurodytas, naudokite 10. Jeigu pabaigos simboliai nenurodyti, naudokite "

# # Funkcija
# def apkirpti_teksta(tekstas, max_ilgis=10, pabaigos_simboliai="..."):
#     if len(tekstas) > max_ilgis:
#         return tekstas[:max_ilgis] + pabaigos_simboliai
#     else:
#         return tekstas

# # Įvestys iš vartotojo
# tekstas = input("Įveskite tekstą: ")
# max_ilgis = input("Įveskite maksimalų ilgį (galima palikti tuščią): ")
# pabaigos_simboliai = input("Įveskite pabaigos simbolius (galima palikti tuščią): ")

# # Apdorojimas
# if max_ilgis == "":
#     max_ilgis = 10
# else:
#     max_ilgis = int(max_ilgis)

# if pabaigos_simboliai == "":
#     pabaigos_simboliai = "..."

# # Funkcijos kvietimas
# rezultatas = apkirpti_teksta(tekstas, max_ilgis, pabaigos_simboliai)

# print("Apkarpytas tekstas:", rezultatas)

# REZULTATAS TERMINALE 
# Įveskite tekstą: labas vakaras LIETUVA
# Įveskite maksimalų ilgį (galima palikti tuščią): 
# Įveskite pabaigos simbolius (galima palikti tuščią): 
# Apkarpytas tekstas: labas vaka...