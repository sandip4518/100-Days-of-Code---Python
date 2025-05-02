import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
y_choice=input("Enter R(rock), P(paper), S(scissors) : ").upper()
if y_choice=="R":
    y_choice=rock
elif y_choice=="P":
    y_choice=paper
else:
    y_choice=scissors
c=[rock,paper,scissors]
comp_choice=random.choice(c)
print("you choosed:\n"+y_choice)
print("Computer choosed:\n"+comp_choice)

if y_choice==comp_choice:
    print("Its a draw.")
elif y_choice==rock and comp_choice==paper:
    print("Computer Won.")
elif y_choice==rock and comp_choice==scissors:
    print("You Won.")
elif y_choice==paper and comp_choice==scissors:
    print("Computer Won.")
elif y_choice==paper and comp_choice==rock:
    print("You Won.")
elif y_choice==scissors and comp_choice==rock:
    print("Computer Won.")
elif y_choice==scissors and comp_choice==paper:
    print("you Won.")





