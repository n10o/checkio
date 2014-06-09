# A median is a numerical value separating the upper half
# of a sorted array of numbers from the lower half.
# In a list where there are an odd number of entities,
# the median is the number found in the middle of the array.
# If the array contains an even number of entities,
# then there is no single middle value, instead the median
# becomes the average of the two numbers found in the middle.
# For this mission, you are given a non-empty array
# of natural numbers (X). With it,
# you must separate the upper half of the numbers
# from the lower half and find the median.

import math

# This answer may be broken but checkio pass this program.
def checkio(data):
    data.sort()
    length = len(data)
    divide = math.floor(length/2)
    if length%2 == 0:
        return (data[divide-1]+data[divide])/2
    else:
        return data[divide]

if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    assert checkio(list(range(1000000))) == 499999.5, "Long."
