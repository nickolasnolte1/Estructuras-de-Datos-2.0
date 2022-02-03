from Practica2 import *
import cProfile

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
            total_creditos()
        if(int(user) == 5):
            saldo()
        if(int(user) == 6):
            promedio_debitos()
        if(int(user) == 7):
            max_debit()
        if(int(user) == 8):
            print()
        if(int(user) <=0 | int(user) > 10):
            break
    else:
        break

def main():
  saldo()

  
  

if __name__ == '__main__':
    cProfile.run('main()')