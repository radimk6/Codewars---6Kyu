# Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
# without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

# test.assert_equals(unique_in_order(""), [])
# test.assert_equals(unique_in_order([]), [])
# test.assert_equals(unique_in_order(()), [])
# test.assert_equals(unique_in_order("A"), ["A"])
# test.assert_equals(unique_in_order(["A"]), ["A"])
# test.assert_equals(unique_in_order(("A",)), ["A"])
# test.assert_equals(unique_in_order("AA"), ["A"])
# test.assert_equals(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])
# test.assert_equals(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])
# test.assert_equals(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
# test.assert_equals(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])

def unique_in_order(sequence):
  if len(sequence) == 0:
    return []
  else:
    unique_number = sequence[0]
    for x in range(len(sequence)):
      if sequence[x] != unique_number:
        unique_number.append(sequence[x])
    return unique_number
    
print(unique_in_order([1, 2, 3, 3, -1]))