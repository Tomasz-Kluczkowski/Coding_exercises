MORSE_CODE = {'..-.': 'F', '-..-': 'X',
              '.--.': 'P', '-': 'T', '..---': '2',
              '....-': '4', '-----': '0', '--...': '7',
              '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
              '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
              '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
              '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
              '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
              '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S',
              '.----': '1', '...---...': 'SOS'}


# Function and argument names are not in lowercase as that is how they need
# to be on Codewars to pass...


def decodeMorse(morseCode):
    """Convert morse code to a human readible string.

    Args:
        morseCode: (str) - Cipher in Morse code. 3 spaces between words,
            1 between letters.

    Returns:
        decoded: (str) - String in a human readible version of the cipher.
    """

    morseCode = morseCode.strip()
    words = morseCode.split('   ')

    chars_lists = [word.split() for word in words]
    decoded = ' '.join([''.join([MORSE_CODE[char] for char in char_list]) for
                        char_list in chars_lists])

    return decoded
