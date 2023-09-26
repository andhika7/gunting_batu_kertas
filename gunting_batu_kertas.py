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

game_images = [rock, paper, scissors]
game_words = ["batu","kertas","gunting"]

#Write your code below this line 👇
print("Welcome to rock, paper, scissors game!")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n")

if int(user_choice)>=3 or int(user_choice)<0:
    print("you type an invalid number, you lose")
else:
    print(f"you choose: {game_words[int(user_choice)]}")
    print(game_images[int(user_choice)])
    # computer_choice = 2
    computer_choice = random.randint(0,2)
    print(f"computer choose: {game_words[int(computer_choice)]}")
    print(game_images[int(computer_choice)])
    
    # 0 for Rock, 1 for Paper, or 2 for Scissors
    if int(user_choice)>int(computer_choice):
        if int(user_choice)==2 and int(computer_choice)==0:
            print("you lose")
        else:
            print("you win")
    elif int(user_choice)<int(computer_choice):
        if int(user_choice)==0 and int(computer_choice)==2:
            print("you win")
        else:
            print("you lose")
    else:
        print("its draw")