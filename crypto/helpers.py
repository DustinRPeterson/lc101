

lower_case_dict = dict()            #create lower case dictionary
upper_case_dict = dict()            #create upper case dictionary

def create_lower(lower_string):
#create lowercase dictionary where [a==0, z==25]
    dict_index = 0
    for c in lower_string:
        lower_case_dict[dict_index] = c
        dict_index += 1

def create_upper(upper_string):
#create uppercase dictionary where [A==0, Z==25]
    dict_index = 0
    for c in upper_string:
        upper_case_dict[dict_index] = c
        dict_index += 1



def alphabet_position(letter):
#Determine the position for and return the key for each alphabetic letter.
#Returns the character if not alphabetic
    create_lower('abcdefghijklmnopqrstuvwxyz')
    create_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letter = str(letter)
    if letter.islower() == True:
        for key, value in lower_case_dict.items():
            if value == letter:
                return key
    elif letter.isupper() == True:
        for key, value in upper_case_dict.items():
            if value == letter:
                return key
    else:
        return letter

def rotate_character(char, rot):
#Rotates the character by the given rotation amount for alphabetic character.  
#Returns the character given if not alphabetic
    current_key = alphabet_position(char)
    if char.islower() == True:   #Test to check if letter is lowercase to maintain case in encryption
        try:
            return lower_case_dict[current_key + rot]
        except KeyError:      #if rotation moves outside of the dictionary subtract 26 to get to correct position
            current_key -= 26
            return lower_case_dict[current_key + rot]
    elif char.isupper() == True:    #Test to check if letter is uppercase to maintain case in encryption
        try:
            return upper_case_dict[current_key + rot]
        except KeyError:        #if rotation moves outside of the dictionary subtract 26 to get to correct position
            current_key -=26
            return upper_case_dict[current_key + rot]
    else:
        return char

def main():
    create_lower('abcdefghijklmnopqrstuvwxyz')
    create_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

if __name__ == '__main__':
    main()