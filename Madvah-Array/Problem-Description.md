# Is an array Madvah array?

A Madhav array a has the following property.

a[0] = a[1] + a[2] = a[3] + a[4] + a[5] = a[6] + a[7] + a[8] + a[9] = ...

Write a function/method named isMadhavArray/IsMadhavArray/is_madhav_array() that returns true if its array argument is a Madhav array, otherwise it returns false.

Edge cases: An array of length 0 or 1 should not be considered a Madhav array as there is nothing to compare.



#Looking for:
Write a function/method named isMadhavArray/IsMadhavArray/is_madhav_array() that returns true if its array argument is a Madhav array, otherwise it returns false.

#Specification:
- return bool

#Initial thoughts:
- check list length and eliminate those that cannot be Madvah Arrays due to incorrect length (they have too many / not enough items).
- make sure empty or single item list is rejected straight away.