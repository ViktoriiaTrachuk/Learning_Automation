# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example

# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# Input validation

# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.

def sum_array(arr):
    if not arr or len(arr) <=3:
            return 0
    highest = max(arr)
    lowest = min(arr)
    sum_except_edges = 0
    for i in arr:
          if i != highest and i != lowest:
                sum_except_edges += i
    return sum_except_edges
        
print(sum_array([1, 2, 2, 2, 3]))

"""
def sum_array(arr):
      if not arr or len(arr) <=2:
            return 0
      arr.remove(max(arr))
      arr.remove(min(arr))

      return sum(arr)

print(sum_array([1, 2, 2, 2, 3]))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([6, 2, 1, 8, 10]))

def sum_array(arr):
      if not arr or len(arr) <=2:
            return 0
      sorted_arr = sorted(arr)
      filtered_arr = sorted_arr[1:-1]
      return sum(filtered_arr)
print(sum_array([1, 2, 2, 2, 3]))
print(sum_array([1, 1, 11, 2, 3]))
print(sum_array([6, 2, 1, 8, 10]))
"""
    #your code here