"""
Check if removing one character makes remaining to have equal frequencies in the input string.
Example:
aaac => aaa - OK
aabbd => aabb - OK
abc => ab - OK
aaabbbcccd => aaabbbccc
There are two cases when removing a character to have equal frequencies in the input:
a) the removal reduces total number of characters and number of individual characters - basically one factor is reduced
to zero.
b) the removal reduces total number of characters but number of individual letters remains.
ad. a)
factor = (input_length - 1) / (total_chars - 1)
ad. b)
factor = (input_length -1 ) / total_chars
In both cases the only valid number is an integer as we cannot have 0.77 of a letter :).
1. Calculate both factors and see which one is an integer.
2. Check if the frequency in the dictionary matches the calculation - profit.
"""


def solve(s):
    # find frequencies
    frequencies = {}
    for char in s:
        if frequencies.get(char):
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    total_chars = len(frequencies)
    factor_reduced_unique_chars = None
    if total_chars > 1:
        factor_reduced_unique_chars = (len(s) - 1) / (total_chars - 1)
        print(factor_reduced_unique_chars)
    factor_reduced_total_chars = (len(s) - 1) / total_chars
    print(factor_reduced_total_chars)
    required_factor = None
    if factor_reduced_unique_chars and factor_reduced_unique_chars % 1 == 0:
        required_factor = factor_reduced_unique_chars
    elif factor_reduced_total_chars % 1 == 0:
        required_factor = factor_reduced_total_chars
    if not required_factor:
        return False
    print(required_factor)


solve('accaa')
