# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).
# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
# two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)

# sample_test_cases = [
#     #   numbers       target   valid results
#     ([1 ,2, 3],            4,  ((0,2), (2,0))),
#     ([1234,5678,9012], 14690,  ((1,2), (2,1))),
#     ([2, 2, 3],            4,  ((0,1), (1,0))),
# ]

def two_sum(numbers, target):
    valid_results = ()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
              valid_results = (i, j)
    return valid_results
  
print(two_sum([2, 2, 3], 4))