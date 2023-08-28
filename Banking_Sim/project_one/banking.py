import project_one.sims as banking
def action():
    action = input("1. Airtime \n"
                   "2. Airtime-others\n"
                   "3. Transfer \n"
                   "4. Cable Tv\n"
                   "5. Data\n"
                   "6. Next\n"
                   "7. Exit\n")
    if action == '1':
        banking.airtime()
    elif action == '2':
        banking.airtime_others()
    elif action == '3':
        banking.trsf()
    elif action == '4':
        banking.cable_tv()
    elif action == '5':
        banking.data()
    elif action == '6':
        next()
    elif action == '7':
        print('Thank You')
        exit()
    else:
        print('Invalid input\n')
        action()
def next():
    action_ii= input("1. A/C Balance \n"
                   "2. Pin\n"
                   "3. Opt-in\n"
                   "4. Opt-out\n"
                   "5. Loan Balance\n"
                   "6. Generate Token\n"
                   "7. Back\n"
                   "8. Next\n"
                   "9. Exit\n")
    if action_ii == '1':
        banking.ac_balance()
    elif action_ii == '2':
        banking.pin()
    elif action_ii == '3':
        banking.optin()
    elif action_ii == '4':
        banking.optout()
    elif action_ii == '5':
        banking.Loanbalance()
    elif action_ii == '6':
        banking.gtoken()
    elif action_ii == '7':
        action()
    elif action_ii == '8':
        nextii()
    elif action_ii == '9':
        print('Thank you')
        exit()
    else:
        print('Invalid Input')
        nextii()


def nextii():
    action_iii = input('1. Deposit/Withdraw Cash\n'
          '2. Auto top up\n'
          '3. Back\n'
          '4. Exit\n')
    if action_iii == "1":
        banking.d_w_c()
    elif action_iii == '2':
        banking.atu()
    elif action_iii == '3':
        next()
    elif action_iii == '4':
        print('Thank You')
        exit()
    else:
        print('Invalid input')
        nextii()
