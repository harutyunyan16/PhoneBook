'''
    models.py contains all the model
    from the project PhoneBook

    models `

    Contact`
        name - contact first name (only characters)
        surnamename - contact last name (only characters)
        phone - contact phone number (length must be 9)
'''

# imports 
from validators import separatorValidate
from otherFunctions import getContact

# main Contact class
class Contact:
    def __init__(self, contactStr, line):
        # line - separator left part
        info = ''
        # self.line - index in file
        self.line = line
        # self.phoneNumber - separator right left
        self.phoneNumber = ''
        # self.error - founded validation problem
        self.error = ''

        # seperator validation
        sepIsValid = separatorValidate(contactStr)
        if sepIsValid:
            info, self.phoneNumber = contactStr.split(sepIsValid[1])
        else:
            self.phoneNumber = getContact(contactStr)
            info = contactStr[:len(contactStr) - len(self.phoneNumber) - 3]
            self.error += 'the separator should be `:` or `-`'

        # configure info and removoving SPACEs from info
        self.phoneNumber = self.phoneNumber.replace(' ', '')

        # phone number validation
        if len(self.phoneNumber) != 9:
            if self.error == '':
                self.error += 'phone number should be 9 digits.'
            else:
                self.error += ', phone number should be 9 digits.'

        # setting contact name and surname
        self.name , self.surname = info.split(' ')[:2]


    def __str__(self):
        return f'{self.name} {self.surname}'