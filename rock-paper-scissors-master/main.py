#import random for later use in cpu choice
import random as rd

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

#place rock paper scissors as sublists in a list 
rps_list=[rock, paper, scissors]
#get user input 0,1, or 2 and covert to integer
user_choice=int(input("type 0 for rock, 1 for paper, and 2 for scissors"))
#use userchoice to print choice from rps_list of ascii
while user_choice>=3 or user_choice<0:
      print('error. Try Again!')
      user_choice=int(input("type 0 for rock, 1 for paper, and 2 for scissors"))
user_choice_ascii=(rps_list[user_choice])
print(f'User Choice:\n{user_choice_ascii}')
#select random number for cpu choice
cpu_choice=rd.randint(0,2)
#use random number to select cpu choice from rps_list
cpu_choice_ascii=(rps_list[cpu_choice])
print(f'CPU Choice:{cpu_choice_ascii}')
# use nested if stmt to create winning choice logic
if cpu_choice==user_choice:
    result='tie'
#logic for rock
elif user_choice==0:
  if cpu_choice==1:
    result='lose'
  elif cpu_choice==2:
    result='win'
#logic for paper
elif user_choice==1:
  if cpu_choice==0:
    result='win'
  elif cpu_choice==2:
    result='lose'
#logic for scissors
elif user_choice==2:
  if cpu_choice==1:
    result='win'
  elif cpu_choice==0:
    result='lose'

#print out win_lose or tie choice display
print(f'You {result}')