# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

def check_triangle():
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    triangle_set = {a,b,c}
    triangle_type = 'scalene'
    if len(triangle_set) == 1:
        triangle_type = 'equalateral'
    if len({a, b, c}) == 2:
        triangle_type = 'isosceles'
    return f'A triangle with sides of {a}, {b} & {c} is a {triangle_type} triangle'

print(check_triangle())
