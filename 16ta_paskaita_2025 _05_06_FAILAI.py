
# # ----------------------UZDUOTIS NR 1-------------------------------
# Sukurkite naują aplanką pavadinimu duomenys savo darbineje direktorijoje
# jame sukurkite failą pavadinimu vardai
# ir ten irasykite savo grupioku/kolegu vardus
# Tuomet paklauskite naudotojo ar jis nori atspausdinti vardus, jeigu jis nori atspausdinti tuomet atspausdinkite failo turini

# import os
# os.makedirs("duomenys")
# with open ("duomenys/vardai.txt", "w") as failas:
#     failas.write(("Justas\n"))
#     failas.write(("Ugne\n"))
#     failas.write(("Justas\n"))
#     failas.write(("MArius\n"))
#     failas.write(("Aš\n"))
#     failas.write(("Simonas\n"))
#     failas.write(("Dominykas\n"))
# vart_ivestis = input("Ar norite atspausdti vardus?: ")
# if vart_ivestis == "taip":
#     with open("duomenys/vardai.txt", "r") as bananas:
#         print(bananas.read())
# else:
#     print("vardai nebus atspausdinti.")

# # REZULTATAS TERMINALE
# # Ar norite atspausdti vardus?: taip
# # Justas
# # Ugne
# # Justas
# # MArius
# # Aš
# # Simonas
# # Dominykas


# ------------------------UZDUOTIS NR 2------------------------------
# Sukurti ant savo darbalaukio aplanką Pagrindinis jame sukurkite du aplankus "pirmas" ir "antras"

# REZULTATAS:
# import os
# os.makedirs("pagrindinis/pirmas")
# os.makedirs("pagrindinis/antras")



# ------------------------UZDUOTIS NR 3------------------------------
# Sukurti programą, kuri:
# •Leistų vartotojui įvesti norimą eilučių kiekį
# •Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# •Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
 
# Patarimai:
# •Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)


# def kuriamas_failas():
#     failo_pavadinimas = "pagrindinis/pirmas/" + input("Iveskite failo pavadinima: ") + ".txt"
#     eilutes = []
#     print("Įveskite tekstą po vieną eilutę.")
#     print("Paspauskite ENTER / Tuscia eilute sustabdys ivedima:")

#     while True:
#         ivestis = input()
#         if ivestis == "":
#              break
#         eilutes.append(ivestis)
#     with open (failo_pavadinimas, "w") as obuolys:
#         for eilute in eilutes:
#             obuolys.write(eilute + "\n")
#     print(f"Failas {failo_pavadinimas} SUKURTAS.")

# kuriamas_failas()
 
# REZULTATAS TERMINALE
# Iveskite failo pavadinima: MASINA
# Įveskite tekstą po vieną eilutę.
# Paspauskite ENTER / Tuscia eilute sustabdys ivedima:
# labas
# as 
# einu
# miegoti

# Failas pagrindinis/pirmas/MASINA.txt SUKURTAS.



# ------------------------------UZDUOTIS NR 4-----------------------------------------
# Sukurti programą, kuri:
# 1 Sukurtų failą „Tekstas.txt“ su pilnu tekstu "Zen of Python".
# 2 Atspausdintų tekstą iš sukurto failo
# 3 Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# 4 Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# 5 Sukurtame faile eilutę "Beautifulis better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# 6 Atspausdintų visą failo tekstą atbulai
# 7 Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# 8 Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
 
# Patarimai:
# •Naudoti from datetime import datetime, datetime.today()
# •Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
# •Kai kur galima panaudoti funkcijas iš praeitų pamok


# 1 Sukuria faila „Tekstas.txt“ su pilnu tekstu "Zen of Python".
from datetime import datetime
zen_text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


with open("Tekstas.txt", "w", encoding="utf-8") as mano_failas:
    mano_failas.write(zen_text)                                    #visas tekstas įrašomas į failą
    
# 2  Perskaito ir atspausdina teksta
with open("Tekstas.txt", "r", encoding="utf-8") as mano_failas:
    tekstas = mano_failas.readlines()                              #readlines() padaro sąrašą – kiekviena eilutė atskirai
