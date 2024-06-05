import random

def d_dare():
   with open('d_dare.txt', 'r', encoding='utf-8') as f:
      
      d_dare = f.readlines()

   return random.choice(d_dare)


if __name__ == '__main__':
   d_dare()
