# Convert RGB to Hex.

Find the missing term in an Arithmetic Progression.

#Task:

The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

#Looking for:
Converter from RGB decimal to HEX.

#Specification:

- Valid input values are between 0 and 255.
- Values outside of the valid input should be rounded to the closest valid value.
- The missing item is never the first or the last item.

#Basic Test Case:

test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")


#Initial thoughts:
- All negative values should be turned into 0.
- All values above 255 should be turned into 255.
- Output is a string.




