import pytest

import morse_decoder

# For reference.
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

test_data = [('     -..-      ', 'X'),
             ('- . ... -   ...---...', 'TEST SOS'),
             ('.----', '1'),
             ('     .--   ---..', 'W 8'),
             ('-----        ', '0'),
             ('- --- -- .- ... --..   -.- .-.. ..- -.-. --.. -.- --- .-- ... -.- ..', 'TOMASZ KLUCZKOWSKI')]


@pytest.mark.parametrize("cipher, expected", test_data)
def test_decodeMorse(cipher, expected):
    """Test decoding morse code into human readible string."""
    assert morse_decoder.decodeMorse(cipher) == expected
