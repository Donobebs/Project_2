import project_one.info as info
import project_one.banking as banking
import random

def inter():
    T_continue = input('Would you like to perform another transaction?\n'
                       '1. YES\n'
                       '2. NO\n')
    if T_continue == '1':
        banking.action()
    elif T_continue == '2':
        print('THANK YOU')
        exit()
    else:
        print('Invalid input!')
        inter()


def airtime():
    my_amount = input("Enter amount:\n")
    if my_amount.isnumeric():
        my_amount = int(my_amount)
        if my_amount >= 50:
            if my_amount > info.Data.balance:
                print("Insufficient funds!")
                exit()
            else:
                recharge = input(f"You will be charged N{my_amount} to recharge airtime on this line.\n"
                      f"1. Proceed\n"
                      f"2. Cancel\n")
                if recharge == "1":
                    if info.Data.balance > my_amount:
                        info.Data.balance -= my_amount
                        print(f"Transaction successful\n")
                        inter()

                    else:
                        print("Insufficient Funds")

                elif recharge == "2":
                    print("Cancelled")
                    inter()
                else:
                    print("Invalid input")
                    airtime()
        else:
            print(f'{my_amount} is below the minimum amount allowed ')
            airtime()
    else:
        print("Invalid input")
        airtime()
def airtime_others():
    recipient = input("Enter recipient's number\n")
    if recipient.isdigit() and len(recipient) == 11:
        amount_others = input("Enter amount\n")
        if amount_others.isnumeric():
            amount_others = int(amount_others)
            my_pin = input(f"Enter your 889 PIN to Top Up \n"
                           f"{recipient} on MTN with NGN {amount_others} or enter 0 \n"
                           f"to cancel.\n")
            if my_pin == '0':
                print('Thank You')
                inter()
            else:
                if my_pin == info.Data.pin :
                    if info.Data.balance >= amount_others:
                        info.Data.balance -= amount_others
                        print("Transaction successful")
                        inter()
                    else:
                        print("Insufficient Funds")
                        exit()
                elif my_pin == 0:
                    print("Cancelled")
                    inter()
                else:
                    print("Invalid pin")
                    airtime_others()
        else:
            print("Invalid input")
            airtime_others()
    else:
        print("Enter a valid phone number!")
        airtime_others()
