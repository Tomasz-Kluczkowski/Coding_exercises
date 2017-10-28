# Merged String Checker

At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 are in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears

#Looking for:
Can strings be merged into string s?

#Specification:

- characters can only be used in the same order
- is_merge should return True if part1 & part2 can be merged, False otherwise

#Sample tests:
Test.expect(is_merge('codewars', 'code', 'wars'));
Test.expect(is_merge('codewars', 'cdw', 'oears'));
Test.expect(not is_merge('codewars', 'cod', 'wars'));

#Initial thoughts:
- validation ? All characters present is same quantities ?
- the first character in any of the parts must be the one we look for now in the complete string.