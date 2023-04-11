def get_choices():

  player_choice = 'rock'
  computer_choice = 'paper'

  # a dictionary of choices is being made, using the local variables decalared above
  choices = {'player': player_choice, 'computer': computer_choice}

  return player_choice + ' and ' + computer_choice


choices = get_choices()

print(choices)

# KEY PAIRS: key is equivalent to the property (name) of an object (dict), and the value is the value of the key (beau)
# EXAMPLE:
# dict = {'name': 'beau', 'color': 'blue'}
