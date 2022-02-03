import cProfile
from runner import *

def main():
  saldo()
  agregar_creditos()
  agregar_debitos()
  total_debitos()
  total_creditos()
  promedio_debitos()
  max_debit()
  registro()

  
  

if __name__ == '__main__':
    cProfile.run('main()')