# --------------------------------------------------------------------- #
###-- Random Password Generator --###
###-- Take several inputs regarding desired password and generate random string
###--
###-- Python learning 2021
###-- Dallyn Wynnychuk
# --------------------------------------------------------------------- #
import random
import pyperclip

# initializations
numbers = ['0','1','2','3','4','5','6','7','8','9']
lowers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
specials = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=',';',':','<','>',',','.','?']

passLenMin = 8
passLenMax = 64

# desired password characteristics
passAccept = 1
while (passAccept):
    lenPass = input('\n\nHow many characters would you like your password to be? \n')
    lenPass = int(lenPass)

    # check to make sure password length is appropriate
    passLimits = [passLenMin,passLenMax]
    if (lenPass >= passLimits[0]) & (lenPass <= passLimits[1]):
        passAccept = 0
    else:
        print('ERROR: Password length is not acceptable. Length must be between 8-64 characters\n')

addSpecialStr = input('Would you like to add special characters? (yes/no)\n').upper()
addNumbersStr = input('Would you like to add numbers? (yes/no)\n').upper()
addUppersStr = input('Would you like to use upper case in addition to lower case? (yes/no)\n').upper()


# check to determine what characters are desired
if ('Y' in addSpecialStr):
    addSpecial = 1
else:
    addSpecial = 0

if ('Y' in addNumbersStr):
    addNumbers = 1
else:
    addNumbers = 0

if ('Y' in addUppersStr):
    addUppers = 1
else:
    addUppers = 0

# add all characters allowed in password
availableChars = lowers

if (addSpecial == 1):
    availableChars = availableChars + specials

if (addNumbers == 1):
    availableChars = availableChars + numbers

if (addUppers == 1):
    availableChars = availableChars + uppers

# determine password characters
passwordChars = [''] * lenPass

for i in range(lenPass):
    passwordChars[i] = random.choice(availableChars)

# join all password characters and print
password = ''.join(passwordChars)
print('\nYour randomized password is:',password,'and it is copied to your clipboard.\n')

# copy password to clipboard 
pyperclip.copy(password)
