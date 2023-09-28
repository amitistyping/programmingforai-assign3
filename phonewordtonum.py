#phone word to number

def phone_word_to_num(phone_word):
    # Alphabet to num map
    letter_to_number = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    result = ""

    # Iterate through each character in the input string
    for char in phone_word:
        # check is alphabet or number, any other character skip
        if char.isalnum():
            # if alphabet, map and extract number
            if char.isalpha():
                result += letter_to_number[char.upper()]
            else:
                result += char  # if digit, return as it is

    return result




