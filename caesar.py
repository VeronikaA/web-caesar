### caesar.py ###

# import sys
from sys import argv, exit
from helpers import alphabet_position, rotate_character

def user_input_is_valid(argv):
    """Receives an array with the command-line arguments. 
    Returns a boolean indicating whether or not the user did everything correctly"""
    if len(argv) != 2:
        return False
    elif argv[1].isalpha():
        return False
    elif argv[1].isdigit() == False:
        return False
    else:
        return True

# Full Caesar function
def encrypt(text, rot):
    """Receives as input a string and an integer; rot, that specifies the rotation amount. 
    Returns the result of rotating each letter in the text by rot places to the right."""
    cypher = []
    for c in text:
        position = rotate_character(c, rot)
        cypher.append(position)
    answer = ''.join(cypher) 
    # print(answer, " ")
    return answer

def main():    
    if user_input_is_valid(argv) == False:
        print("usage: python3 caesar.py n")
        exit()
        # print("Type a message to encrypt: ")
    message = input("Type a message to encrypt: ")
    key = int(argv[1])
    crypto = encrypt(message, key)
    print(crypto)

if __name__ == '__main__':
    main()
