print('DZ14')

inputtedNumber = int(input('Enter your number pls: '))

while True:
    tempNumber = 1
    if inputtedNumber <= 9:
        print(inputtedNumber)
        break

    for number in str(inputtedNumber):
        tempNumber *= int(number)
    inputtedNumber = tempNumber

print('Thank you for using')

################################################

while inputtedNumber > 10:
    tempNumber = 1
    for number in str(inputtedNumber):
        tempNumber *= int(number)
    inputtedNumber = tempNumber
else:
    print(inputtedNumber)

print('Thank you for using')
