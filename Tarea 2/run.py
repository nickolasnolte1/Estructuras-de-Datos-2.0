from Practica2 import *

while(True):
    menu()
    user = input("\n> ")
    if True:
        if(int(user) ==1):
            agregar_debitos()
        if(int(user) == 2):
            agregar_creditos()
        if(int(user) == 3):
            total_debitos()
        if(int(user) == 4):
            totalCreditosf()
        if(int(user) == 5):
            saldo()
        if(int(user) == 6):
            promedioDebitos()
        if(int(user) == 7):
            debitoGrande()
        if(int(user) == 8):
            registro()
        if(int(user) == 9):
            print()
        if(int(user) <=0 | int(user) > 10):
            break
    else:
        break