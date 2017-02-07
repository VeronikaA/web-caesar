import string
# helper function 1, returns numerical key of letter input by user
def alphabet_position(letter):
    """ Creates key by receiving a letter and returning the 0-based numerical position of that letter in the alphabet, regardless of case."""
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    alphabet1 = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase
    i = 0
    for c in alphabet:
        key = 0
        c = letter
        if c in alphabet1:
            ascii_value = ord(c)
            c = ascii_value
            key = (c - 97) % 26
        elif c in alphabet2:
            ascii_value = ord(c)
            c = ascii_value
            key = (c - 65) % 26
        elif c not in alphabet:
            key = ord(c)
        return key
        
# helper funtion 2
def rotate_character(char, rot):
    """Receives a character 'char', and an integer 'rot'. 
    Returns a new char, the result of rotating char by rot number of places to the right."""
    a = char
    a = alphabet_position(a)
    rotation = (a + rot) % 26
    if char in string.ascii_lowercase:
        new_char = rotation + 97
        rotation = chr(new_char)
    elif char in string.ascii_uppercase:
        new_char = rotation + 65
        rotation = chr(new_char)
    elif char == char:
        rotation = char
    return rotation
