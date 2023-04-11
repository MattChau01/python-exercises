# importing functions from python library
import random


def get_choices():

  player_choice = input("Enter a choice (rock, paper, scissors): ")

  options = ['rock', 'paper', 'scissors']

  computer_choice = random.choice(options)

  choices = {
    'player choice': player_choice,
    'computer choice': computer_choice
  }

  return choices


choices = get_choices()

print(choices)

# a list can be made by creating a variable and assigning a list of elements inside a bracket
# EXAMPLE
# food = ['pizza', 'carrots', 'eggs']
# we can use the random method that was imported at the top to randomly assign an element as such:
# dinner = random.choice(food)
