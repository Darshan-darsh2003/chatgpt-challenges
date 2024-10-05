'''
Task 2: Array Pair Sum
    Write a function that, given an array of integers and a target sum, returns all the unique pairs of numbers from the array that add up to the target sum.

Requirements:
Return the pairs as a list of tuples.
    Each pair should only appear once, even if there are duplicate numbers in the array.
    You can assume the array will contain at least two numbers.
Example Input:
    arr = [2, 4, 3, 5, 7, 8, 1, 9, -2]
    target = 7
Expected Output:
    [(2, 5), (3, 4), (8, -1)]

Constraints:
    Try to implement this efficiently, aiming for O(n) time complexity.
    Avoid using the same element twice in the pair.
'''

from typing import List, Tuple

def arrayToPair(values: List[int],sum: int) -> List[Tuple[int, int]]:
    tupleArray:List[Tuple[int,int]] = []
    for value in values:
        pass

'''
    Failed to Complete

    ChatGpt result:
    Approach:
        Use a set to store the values we've already seen.
        As you iterate through the array, for each number, check if the difference between the target sum and the current number has been seen before. If it has, you've found a pair.
        Store the pairs in a list to return as the result.
'''
from typing import List, Tuple

def arrayToPair(values: List[int], target: int) -> List[Tuple[int, int]]:
    # Set to store the seen values
    seen = set()
    # List to store the result pairs
    result: List[Tuple[int, int]] = []
    
    for value in values:
        # Calculate the complement that would make the pair sum to target
        complement = target - value
        
        # Check if the complement exists in the set of seen values
        if complement in seen:
            # If it exists, this is a valid pair
            result.append((complement, value))
        
        # Add the current value to the set of seen values
        seen.add(value)
    
    return result

# Example usage
arr = [2, 4, 3, 5, 7, 8, 1, 9, -2]
target = 7
print(arrayToPair(arr, target))  # Output: [(5, 2), (4, 3), (-2, 9)]


'''
Explanation:
    seen = set(): This keeps track of the numbers we've already processed. Using a set ensures that checking for the complement (complement in seen) happens in O(1) time.

    Complement Calculation: For each value, the complement is target - value. We check if this complement has already been seen in the set. If it has, we add the pair (complement, value) to the result.

    Store the Result: Every time a valid pair is found, it's added to the result list. We use a list of tuples for the pairs.

    Efficiency: This approach runs in O(n) time, where n is the length of the input list, because each number is processed once.

Example:
    For arr = [2, 4, 3, 5, 7, 8, 1, 9, -2] and target = 7:

    First, 2 is checked. The complement is 5 (because 7 - 2 = 5), but 5 is not in seen yet, so 2 is added to seen.
    Then 4 is checked. The complement is 3, but 3 is not in seen yet, so 4 is added to seen.
    When we reach 3, its complement is 4 (which is in seen), so (4, 3) is added to the result.
    This process continues until all valid pairs are found.
'''