from Practica2 import *

while(True):
    menu()
    user = input("\n--> ")
    try:
        if(int(user) ==1):
            addDebitos()
        if(int(user) == 2):
            addcreditos()
        if(int(user) == 3):
            totalDebitosf()
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
            prnt()
        if(int(user) ==10):
            eliminar()
            print('Los nuevos valores son: \b')
            prnt()
            totalDebitosf()
            totalCreditosf()
            saldo()
            promedioDebitos()
            debitoGrande()
            registro()
        if(int(user) <=0 | int(user) > 10):
            break
    except ValueError:  
        break