def data():
   def action_one():
       action = input('1. 100MB - N100\n'
                      '2. 200MB - N200\n'
                      '3. 350MB - N300\n'
                      '4. 750MB - N550\n'
                      '5. 1.5GBB - N1000\n'
                      '6. 2GB - N1200\n'
                      '7. Next\n'
                      '8. Back\n')
       if action == '1':
           check_pin= (input('You are about to buy[100MB Daily Plan]\n'
                                 'Enter your 4 digits USSD pin:\n'))
           if (check_pin) == (info.Data.pin) :
               print("You have successfully purchased N100 - 100MB Daily Plan  ")
               inter()
               info.Data.balance -= 100
           else:
               print('invalid pin')
               action_one()
       elif action == '2':
           check_pin = (input('You are about to buy[200MB Daily Plan]\n'
                                 'Enter your 4 digits USSD pin:\n'))
           if check_pin == info.Data.pin:
               print("You have successfully purchased 200MB Daily Plan  ")
               inter()
               info.Data.balance = - 200

           else:
               print('invalid pin')
               action_one()
       elif action == '3':
           check_pin = (input('You are about to buy[350MB Daily Plan]\n'
                                 'Enter your 4 digits USSD pin:\n'))
           if check_pin == info.Data.pin:
               print("You have successfully purchased 350MB Daily Plan  ")
               inter()
               info.Data.balance -= 300
           else:
               print('invalid pin')
               action_one()
       elif action == '4':
           check_pin = (input('You are about to buy[750MB Monthly for 30 DAYS]\n'
                                 'Enter your 4 digits USSD pin:\n'))
           if check_pin == info.Data.pin:
               print("You have successfully purchased 750MB Monthly Plan For 30 DAYS  ")
               inter()
               info.Data.balance -= 550
           else:
               print('invalid pin')
               action_one()
       elif action == '5':
           check_pin = (input('You are about to buy[1.5GB Monthly for 30 DAYS]\n'
                                 'Enter your 4 digits USSD pin:\n'))
           if check_pin ==info.Data.pin:
               print("You have successfully purchased 1.5GB Monthly Plan for 30 DAYS ")
               inter()
               info.Data.balance -= 1000
           else:
               print('invalid pin')
               action_one()
       elif action == '6':
           check_pin = (input('You are about to buy[2GB Monthly for 30 DAYS]\n'
                                 'Enter your 4 digits USSD pin:\n'))
           if check_pin == info.Data.pin:
               print("You have successfully purchased 2GB MOnthly Plan For 30 DAYS")
               inter()
               info.Data.balance -= 1200
           else:
               print('invalid pin')
               action_one()
       elif action == '7':
           action_two =  input('1. 2GB - N1200\n'
                               '2. 4GB - N1500\n'
                               '3. 4.5GB - N2000\n'
                               '4. 10GB - N3000\n'
                               '5. 12GB - N3500\n'
                               '6. 6.5GB - N2500\n'
                               '7. Back\n')
           if action_two == '1':
               check_pin = (input('You are about to buy[2GB Monthly for 30 Days]\n'
                                             'Enter your 4 digits USSD pin:\n'))
               if check_pin == info.Data.pin:
                   print("You have successfully purchased 2GB Monthly Plan for 30 Days ")
                   inter()
                   info.Data.balance -= 1200
               else:
                   print('invalid pin')
                   action_one()
           elif action_two == '2':
               check_pin = (input('You are about to buy[4GB Monthly for 30 DAYS]\n'
                                     'Enter your 4 digits USSD pin:\n'))
               if check_pin == info.Data.pin:
                   print("You have successfully purchased 4GB Monthly Plan for 30 Days  ")
                   inter()
                   info.Data.balance -= 1500
               else:
                   print('invalid pin')
                   action_one()
           elif action_two == '3':
               check_pin = (input('You are about to buy[4.5GB Mpnthly for 30 DAYS]\n'
                                     'Enter your 4 digits USSD pin:\n'))
               if check_pin == info.Data.pin:
                   print("You have successfully purchased 4.5GB  Monthly Plan for 30 Days   ")
                   inter()
                   info.Data.balance -= 2000
               else:
                   print('invalid pin')
                   action_one()
           elif action_two == '4':
               check_pin = (input('You are about to buy[10GB Monthly for 30 DAYS]\n'
                                     'Enter your 4 digits USSD pin:\n'))
               if check_pin == info.Data.pin:
                   print("You have successfully purchased 10GB Monthly Plan For 30 DAYS  ")
                   inter()
                   info.Data.balance -= 3000
               else:
                   print('invalid pin')
                   action_one()
           elif action_two == '5':
               check_pin = (input('You are about to buy[12GB Monthly for 30 DAYS]\n'
                                     'Enter your 4 digits USSD pin:\n'))
               if check_pin == info.Data.pin:
                   print("You have successfully purchased 12GB Monthly Plan for 30 DAYS ")
                   inter()
                   info.Data.balance -= 3500
               else:
                   print('invalid pin')
                   action_one()
           elif action_two== '6':
               check_pin = (input('You are about to buy[6.5GB Monthly for 30 DAYS]\n'
                                    'Enter your 4 digits USSD pin:\n'))
               if check_pin == info.Data.pin:
                   print("You have successfully purchased 6.5GB MOnthly Plan For 30 DAYS")
                   inter()
                   info.Data.balance -= 2500
               else:
                   print('invalid pin')
                   action_one()
           elif action_two == '7':
               action_one()
           else:
               print('Invalid input ')
               action_one()
       elif action == '8':
           banking.action()
       else:
           print('Invalid!')
           action_one()
   action_one()
