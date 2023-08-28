import  project_one.banking as run
import project_one.info as info
ussd = input('Dail *889#:')
def work():
    if ussd == '*889#':
        user_input = input('Welcome to ussd banking please note N6.98\n'
                       'network charge will be applied to your account\n'
                       'or banking services on this channel\n'
                       '1.Accept\n'
                       '2.Cancel\n').lower()
        if user_input == "1":
            number = (input("Enter Your Phone Number:"))
            if number.isdigit() and len(number) == 11 :
                if number == info.Storedinfo.phone_no:
                    info.Data.pin = info.Storedinfo.pin
                    info.Data.balance = info.Storedinfo.balance
                    info.Data.acct_no = info.Storedinfo.acct_no
                    info.Data.debit_card = info.Storedinfo.debit_card_pan
                    info.Data.dob = info.Storedinfo.dob
                    info.Data.last_n = info.Storedinfo.last_n
                    info.Data.first_n = info.Storedinfo.first_n
                    run.action()
                else:
                    acc = input('Open Xpress Account\n'
                      '1.Accept\n'
                      '2.Cancel\n')
                    if acc == '1':
                        info.Data.user_info()
                    else:
                        print('Invalid')
                        work()
                    continue_p = input('Would you like to make a transcation?\n'
                                       '1. Yes\n'
                                       '2. No\n')
                    if continue_p == '1':
                        run.action()
            else:
                print('Invalid input!! Enter a valid phone number.')
                work()
        elif user_input == '2':
            print('Thank You!!')
            exit()
        else:
            print("Invalid")
            work()
    else: 
        print('Invalid Code!')


work()