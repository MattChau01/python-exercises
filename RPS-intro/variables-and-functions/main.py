# the string 'rock' is being assigned to variable name
# 'player_choice' (python uses underscore to space out)

# indenting variables under a function makes it local to that function


def get_choices():

  player_choice = 'rock'
  computer_choice = 'paper'

  # return player_choice
  # return computer_choice
  return player_choice + ' and ' + computer_choice


choices = get_choices()

print(choices)
