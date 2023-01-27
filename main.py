import os
from models import Contact
from otherFunctions import getSortOrder, getFilteredList

# program start
while True:
    # taking path from user
    path = input('File path : ')

    # getting file path
    if not os.path.exists(path):
        # if path is invalid
        print('File not found or not exist! Please check the path.')
        continue
    
    # getting filter arguments
    ascOrDesc, criteria = getSortOrder()
   

    # reading contacts lines from file
    with open(path, 'r') as f:
        contactsLines = f.readlines()
    
   
    # removing \n from lines
    contactsLines = [el.replace('\n', '') for el in contactsLines]

    # removing blank lines
    contactsLines = [el for el in contactsLines if el != '']


    # creating objects from file`s lines
    contacts = [Contact(line, text) for (text, line) in enumerate(contactsLines, start=1)]
    
    # filtering objects list
    contacts = getFilteredList(contacts, ascOrDesc, criteria)
    
    # printing file structure
    print('\nFile structure:')
    for (line, el) in enumerate(contacts, start=1):
        print(f"{line})" + contactsLines[el.line - 1])



    # printing founded validations
    print('\nValidations:')
    for (line, el) in enumerate(contacts, start=1):
        if el.error:
            print(f'line {line}: {el.error}')


    # program end
    break
