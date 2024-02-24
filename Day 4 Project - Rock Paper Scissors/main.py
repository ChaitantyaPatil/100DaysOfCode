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
move = [rock,scissors,paper]
print("******** Welcome To Game *******")
print("""
1.Rock
2.Scissors
3.Paper
""")
user_move = int(input())
print(move[user_move-1])

print("computer chose : ")
computer_move = random.randint(1,3)
print(move[computer_move-1])

#Rock wins against scissors; paper wins against rock; and scissors wins against paper
# rock > scissors > paper

if user_move==1 and computer_move ==2 :
    print("YOU WIN")
elif user_move==2 and computer_move == 3:
    print("YOU WIN")
elif user_move == 3 and computer_move == 1:
    print("YOU LOSE")
elif user_move == computer_move:
    print("TIE")
else:
    print("YOU LOSE")
