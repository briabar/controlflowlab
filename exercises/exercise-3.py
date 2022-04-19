# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

def dog_years(human_age):
    human_age = int(human_age)
    early_years = 0
    if human_age == 1:
        return 10
    if human_age >= 2:
        early_years += 20
    if human_age >= 2:
        return ((human_age - 2) * 7) + early_years

print(dog_years(input('Input a dog\'s age in human years: ')))