def trsf():
    banks_list = '1.Uba\n2.Access\n3.Zenith\n4.Unity\n5.Next'
    acc_names = ['Paul Okoye', 'Bright Unwosu', 'David Ana',"Jude ike",'Peter Obi',"Bola Tinubu"]
    print('1. GT Bank\n2. Other Banks')
    print('press # to go back to the main menu')

    trnsf = input('')
    if trnsf == '#':
        banking.action()
    elif trnsf == '1':
        account_number = str(input('Enter account number:\n'))
        if len(account_number) == 10 and account_number.isnumeric():
            amount = int(input('Enter amount: \n'))
            pin = (input('Enter pin:\n'))
            info.Data.balance -= amount
            acc_name = acc_names.pop()
            if pin == info.Data.pin:
                print(f'You have successfully transferred: {amount}\n To {acc_name}{account_number}')
                print(f'Your balance is {info.Data.balance}')
                inter()
        else:
            print('Invalid input')
            trsf()
    elif trnsf == '2':
        amount = int(input('Enter amount:\n'))
        acc_num = str(input('Enter account number:\n'))
        if len(acc_num) == 10 and acc_num.isnumeric:
            print(banks_list)
            bank = input('Select Receipients Bank\n')
            if bank.isnumeric():
                acc_name = acc_names.pop()
                pin = (input('Enter Pin:\n'))
                info.Data.balance -= amount
                if pin == info.Data.pin:
                    print(f'You have successfully transferred: {amount}\nTo {acc_name}\n{acc_num}')
                    print(f'Your balance is N{info.Data.balance}')
                    inter()
                else:
                    print('Invalid input')
                    trsf()
            else:
                print("Invalid!")
                trsf()
        else:
            print("Invalid!")
            trsf()
    else:
        print("Invalid!")
        trsf()


def cable_tv():
    sm = input('Pay Bills\n'
               'Enter Smartcard no:')
    if sm.isdigit() and len(sm) == 10:
        next = input(f"Pay Bills\n"
                     f"1.Save smartcard: {sm}\n"
                     f"2.Don't save\n")
        if next == '1':
            save = sm
        elif next == '2':
            amt = (input('Pay Bills\n'
                        'Enter Amount\n'))
            if amt.isnumeric():
                amt = int(amt)
                check_pin = input(f'You are about to pay DSTV\n'
                                  f'Number {sm}\n'
                                  f'Amount: N{amt}\n'
                                  f'Enter Pin to confirm:\n')
                if check_pin == info.Data.pin and check_pin.isdigit():
                    print(f"{info.Data.acct_no}\n"
                          f"{info.Data.first_n}{info.Data.last_n}\n"
                          f"You have successfully Recharged DSTV Number{sm}\n"
                          f"Amt:N{amt}\n")
                    inter()
                    info.Data.balance -= amt
                else:
                    print('Invalid Pin')
                    cable_tv()
            else:
                print('Invalid input!')
                cable_tv()
        else:
            print('Invalid input!')
            cable_tv()
    else:
        print('Invalid input!')
        cable_tv()
def atu():
    user_input = input('Welcome to the GTBank auto top-up service.\n'
                       'What would you like to do?\n'
                       '1.subscribe \n'
                       '2.unsubscribe\n').lower()
    if user_input == '1':
        amount = (input('Kindly input the auto top-up amount greater than N50\n'))
        if amount.isdigit():
            amount = int(amount)
            if amount > info.Data.balance:
                print("Inssuficient Funds")
                exit()
            else:
                if amount >= 50:
                    pin = input('To confirm your auto top-up when you '
                                'reach a threshold of N50 please enter your PIN.')
                    if pin == info.Data.pin:
                        print(f'you have sucessfully activated your auto top-up')
                        inter()
                    else:
                        print('PIN Invalid please try again')
                        atu()
                else:
                    print('Please enter amount greater than N50')
                    atu()
        else:
            print('Invalid input!')
            atu()
    elif user_input == '2':
        print("You've succesfuly unsubscribed from auto top-up services")
        inter()
    else:
        print('Invalid input')
        atu()
