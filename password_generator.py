# Docs on generating both hard and easy passwor for your website or app
# first import your random module and then create a random letters, numbers and symbols 
#use for loop , shuffle(), int(), append(), range(), f-strings and string join()

import random



LETTERS  =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',   'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

NUMBERS  =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

SYMBOLS  =  ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '+', '=', '-']




print("--------------------------------------------------------------\n\n")

print("HERE YOUR CAN GENERATE A STRONGE EASY_PASSWORD FOR YOUR SITE\n")

print("--------------------------------------------------------------\n\n")

LETER  =  int(input("How many letter would you like for your password? \n:"))
NUM   =  int(input("How many numbers would you like for your password? \n:"))
SYM  =  int(input("How many symbols would you like for your password? \n:"))



EASY_PASSWORD =""

for letter in range(1, LETER + 1 ):
    EASY_PASSWORD +=  random.choice(LETTERS)

for number in  range(1, NUM + 1):
    EASY_PASSWORD  +=  random.choice(NUMBERS)

for symbol in  range(1, SYM + 1 ):
    EASY_PASSWORD  +=  random.choice(SYMBOLS)
print("\n--------------------------------------------------------------\n")

print(F"Your password is : {EASY_PASSWORD}")

print("\n\n--------------------------------------------------------------\n\n")


#Docs on generating hard level password with python 

print("--------------------------------------------------------------\n\n")# this is my line breaker 

print("HERE YOUR CAN GENERATE A STRONGE HARD_PASSWORD FOR YOUR SITE\n")

print("--------------------------------------------------------------\n\n")

HARD_PASSWORD = []

for letter in range(1, LETER + 1 ):
    HARD_PASSWORD +=  random.choice(LETTERS)# with list you can do hard_password.append(random.choice(LETTERS)) but i choose to do it my way

for number in  range(1, NUM + 1):
    HARD_PASSWORD  +=  random.choice(NUMBERS)

for symbol in  range(1, SYM + 1 ):
    HARD_PASSWORD  +=  random.choice(SYMBOLS)

random.shuffle(HARD_PASSWORD)
PASSWORD  = "".join(HARD_PASSWORD)# you can also make use of for loop, like 

                                  #passwor = ""

                                  # for l in hard_password:
                                  #    password  += l
                                  # then print your password 


print("\n--------------------------------------------------------------\n")

print(F"Your password is : {PASSWORD}")

print("\n\n--------------------------------------------------------------\n\n")
