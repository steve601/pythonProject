import time
print('WELCOME TO ODHASONS SOLUTIONS  ATM SIMULATION')

print('Please insert your ATM card')
print('Please wait...\n Processing information...\n Successful!!!')
print(' ')
time.sleep(5)
print('Please create account')

username = input('Please type your username: ')
pin = int(input('Please enter your unique four digit pin: '))
print("Please don't use your Birth Year as your pin!!")
time.sleep(5)
print('Account created successfully!!!\nPlease confirm your details below;')
print(f"Username: {username}\nPIN: {pin}")

balance = 10000
attempt = 0
print(' ')
time.sleep(5)
print('Log in to continue.')
def preprocess():

    global attempt

    while (attempt < 4):

        name = input('Enter Your Username: ')
        pn = int(input('Enter your PIN: '))

        if (username == name) & (pin == pn):
            print(f"Welcome {name} !")
            print('MAIN MENU\n1.Withdrawal\n2.Deposit\n3.Inquiries')

            print('Press 1 for withdrawal\n Press 2 for deposit\n Press 3 for inquiries')
            option = int(input('Please select an option; '))

            if option == 1:
                print('WITHDRAWAL')
                withdraw = int(input('How much do you wish to withdraw? '))

                if balance > withdraw:
                    print(f"Print take your cash! \n Your current balance is {balance - withdraw}")
                else:
                    print(f'Failed,you have insufficient funds, your current balance is {balance}.Thank you')
            elif option == 2:
                print('DEPOSIT')
                depo = int(input('Enter amount you want to deposit; '))

                print(f"Successful! \nYour current balance is {balance + depo}")
            elif option == 3:
                print('INQUIRIES')
                print(f"Your current balance is {balance}")

            else:
                print('Invalid option')
            return True

        else:
            print('Invalid credentials, please try again ')
            attempt += 1
            print(f"You have {4 - int(attempt)} attempts left!!")

    print('Maximum attempts reached.\n Contact the owner.\n You have been logged out!')
    return False

preprocess()

print('THANK YOU!!!')




