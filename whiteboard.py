# https://www.codewars.com/kata/550554fd08b86f84fe000a58/python <-- link
# Write a function that takes two arrays of strings as input, a1 and a2. The function should 
# return an array r that contains all of the strings in a1 that are substrings of strings in a2, 
# sorted in lexicographical order.

# Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# solution(a1,a2) -> returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# solution(a1,a2) -> returns []

def solution(a1, a2):
    output = []
    for word in a1:
        if word in output:
            continue
        for check_word in a2:
            if word in check_word:
                output.append(word)
                break
    return sorted(output)


# def solution(a1, a2):
#     a2 = '.'.join(a2) # O(n)
#     answer = [] # O(1)
#     for word in a1: # O(m)
#         if word in a2 and word not in answer: # O(n) + O(m)
#             answer.append(word) # O(1)
#     return answer # O(1)

