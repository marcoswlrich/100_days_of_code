import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(
    input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n")
)

print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("O computador escolheu:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Você digitou um número inválido, você perdeu!")
elif user_choice == 0 and computer_choice == 2:
    print("Você venceu!")
elif computer_choice == 0 and user_choice == 2:
    print("Você perdeu")
elif computer_choice > user_choice:
    print("Você perdeu")
elif user_choice > computer_choice:
    print("Você venceu!")
elif computer_choice == user_choice:
    print("É um empate")
