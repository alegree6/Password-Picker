import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'naranjo', 'amarillo', 'verde', 'azul', 'purple', 'fluffy', 'blanco', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'medved']

print('Welcome to Password Picker!')

while True: 
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + str(number) + special_char

        print('Your new password is: %s' % password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
            break
