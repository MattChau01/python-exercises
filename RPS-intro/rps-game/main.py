# importing functions from python library
import random


def get_choices():

  player_choice = input("Enter a choice (rock, paper, scissors): ")

  options = ['rock', 'paper', 'scissors']

  computer_choice = random.choice(options)

  choices = {
    'player_choice': player_choice,
    'computer_choice': computer_choice
  }

  return choices


def check_win(player, computer):

  # Concatenation:
  # print('You chose ' + player + ', and computer chose ' + computer)

  # F-string:
  print(f'You chose {player}, and computer chose {computer}')

  if player == computer:
    return ("It's a tie!")

  elif player == 'rock':
  # if statements can be nested within another if statement
    if computer == 'scissors':
      return ("Rock smashes scissors! You Win!")
    else:
      return ("Paper covers rock! You lose.")

  elif player == 'paper':
    if computer == 'rock':
      return ("Paper covers rock! You Win!")
    else:
      return ("Scissors cut paper! You lose.")

  elif player == 'scissors':
    if computer == 'paper':
      return ("Scissors cut paper! You Win!")
    else:
      return ("Rock smashes scissors! You lose.")

  # return [player, computer]


choices = get_choices()

result = check_win(choices['player_choice'], choices['computer_choice'])

print(result)

# `if and else statements`: can be used to test different scenarios. starts with `if` statement,
#  then `elif` for an else if statement and lastly an `else` statement
# EXAMPLE
# a = 20
# if age >= 18:
#   print('you are an adult')
# elif age > 12:
#   print('you are a teenager')
# elif age > 1:
#   print('you are a child')
# else:
#   print('you are a baby')


# F-strings: similar to template literals, and easier to write strings rather than using concatenation
# EXAMPLE
# age = 25
# print(f"Jim is {age} years old.")

# Indexes: use brackets on a variable to select a key value
# EXAMPLE
# choices = { 'player_choice': 'rock', 'computer_choice': 'scissors' }
# choices['player_choice'] = 'rock'
