#UZDUOTIS__________________________________________
# Sukurti norimą žodyną ir juose:
# •Atspausdinti vieną norimą įrašą
# •Pridėti įrašą
# •Ištrinti įrašą
# •pakeisti įrašą
# Leiskite naudotojui pasirinkti kokį įrašą pridėti kokį ištrinti ir kokį pakeisti. 
# Pradinį žodyną su kažkiek reikšmių galite sukurti patys be naudotojo.




# # # Sukurti norimą žodyną ir juose:
# zodynas = {"kate":"juoda", "suo":"baltas", "paukstis":"melynas"}
# print(zodynas)
# #REZULTATAS TERMINALE
# {'kate': 'juoda', 'suo': 'baltas', 'paukstis': 'melynas'}


# # •Atspausdinti vieną norimą įrašą / # Paprašome naudotojo įvesti gyvūno pavadinimą
# gyvunas = input("Įveskite gyvūno pavadinimą, kurio spalvą norite sužinoti: ")
# # Tikriname, ar toks gyvūnas yra žodyne
# if gyvunas in zodynas:
#     print("Gyvūno spalva yra:", zodynas[gyvunas])
# else:
#     print("Tokio gyvūno nėra žodyne.")
# #REZULTATAS TERMINALE
# Gyvūno spalva yra: juoda



# # •Pridėti įrašą /# Paprašome naudotojo įvesti naują gyvuna ir jo spalvą
# gyvunas = input("Įveskite naują gyvūno pavadinimą: ")
# spalva = input("Įveskite šio gyvūno spalvą: ")
# # Pridedame naują įrašą į žodyną
# zodynas[gyvunas] = spalva
# # Atspausdiname atnaujintą žodyną
# print("Naujas gyvunas:", zodynas[gyvunas])
# #REZULTATAS TERMINALE
# Įveskite naują gyvūno pavadinimą: lokys
# Įveskite šio gyvūno spalvą: zalias
# Naujas gyvunas: zalias



# # •Ištrinti įrašą
# # Paprašome vartotojo nurodyti, kurį gyvūną ištrinti
# istrinti = input("Kokį gyvūną norite ištrinti? ")
# # Patikriname, ar toks įrašas egzistuoja
# if istrinti in zodynas:
#     del zodynas[istrinti]
#     print(f"Gyvūnas '{istrinti}' sėkmingai ištrintas.")
# else:
#     print("Toks gyvūnas žodyne nerastas.")
# # Atspausdiname atnaujintą žodyną
# print("Atnaujintas žodynas:", zodynas)
#REZULTATAS TERMINALE
# Kokį gyvūną norite ištrinti? suo
# Gyvūnas 'suo' sėkmingai ištrintas.
# Atnaujintas žodynas: {'kate': 'juoda', 'paukstis': 'melynas'}




# # •pakeisti įrašą / # Paprašome vartotojo pasirinkti, kurio gyvūno spalvą keisti
# gyvunas = input("kurio gyvuno spalva norite pakeiti? ")
# #Tikriname ar toks gyvunas yra zodyne
# if gyvunas in zodynas:
#     nauja_spalva = input("iveskite nauja spalva ")
#     zodynas[gyvunas] = nauja_spalva
#     print(f"{gyvunas} spalva pakeista į: {nauja_spalva}")
# # Parodome atnaujintą žodyną
# print("Atnaujintas žodynas:", zodynas)
# #REZULTATAS TERMINALE
# kurio gyvuno spalva norite pakeiti? kate
# iveskite nauja spalva geltona
# kate spalva pakeista į: geltona
# Atnaujintas žodynas: {'kate': 'geltona', 'suo': 'baltas', 'paukstis': 'melynas'}



# Leiskite naudotojui pasirinkti kokį įrašą pridėti kokį ištrinti ir kokį pakeisti. 
# Paklauskime ka vartotojas nori daryti (prideti, istrinti, pakeisti)
# veiksmas = input("kokius veiksmus norite atlikti su gyvunai, ar prideti nauja gyvuna, ar istrinti esama, ar pakeisti? ")
# if veiksmas == "prideti":
#     gyvunas = input("koki gyvuna norite prideti? ")
#     spalva = input("kokia bus gyvuno spalva? ")
#     zodynas[gyvunas] = spalva
#     print("prie iraso pridetas naujas gyvunas")
#     print("atnaujintas zodynas:", zodynas)
# #REZULTATAS TERMINALE
# {'kate': 'juoda', 'suo': 'baltas', 'paukstis': 'melynas'}
# kokius veiksmus norite atlikti su gyvunai, ar prideti nauja gyvuna, ar istrinti esama, ar pakeisti? prideti
# koki gyvuna norite prideti? vilkas
# kokia bus gyvuno spalva? geltona
# prie iraso pridetas naujas gyvunas
# atnaujintas zodynas: {'kate': 'juoda', 'suo': 'baltas', 'paukstis': 'melynas', 'vilkas': 'geltona'}



