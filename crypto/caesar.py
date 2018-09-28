from helpers import alphabet_position, rotate_character  #Import functions to help with encryption from helpers.py

#Create dictionaries for lowercase and uppercase letters
lower_case_dict = dict()
upper_case_dict = dict()


def create_lower(lower_string):
#Function to create lower case dictionary [a==0, z==25]
    dict_index = 0
    for c in lower_string:
        lower_case_dict[dict_index] = c
        dict_index += 1


def create_upper(upper_string):
#Function to create lower case dictionary [A==0, Z==25]
    dict_index = 0
    for c in upper_string:
        upper_case_dict[dict_index] = c
        dict_index += 1



def encrypt(text, rot):
#Encrypt all alphabetic charcters using the rotation amount provided.
#rotate_charcter is called from helpers.py
    new_text = ''
    for c in text:
        if c.isalpha() == True:
            new_text += rotate_character(c, rot)
        else:
            new_text += c
    return new_text



def main():
    create_lower('abcdefghijklmnopqrstuvwxyz')
    create_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    message = input("Type a message: ")  #Get message to encrypt
    rotate = int(input("Rotate by: "))   #Get the number of characters to rotate by
    encrypted_message = encrypt(message, rotate)
    print(encrypted_message)             #Print encrypted message returned from encrypt function

if __name__ == "__main__":
    main()
    