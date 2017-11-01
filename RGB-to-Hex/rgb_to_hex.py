def rgb(r, g, b):
    """Converts decimal values for color r, g, b to hexadecimal."""

    def dec_to_hex(dec):
        """Convert decimals to hexadecimals."""

        vals = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
                5: "5", 6: "6", 7: "7", 8: "8",
                9: "9", 10: "A", 11: "B", 12: "C",
                13: "D", 14: "E", 15: "F"}
        conv = []
        result = dec
        while True:
            remainder = result % 16
            result = result // 16
            remainder = vals[remainder]
            conv.append(remainder)

            if result == 0:
                conv.reverse()
                return "{:0>2}".format("".join(conv))

    output = ""

    for dec in [r, g, b]:

        if dec < 0:
            output += "00"
        elif dec > 255:
            output += "FF"
        else:
            output += dec_to_hex(dec)

    return output


