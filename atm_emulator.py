#!/usr/bin/python3
import os
import string
import getpass
import time

#create list of users, their PINs and bank statements
#here - version of 5 users list, but ATMs connects with database and then
#users are autorizied

users = ['krzysiek', 'denis', 'tomek', 'peter', 'lukas']
pin_code = ['1111', '2222', '3333', '4444', '5555']
amount = [500, 1000, 1500, 2000, 2500]
count = 0
inner_counter = 0

#check if user exists
while True:
        user = input('\nENTER USER NAME: ')
        user = user.lower()
        if user in users:
            if user == users[0]:
                n = 0
            elif user == users[1]:
                n = 1
            elif user == users[2]:
                n = 2
            elif user == users[3]:
                n = 3
            else:
                n = 4
            break
        else:
            #wrong username, 5 attemps counting
            print('-----------------------')
        print('WRONG USERNAME')
        print('-----------------------')

#check users pins - 3 attempts
while count < 3:
    print('--------------------')
    pin = str(getpass.getpass('ENTER YOUR PIN: '))
    print('--------------------')
    if pin.isdigit():
        if user == 'krzysiek':
            if pin == pin_code[0]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'denis':
            if pin == pin_code[1]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'tomek':
            if pin == pin_code[2]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'peter':
            if pin == pin_code[3]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'lukas':
            if pin == pin_code[4]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

    else:
        print('----------------------')
        print('PIN CODE HAS 4 DIGITS')
        print('----------------------')
        count = count + 1

#while user has 3 false attempts
while count == 3:
        print('----------------------')
        print('YOUR CARD IS LOCKED')
        print('3 FALSE ATTEMPTS')
        print('----------------------')
        exit()

print('-------------------')
print('WELCOME TO YOUR ACCOUNT ', str.capitalize(users[n]))
print('-------------------')
while True:
    print('-----------------------')
    options = input('SELECT OPTION:\nStatement-(S), Withdraw-(W) \n'
    'Cash-In-(C), Change PIN-(P) \nQuit-(Q) \n').lower()
    print('-----------------------')
    valid_options = ['s', 'w', 'c', 'p', 'q']
    options = options.lower()
    if options == 's':
       print('-------------------')
       print(str.capitalize(users[n]), ', MONEY STATUS: ', amount[n], 'EURO. ')
       print('-------------------')
    elif options == 'w':
      print('--------------------')
      print('w otions')
      print('--------------------')
    elif options == 'c':
      print('--------------------')
      print('c options')
      print('--------------------')
    elif options == 'p':
      print('--------------------')
      print('p otions')
      print('--------------------')
    elif options == 'q':
        exit()
    else:
        print('------------------')
        print('OPTIONS NOT VALID')
        print('------------------')