# # Pradinį žodyną su kažkiek reikšmių galite sukurti patys be naudotojo
# zodynas = {"butas": "mieste", "namas": "miske", "sodyba": "prie juros"}
# print("nekilnojamas turtas Lietuvoje:", zodynas)
# #REZULTATAS TERMINALE
# nekilnojamas turtas Lietuvoje: {'butas': 'mieste', 'namas': 'miske', 'sodyba': 'prie juros'}







# UZDUOTIS ZEN OF PHYTON
# Parašyti programą, kuri su eilute "Zen of Python, by Tim Peters„ (tai yra pirma eilutė) darytų šiuos veiksmus:
# 1) Atspausdintų paskutinį antro žodžio simbolį (situos darykite su split)
# 2) Atspausdintų pirmą trečio žodžio simbolį
# 3) Atspausdintų tik pirmą žodį (pameginkite ir su slicing pvz. tekstas[0:5]) ir su split
# 4) Atspausdintų tik paskutinį žodį
# 5) Atspausdintų visą frazę atbulai
# 6) Atskirtų žodžius ir juos atspausdintų
# 7) Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
# Patarimas: naudoti string karpymo įrankius, funkcijas split(), replace()


# # 1) Atspausdintų paskutinį antro žodžio simbolį (situos darykite su split)
# tekstas = ("Zen of Python, by Tim Peters")
# zodziai = tekstas.split()
# print(zodziai)
# antras_zodis = zodziai[1]
# paskutine_raide = antras_zodis[-1]
# print("paskutine_antro_zodzio_raide:", paskutine_raide, antras_zodis)
# print("paskutine_antro_zodzio_raide:", paskutine_raide,)
# # #REZULTATAS TERMINALE
# paskutine_antro_zodzio_raide: f


# # # 2) Atspausdintų pirmą trečio žodžio simbolį
# trecias_zodis = zodziai[2]
# pirma_raide = trecias_zodis[0]
# print("trecio zodzio pirmoji raide:", pirma_raide)
# #REZULTATAS TERMINALE
# trecio zodzio pirmoji raide: P


# # 3) Atspausdintų tik pirmą žodį su split (pameginkite ir su slicing pvz. tekstas[0:5]) 
# pirmas_zodis = zodziai[0]
# print("Atspausdinamas pirmas zodis:", pirmas_zodis)
# #REZULTATAS TERMINALE
# Atspausdinamas pirmas zodis: Zen
# # Atspausdintų tik pirmą žodį su slicing pvz. tekstas[0:5]
# pirmas_zodis_slicing = zodziai[0:1] [ 0]
# print("Atspausdinamas pirmas zodis:", pirmas_zodis_slicing)
# # #REZULTATAS TERMINALE
# Atspausdinamas pirmas zodis: Zen


# # 4) Atspausdintų tik paskutinį žodį
# paskutinis_zodis = zodziai[-1]
# print("Atspausdinamas paskutinis zodis:", paskutinis_zodis)
# REZULTATAS TERMINALE
# Atspausdinamas paskutinis zodis: Peters


# # 5) Atspausdintų visą frazę atbulai
# atbulai = tekstas[::-1]
# print("Spausdiname teksta atbulai:", atbulai)
# # REZULTATAS TERMINALE
# Spausdiname teksta atbulai: sreteP miT yb ,nohtyP fo neZ


# # 6) Atskirtų žodžius ir juos atspausdintų
# print("zodziai po viena:")
# print(zodziai)
# # # REZULTATAS TERMINALE
# ['Zen', 'of', 'Python,', 'by', 'Tim', 'Peters']


# # 7) Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
# naujas_textas = tekstas.replace("Python,", "Programming")
# print(naujas_textas)
# # # # UZDUOTIS
# Sukurti programą, kuri:
# •Leistų vartotojui įvesti metus
# •Atspausdintų „Keliamieji metai“, jei taip yra
# •Atspausdintų „Nekeliamieji metai“, jei taip yra
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų
# Zen of Programming by Tim Peters





# UZDUOTIS KELIAMIEJI METAI
# Sukurti programą, kuri:
# •Leistų vartotojui įvesti metus
# •Atspausdintų „Keliamieji metai“, jei taip yra
# •Atspausdintų „Nekeliamieji metai“, jei taip yra
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų

# #paprasome vartotojo ivesti metus
# metai = int(input("iveskite metus: "))
# # patikrinmae ar tai keliamieji metai
# if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
#     print("keliamieji metai")
# else:
#     print("nekeliamieji metai")
# # REZULTATAS TERMINALE
# # iveskite metus: 1800
# # nekeliamieji metai
# # iveskite metus: 400
# # keliamieji metai





# # UZDUOTIS
# •Sukurkite sąrašą su pasikartojančiomis reikšmėmis,
#  viena komanda pašalinkite visas šias pasikartojančias reikšmes (print galima naudoti, neribotą kiekį kartų)
# •Sukurkite du identiškus objektus (tuple ir sąrašas), 
# pamatuokite ar atspausdindami visus tuple elementus sutaupote laiko palyginus su spausdinant visus sąrašo elementus.

# •Sukurkite sąrašą su pasikartojančiomis reikšmėmis
sarasas = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
print("Pradinis sarasas:", sarasas)
# REZULTATAS TERMINALE
# Pradinis sarasas: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
#pasaliname pasikartojancias reiksmes
