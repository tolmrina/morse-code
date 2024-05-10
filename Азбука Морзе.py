MorseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '......', ',': '.-.-.-',
    ':': '---...', ';': '-.-.-.', '(': '-.--.-', '"': '.-..-.', '-': '-...._', '/': '-..-.', '_': '..--.-',
    '?': '..--..', '!': '--..--', '+': '.-.-.', '@': '.--.-.'
}


def encode_to_morse(text):
    global MorseCode
    morse_code = ''
    for char in text.upper():
        if char in MorseCode:
            morse_code += MorseCode[char] + ' '
        elif char == ' ':
            morse_code += ' '
        else:
            morse_code += char
    return morse_code.strip()


def decode_from_morse(code):
    global MorseCode
    decode_message = ''
    words = code.split('  ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in MorseCode.values():
                decode_message += list(MorseCode.keys())[list(MorseCode.values()).index(letter)]
            else:
                decode_message += letter
        decode_message += ' '
    return decode_message.strip()


def main():
    while True:
        choose = input('Hello. What do you need "encode" or "decode"? ')
        if choose.lower() == 'encode':
            message = input('Enter the text you want to encode: ')
            print(encode_to_morse(message))
        elif choose.lower() == 'decode':
            message = input('Enter the code you want to decode: ')
            print(decode_from_morse(message))
        elif choose.lower() == 'exit':
            print('Goodbye. Have a nice day.')
            break
        else:
            print('Invalid choice! Please enter "encode", "decode", or "exit".')


main()
input()