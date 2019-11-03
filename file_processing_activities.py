
import os

loopcheck = ""
while True:
    print('Welcome to file_processing_activities')
    basedir = input('Please chose a directory to store your file in: ')

    while not (os.path.isdir(basedir)):
        check = input("This directory does not exist. Would you like to create it (respond 'y' or 'yes' yes, 'n' or 'no' for no)? ").lower()
        if check == 'y' or check == 'yes:':
            os.mkdir(basedir)
        elif check == 'n' or check == 'no':
            loopcheck = 'n'
            break
        else:
            print('Could not understand that, please try again.')
            continue
    if loopcheck == 'n':
        continue

    file = input('Please input a file name: ')
    file_name = f'{file}.txt'
    if not basedir[-1] == "\\":
        basedir = basedir + '\\'
    complete_path = basedir + file_name
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone_number = input("What is your phone number? ")
    line = f'{name},{address},{phone_number}'
    with open(complete_path, 'a') as fileHandle:
        fileHandle.write(line + "\n")
    print('Your file has been made, here are the contents of the file to date:')
    with open(complete_path, 'r') as readHandle:
        for line in readHandle:
            print(line.strip())
    while True:
        check2 = input("Do you want to make another file (respond 'y' or 'yes' yes, 'n' or 'no' to exit)? ").lower()
        if check2 == 'y' or check2 == 'yes:':
            break
        elif check2 == 'n' or check2 == 'no':
            exit()
        else:
            print('Could not understand that, please try again.')
            continue
