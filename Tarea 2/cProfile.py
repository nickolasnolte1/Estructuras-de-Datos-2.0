import cProfile
from programa import Practica2

def main():
  max_debit()
  saldo()
  show()
  

if __name__ == '__main__':
    cProfile.run('main()')