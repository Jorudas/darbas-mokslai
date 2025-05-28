




# # siandien = datetime.datetime.today()
# # siandien_data = datetime.date.today()
# # siandien_laikas = datetime.datetime.today().time()

# # print(siandien)
# # print(siandien_data)
# # print(siandien_laikas)
# # print("" + "-" * 20)

# # mano_data = datetime.datetime(2023, 10, 1, 12, 0, 0)

# # print(mano_data.strftime("%B %A"))


# # text = "2023-10-01 12:00:00"

# # data = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S")



# # print(data.year)




# # print("tekstas ", str(type(text)))
# # print("data " + str(type(data)))

# # print(data)

# text = input("Iveskite data(yyyy-mm-dd): ")
# # metai = int(input("Iveskite data(yyyy): "))
# # menesis = int(input("Iveskite data(mm): "))
# # diena = int(input("Iveskite data(dd): "))


# # print(metai, menesis, diena)
# data = datetime.datetime.strptime(text, "%Y-%m-%d")

# # print(type(text))
# # print(type(data))

# # print(data)
# # print(data.year)    

# skirtumas = datetime.datetime.now() - data

# print("Skirtumas: ", type(skirtumas))
# print(skirtumas.days)




# UZDUOTIS NR 1
# Sukurkite sąrašą iš kelių skirtingų tipų elementų string, bool, int, float (galite įterpti ir daugiau tipų), sukurkite ciklą,
#       kuris paimtų visus skaičius (int ir float) ir išvestų jų sumą.
# Parašyti programą, kuri:
# Leistų vartotojui įvesti sveiką skaičių.
# Atspausdintų True, jei skaičius teigiamas.
# Atspausdintų False, jei skaičius neigiamas ar lygus 0.
# True / False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar_skaicius_teigiamas.
# Patarimas: naudoti input, boolean, if/else.

# 1ma dalis sprendimo: sąrašas ir skaičių suma
# mano_sarasas = (True, False, 3, 4.5, 'namas')
# #CIKLAS
# suma = 0
# for elementas in mano_sarasas:
#     if type(elementas) == int or type(elementas) == float:
#         suma += elementas 
# print("Skaiciu suma: ", suma)
# REZULTATAS TERMINALE 
# Skaiciu suma:  7.5

# 2 dalis sprendimo: tikriname vartotojo ivesta skaiciu
# try:
#     Vart_ivestis = int(input("Iveskite sveika skaiciu: "))
#     ar_skaicius_teigiamas = Vart_ivestis > 0
#     print(ar_skaicius_teigiamas)  # jei istrinsime sia eilute, tada nebus rasomi FALSE arba True

#     if ar_skaicius_teigiamas:
#         print ("Skaicius teigiamas")
#     else:
#         print("skaicius yra neigiamas")
# except ValueError:
#     print("Ivedete ne skaiciu, bandykite dar karta!!")
# REZULTATAS TERMINALE
# 1) Iveskite sveika skaiciu: -3
# False
# skaicius yra neigiamas
# 2) Iveskite sveika skaiciu: 2
# True
# Skaicius teigiamas
# 3) Iveskite sveika skaiciu: KAunas
# Ivedete ne skaiciu, bandykite dar karta!!


# UZDUOTIS NR 2
# Parašyti programą, kuri:
# Atspausdintų dabartinę datą ir laiką.
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų.
# Pridėtų prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų.
# Atspausdintų dabartinę datą ir laiką tokiu formatu:
# 2019 03 08, 09:57:17
# Patarimas: naudoti
# datetime, timedelta
# (from datetime import timedelta)






# UZDUOTIS NR 3
# Parašyti programą, kuri:
# Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį).
# Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# Metų
# Mėnesių
# Dienų
# Valandų
# Minučių
# Sekundžių
# Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t. t. paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, .days, .total_seconds()
# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):
# skaicius = 4.66
# print(round(skaicius))



# UZDUOTIS NR 4
# Pakeisti 1 ir 3 užduotis taip, kad neteisingai įvedus duomenis ar įvykus klaidoms,
# programos mestų norimas klaidas lietuvių kalba (panaudoti try/except).
   