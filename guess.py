import random

randomNo= random.randint(1,100)
print('Guess The Number')
num=-1
guesses = 0

while(num != randomNo):
    guesses +=1
    num =int(input('Enter Number:'))
    if(num > randomNo ):
        print('Enter lower Number')
        
    else:
        print('Enter higher number:')
        

print(f'The number matches the number is {num} and guesses is {guesses}')  

