import cProfile
from runner import *

def main():
  max_debit()
  

if __name__ == '__main__':
    cProfile.run('main()')