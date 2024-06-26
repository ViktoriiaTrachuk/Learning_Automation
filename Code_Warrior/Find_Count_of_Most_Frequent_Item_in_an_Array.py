"""
Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
Example
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5
"""

#Using loops inside loops:
collection = [4, 2, 3, 2, 1, 4, 53, 5, 3, 5, 34, 2, 4, 4]

def most_frequent_item_count(collection):
    if not collection:
        return 0
    max_count = 0
    
    for i in range(len(collection)):
        count = 0
        for j in range(len(collection)):
            if collection[i] == collection[j]:
                count +=1
        if count > max_count:
            max_count = count
    return max_count
print(most_frequent_item_count(collection))
"""
len(collection) evaluates to 5, so range(len(collection)) generates numbers 0 to 4.
The for loop iterates through these numbers (0 to 4), and in each iteration:
i takes on the current index value (0, 1, 2, 3, 4).
collection[i] accesses the element at index i in the list collection.
"""

def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print("% d : % d" % (key, value))
print(CountFrequency([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))


def most_frequent_count(arr):
    if not arr:
        return 0
    
    frequency = {}
    
    for item in arr:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    return max(frequency.values())
print(most_frequent_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))

# # Example usage
# input_array = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# print(most_frequent_count(input_array))  # Output: 5
# """