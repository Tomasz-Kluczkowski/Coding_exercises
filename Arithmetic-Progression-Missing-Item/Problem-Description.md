# Give me a Diamond

Find the missing term in an Arithmetic Progression.

#Task:

An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: Exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function findMissing (list) , list will always be at least 3 numbers. The missing term will never be the first or last one.

Example :

findMissing([1,3,5,9,11]) == 7

#Looking for:
A missing item in the arithmetic progression.

#Specification:

- The input is always minimum 3 items.
- Only one item is missing.
- The missing item is never the first or the last item.

#Basic Test Case:

findMissing([1,3,5,9,11]) == 7


#Initial thoughts:
- The difference between consecutive items must be the same.
- The location of the missing item is not known.
- The difference between the sum of items present and the complete sum is the missing item.
- sum_complete = (n+1)*(n1 + nlast)/2



