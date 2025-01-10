import functions
import time
import os

rajzok = {
    "000":{"név":"Kilépés"},
    "001":{"név": "Háromszög"},
    "002":{"név": "Négyszög"},
    "003":{"név": "Kör"},
    "004":{"név": "Csillag"},
    "005":{"név": "Koch-görbe"}
}

user = ""
while user != "000":
    os.system('cls')
    for szotar in rajzok:
        print(f"{szotar} - {rajzok[szotar]["név"]}")
    user = input("Adja meg melyik rajzot szeretné látni: ")
    if user =="000":
        print("Kilépés", end="")
        for _ in range(3):
            print(".", end="")
            time.sleep(1)
    elif user == "001":
        functions.haromszog()
    elif user == "002":
        functions.negyszog()
    elif user == "003":
        functions.kor()
    elif user == "004":
        functions.csillag()
    elif user == "005":
        functions.indito()
    else:
        continue