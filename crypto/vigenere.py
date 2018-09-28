
#Encrypts text using the vignere algorithm (https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

from helpers import alphabet_position, rotate_character  #import alphabet_position and rotate_character from helpers.py

lower_case_dict = dict()   #create dictionary for lowercase letters
upper_case_dict = dict()   #create dictionary for uppercase letters

def create_lower(lower_string):
#fill in the lower case dictionary where [a==0, z==25]
    dict_index = 0
    for c in lower_string:
        lower_case_dict[dict_index] = c
        dict_index += 1

def create_upper(upper_string):
#fill in the lower case dictionary where [A==0, Z==25]
    dict_index = 0
    for c in upper_string:
        upper_case_dict[dict_index] = c
        dict_index += 1

def encrypt(text, rot):
#Encrypts the text, uses helpers.rotate_character()
    rotation_list = list()  #create the list that will store the numbers to rotate for each character in cypher
    rotation_num = 0
    new_text = ''
    for i in rot:
        #use the rotation_list to store the position of each letter in the cypher word used
        rotation_list.append(alphabet_position(i))
        print(rotation_list)
    for c in text:
        if c.isalpha() == True:
            try:
                #rotate the character by the amount given in the rotation_list
                rotation = rotation_list[rotation_num]
                new_text += rotate_character(c, rotation)
                rotation_num += 1  #move to the next amount in rotation list
            except IndexError:
                #if rotation_num is moved out of the rotation_list index reset to 0
                rotation_num = 0
                rotation = rotation_list[rotation_num]
                new_text += rotate_character(c, rotation)
                rotation_num += 1
        else:
            #if not alphabetic charcter do not change
            new_text += c

    return new_text








def main():
    create_lower('abcdefghijklmnopqrstuvwxyz')
    create_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    message = input("Type a message: ")
    rotate = input("Encryption string: ")
    encrypted_message = encrypt(message, rotate)
    print(encrypted_message)

if __name__ == "__main__":
    main()

