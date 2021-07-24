# Homework 4
# Using the make_tree function created in class as an example...
# Create a new function which generates a tree where each branch uses numbers:
#     1
#    222
#   33333
#  4444444
#     |
# The height of the tree should still be variable, however if height is > 9, the numbers should be reused from zero.
# if height = 10 then the bottom branch should use 0
# if height = 11 then the bottom branch should use 1
# if height = 12 then the bottom branch should use 2... etc.
# Bonus challenge:
#             1
#            121
#           12321
#          1234321
#         123454321
#        12345654321
#       1234567654321
#      123456787654321
#     12345678987654321
#    1234567890987654321
#   123456789010987654321
#            |

#Ellie
import random

def make_number_tree(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        print(' ' * (height_of_tree - branch) + str((branch + 1) % 10) * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')

make_number_tree()


def make_number_tree_nm(height_of_tree: int = random.randint(2, 12)):
    for branch in range(height_of_tree):
        symbol = branch + 1
        if symbol >= 10:
            symbol = symbol - 10 * int(symbol/10)
        print(' ' * (height_of_tree - branch) + str(symbol) * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')

make_number_tree_nm(12)


#mine
def make_tree(height_of_tree: int, number: int):
    for branch in range(height_of_tree):
        if number < 9:
            number = 1 + branch
            print(' ' * (height_of_tree - branch) + (str(number) * (1 + (branch * 2))))
        else:
            new_number = int(list(str(1+branch)).pop(1))
            print(' ' * (height_of_tree - branch) + (str(new_number) * (1 + (branch * 2))))
    print(' ' * height_of_tree + '|')

make_tree(21, 1)