print("ORIGINALUS TEKSTAS:\n")
for eilute in tekstas:                                   #pereik per kiekvieną „eilutę“ objekte tekstas
    print(eilute.strip())                             #.strip() – pašalina tarpus, tabuliacijas, naujas eilutes (\n, \t) nuo pradžios ir pabaigos.

# 3 Paskutinėje sukurto failo eilutėje prideda šiandienos data ir laika
siandien = datetime.today().strftime("%Y-%m-%d %H:%M:%S")           #strftime(...) sukuria datą ir laiką kaip tekstą
tekstas[-1] = tekstas[-1].strip() + " [" + siandien + "]\n"            #tekstas[-1] – paskutinė eilutė / strip() pašalina tarpus ir \n, kad nesulūžtų

# 4 Sunumeruoja teksto eilutes (kiekvienos pradzioje prideda skaičių).
sunumeruotas = [f"{i+1}. {eilute}" for i, eilute in enumerate(tekstas)]  #enumerate(...) prideda numerį prie kiekvienos eilutės

# 5 Sukurtame faile eilute "Beautifulis better than ugly." pakeicia i lietuviska "Gražu yra geriau nei bjauru."
for i in range(len(sunumeruotas)):                   # einame per visas eilutes ir  jei randame atitinkamą sakinį – jį pakeičiame lietuvišku
    if "Beautiful is better than ugly." in sunumeruotas[i]:
        sunumeruotas[i] = sunumeruotas[i].replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

# 6 Atspausdina visa failo teksta atbulai
print("\nTEKSTAS ATBULAI:\n")
for eilute in reversed(sunumeruotas):                    # apverčia eilutes #strip() pašalina nereikalingus tarpelius
    print(eilute.strip())

# 7 Atspausdina, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
tekstas_vienas = "".join(sunumeruotas)
zodziu_kiekis = len(tekstas_vienas.split())                             # split()	padalina į žodžius
skaiciu_kiekis = sum(simbolis.isdigit() for simbolis in tekstas_vienas) #isdigit()	tikrina ar simbolis – skaičius
didziosios = sum(simbolis.isupper() for simbolis in tekstas_vienas)    # isupper()	tikrina ar simbolis – didžioji raidė
mazosios = sum(simbolis.islower() for simbolis in tekstas_vienas)       # islower()	tikrina ar simbolis – mažoji raidė

print("\nSTATISTIKA:")
print("Žodžių:", zodziu_kiekis)
print("Skaičių:", skaiciu_kiekis)
print("Didžiųjų raidžių:", didziosios)
print("Mažųjų raidžių:", mazosios)

# 8 Sukuriame naują failą su DIDŽIOSIOMIS raidėmis

with open("Tekstas_DIDŽIOSIOMIS.txt", "w", encoding="utf-8") as mano_failas:
    mano_failas.writelines([eil.upper() for eil in sunumeruotas])   # upper() paverčia kiekvieną simbolį į didžiąją raidę / # writelines(...) įrašo visą sąrašą į failą

# REZULTATAS TERMINALE:
# ORIGINALUS TEKSTAS:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# TEKSTAS ATBULAI:

# 19. Namespaces are one honking great idea -- let's do more of those! [2025-05-07 21:19:59]
# 18. If the implementation is easy to explain, it may be a good idea.
# 17. If the implementation is hard to explain, it's a bad idea.
# 16. Although never is often better than *right* now.
# 15. Now is better than never.
# 14. Although that way may not be obvious at first unless you're Dutch.
# 13. There should be one-- and preferably only one --obvious way to do it.
# 12. In the face of ambiguity, refuse the temptation to guess.
# 11. Unless explicitly silenced.
# 10. Errors should never pass silently.
# 9. Although practicality beats purity.
# 8. Special cases aren't special enough to break the rules.
# 7. Readability counts.
# 6. Sparse is better than dense.
# 5. Flat is better than nested.
# 4. Complex is better than complicated.
# 3. Simple is better than complex.
# 2. Explicit is better than implicit.
# 1. Gražu yra geriau nei bjauru.

# STATISTIKA:
# Žodžių: 158
# Skaičių: 43
# Didžiųjų raidžių: 20
# Mažųjų raidžių: 630




# --------------------------------UZDUOTIS NR 5------------------------------------------------------
# Sukurti programą, kuri:
# •Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# •Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# •Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
 
# Patarimai:
# •Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_birthtime