import random
import datetime
class Storedinfo:
    phone_no = "08172993589"
    balance = 5000000
    first_n = "Daniel"
    last_n = 'joel'
    acct_no = '2136666174'
    dob = '2002/06/11'
    pin = '1478'
    gender = 'Male'
    debit_card_pan = '678502'



class Data:
    balance = 0.0
    first_n = None
    last_n = None
    acct_no = None
    dob = None
    pin = 0
    debit_card = '123456'
    phone_no = 0

    @classmethod
    def user_info(cls):
        cls.first_n = input('Enter firstname:\n').capitalize()
        cls.last_n = input('Enter lastname:\n').capitalize()
        cls.gender = input('Define your Gender:\n'
                           '1. Male\n'
                           '2. Female\n')
        if cls.gender == '1':
            cls.gender == 'Male'
        elif cls.gender == '2':
            cls.gender == 'Female'
        else:
            print('Invalid input')
            Data.user_info()
        cls.dob = input("Enter Date of Birth' 'DD/MM/YYYY':\n")
        try:
            date = datetime.datetime.strptime(cls.dob,"%d/%m/%Y")
        except:
            print('Incorrect date!')
            Data.user_info()
        cls.pin = input('Enter 4 digit Pin:\n')
        if cls.pin.isdigit() and len(cls.pin) == 4:
            cls.acct_no = str(random.randrange(1000000000, 10000000000))
            print(f'Dear {cls.first_n} {cls.last_n} Your Acct Number is: {cls.acct_no}\n ')
        else:
            print('Invalid: Enter A Four Digit Pin')
            Data.user_info()