def d_w_c():
    dwc = input('1. Cash Deposit\n'
                '2. Cash withdrawal\n')
    if dwc == '1':
        amount =(input("Enter amount to be Deposited: "))
        if amount.isnumeric():
            amount = int(amount)
            info.Data.balance += amount
            print(f" Amount Deposited:{amount}\n"
                  f" Available balance:{info.Data.balance}\n")
            inter()
        else:
            print('Invalid input!')
            dwc()
    elif dwc == '2':
        amount = (input("Enter amount to be Withdrawn: "))
        if amount.isdigit():
            amount = int(amount)
            if info.Data.balance >= amount:
                info.Data.balance -= amount
                print(f"You Withdrew:{amount}\n"
                      f"Available Balance:{info.Data.balance}\n")
                inter()
            else:
                print("\n Insufficient balance  ")
                exit()
        else:
            print("Invalid input!")
            d_w_c()
    else:
        print('Invalid input!')
        d_w_c()

def gtoken():
    user_input = input('Please enter Your Pin to retrieve your token code:\n'
                       'Enter 0 to cancel\n')
    if user_input.isnumeric() and user_input != '0':
        if user_input == info.Data.pin:
            token = random.randrange(1000000,10000000)
            print(f"Token:{token}\n")
            inter()
        else:
            print('Invalid Authorization PIN.')
            gtoken()
    else:
        print('Thank you')
        inter()
def Loanbalance():
    loanPin = input('Please Enter your 737 PIN to confirm or 0 to cancel\n')
    if loanPin == info.Data.pin:
        print(f"(You don't have an outstanding loan on customer number: {info.Data.acct_no})")
        inter()
    elif loanPin == '0':
        print('Thank you')
        inter()
    else:
        print('Account details is not valid, please verify')
        Loanbalance()
