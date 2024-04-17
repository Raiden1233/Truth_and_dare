import random

def t_question():
   with open('t_question.txt', 'r', encoding='utf-8') as f:
      
      t_questions = f.readlines()

   return random.choice(t_questions)


if __name__ == '__main__':
   t_question()
