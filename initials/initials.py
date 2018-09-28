#Tells the user the initials for the given name
#Created by Dustin Peterson for the Launchcode LC101 Initials assignment

def get_initials(fullname):
    #Given a persons name returns their initials in uppercase letters
    sub_names = list()
    initials = ''
    sub_names = fullname.split(' ')
    for name in sub_names:
        initials += name[0]
    return initials.upper()

def main():
    name = input("What is your name? ")
    print(get_initials(name))

if __name__ == '__main__':
    main()