def pin():
    features = input(
        '    Opt in for 889\n'
        '1.  Create/Reset PIN - Debit card\n'
        '2.  Creat PIN - No Debit Card\n'
        '3.  Change PIN - Debit Card\n'
        '4.  Chnage PIN - No Debit Card\n'
    )
    if features == '1':
        cardD = input('Enter the 6 last digits of your debit card\n')
        if cardD == info.Data.debit_card:
            newpin = input('Please enter new pin\n')
            confirm_newPin = input('Please confirm your new pin\n')
            if newpin.isdigit() and len(newpin) == 4:
                print('You have successfully created your pin\n')
                inter()
                info.Data.pin = newpin
            elif newpin.isdigit() == confirm_newPin.isdigit() == False:
                print('Please check your input, you can only enter digits')
                pin()
            else:
                print("PIN doesn't match ")
                pin()

        else:
            print('Invalid user, please verify')
            pin()

    elif features == '2':
        acct = input('Please enter your 10 digit Account number\n')
        if acct.isdigit() and len(acct) == 10 :
            acc = int(acct)
            if acct == info.Data.acct_no:
                date_of_birth = input('Please enter DOB in the following format dd/mm/yyyy\n')
                if date_of_birth == info.Data.dob:
                    userDetails = input(f'Name:{info.Data.last_n}{info.Data.first_n}\n'
                                        f'Account No:{info.Data.acct_no}\n'
                                        f'Enter 1 to proceed or 0 to exit\n')
                    if userDetails == '1':
                        newPin = input('Please enter 4 digits to creat GT bank pin\n')
                        confirm_newPin = input('Please confirm your new pin\n')
                        if newPin.isdigit() and len(newPin) == 4 and newPin == confirm_newPin:
                            print('You have successfully created your GT bank pin')
                            inter()
                        else:
                            print("Pin doesn't match")
                            pin()

                    elif userDetails == '0':
                        print('Thank you')
                        inter()
                    else:
                        print('You can only enter 1 or 0')
                        pin()

        elif acct.isdigit() != acctnum.isdigit():
            date_of_birth = input('Please enter DOB in the following format dd-mm-yyyy\n')
            if date_of_birth != dob:
                print('Account details is not valid, please verify')
                pin()
            else:
                print('Invalid user, Please verify')
                pin()
        else:
            pin()
    elif features == '3':
        existing_pin = input('Please enter existing pin\n')
        if existing_pin == info.Data.pin:
            cardD = input('Enter the last six digits of your GT bank debit card to continue\n')
            if cardD == info.Data.debit_card:
                newpin = input('Please enter your new four digit PIN\n')
                confirm_newPin = input('Please confirm your new pin\n')
                if newpin.isdigit() and confirm_newPin.isdigit() and len(newpin) == 4 :
                    print('You have sucessfully changed your PIN')
                    inter()
                elif newpin.isdigit() == confirm_newPin.isdigit() == False:
                    print('Please check your input, you can only enter digits')
                    pin()
                else:
                    print("PIN doesn't match")
                    pin()
        elif existing_pin != pin:
            cardD = input('Enter the last six digits of your GT bank debit card to continue\n')
            if cardD == info.Data.debit_card:
                print('An error occoured, please try again')
                pin()
            else:
                print('Invalid user, please verify')
                pin()
        else:
            print('Invalid user, please verify')
            pin()
    elif features == '4':
        existing_pin = input('Please enter existing pin\n')
        if existing_pin == info.Data.pin:
            acct = input('Please enter your 10 digit Account Number\n')
            if len(acct)== 10 and acct == info.Data.acct_no :
                date_of_birth = input('Please enter DOB in the following format dd/mm/yyyy\n')
                if date_of_birth == info.Data.dob:
                    userDetails = input(f'Name:{info.Data.first_n}{info.Data.last_n}\n'
                                        f'Account No:{info.Data.acct_no}\n'
                                        f'Enter 1 to proceed or 0 to exit\n')
                    if userDetails == '1':
                        newPin = input('Please enter 4 digits to create GT bank PIN\n')
                        confirm_newPin = input('Please confirm your new pin\n')
                        if len(newPin) == 4 and newPin == confirm_newPin:
                            print('You have successfully changed your PIN')
                            inter()
                        else:
                            print("PIN doesn't match")
                            pin()
                    elif userDetails == '0':
                        print('Thank you')
                        inter()
                    else:
                        pin()
                else:
                    print('An error occoured, please try again')
                    pin()

        elif existing_pin != info.Data.pin:
            acct = input('Please enter your 10 digit Account Number\n')
            if len(acct) == 10 and acct == info.Data.acct_no:
                print('Account Number is not valid, please verify')
                pin()
        else:
            pin()
    else:
        print('Please select an option from the below menu')
        pin()
def optin():

    opt = input('Enter your ussd pin to opt in\n: ')
    if opt == info.Data.pin:
        vrfy_card =input('Please enter the last six digits of \n'
                          'your debit card to continue\n: ')
        if vrfy_card == info.Data.debit_card:
            print('You have successfully activated the OPT on your account\n')
            inter()
        else:
            print('Invalid digits, try again\n')
            optin()
    else:
        print('Invalid digits, try again')
        optin()

def optout():
    opt_out = input('Enter your ussd pin to opt out\n: ')
    if opt_out == info.Data.pin:
        print('You have successfully opted out, Thank you')
        inter()
    else:
        print('Invalid pin, try again')
        optout()

def ac_balance():
    bal_check = input("Enter your 10 digit Acct Number:\n")
    if bal_check == info.Data.acct_no:
        pin_check = input('Enter 4 Digit Pin:\n')
        if pin_check == info.Data.pin:
            print(f"Available Balance:{info.Data.balance}")
            inter()
        else:
            print("Invalid")
            ac_balance()
    else:
        print('Null')
        ac_balance()
