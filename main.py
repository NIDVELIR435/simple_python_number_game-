# simple game user have to understand what number program chose
import random

# default messages
defaultMessage = 'write number which program can be'
minCountMessage = 'number should be greater then 5'
whatNumberMessage = 'What number you think was generated?'
shouldWriteIntMessage = 'I perceive only integer'

# assigns restrict  max number for game
maxNumber = input(defaultMessage)

while maxNumber.isdigit():
    maxNumber = input(defaultMessage)
print('here')

while int(maxNumber) <= 5:
    maxNumber = input(minCountMessage)

randomNumber = random.randint(1, int(maxNumber))

answer = input(whatNumberMessage)
attempt = 0
while answer != randomNumber:
    if attempt == 5:
        print('you lose')
        break

    if type(answer) != 'int':
        attempt += 1
        answer = input(shouldWriteIntMessage)

    answer = int(answer)

    if answer > randomNumber:
        attempt += 1
        answer = input('less')

    if answer < randomNumber:
        attempt += 1
        answer = input('more')
    if answer == randomNumber:
        print('You won!!')
        break;