# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

from cgi import test


def is_vowel(ch):
    if ch.upper() in ['A','E','I','O','U']:
        return True
    return False

test_case = input('Input a letter: ')
if not test_case.isalpha() or len(test_case) != 1:
    print(f'Invalid input')
else:
    if is_vowel(test_case):
        print(f'The letter {test_case} is a vowel')
    else:
        print(f'The letter {test_case} is a consonant')