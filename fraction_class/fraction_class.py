class Fraction:

    def __init__(self, numerator, denominator):
        greates_common_denominator = self.find_greates_common_divisor(numerator, denominator)
        self.top = numerator // greates_common_denominator
        self.bottom = denominator // greates_common_denominator

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def find_greates_common_divisor(self, a, b):
        if b == 0:
            return a
        else:
            return self.find_greates_common_divisor(b, a % b)

    def __add__(self, other):
        common_denominator = self.bottom * other.bottom
        first_numerator = self.top * other.bottom
        second_numerator = other.top * self.bottom
        a = first_numerator + second_numerator
        b = common_denominator
        return Fraction(a, b)

    def __str__(self):
        return '%s/%s' % (str(self.top), str(self.bottom))


print(Fraction(4, 5))

print(Fraction(4, 8) + Fraction(8, 64))
