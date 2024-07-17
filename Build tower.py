# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

# test.assert_equals(tower_builder(1), ['*', ])
# test.assert_equals(tower_builder(2), [' * ', '***'])
# test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])

def tower_builder(n_floors):
  x = 1
  y = "*"
  space = " "
  spaces = (n_floors - 1)
  tower = []
  for one_floor in range(1, n_floors + 1):
    floors = (f"{spaces * space}{x * y}{spaces * space}")
    tower.append(floors)
    x += 2
    spaces -= 1
    
  return tower

print(tower_builder(3))