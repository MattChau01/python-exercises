# Ternary operators

## ternarys are used for shorthand conditional comparisons

## a different example are useage of if else statements to conditionally return
## EXAMPLE:
# def is_adult(age):
#   if age > 18:
#     return True
#   else:
#     return False

# ternary format:

age = input('Enter your age: ')
# User inputs '24'

user_input = int(age)
# Input is turned into an integer


def is_adult(user_input):
    return True if user_input > 18 else False


print(is_adult(user_input))

# returns True
