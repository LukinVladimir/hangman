import random
import hangman_picture

vocabulary = []
with open('vocabulary.txt') as file:
    for word in file.readlines():
        vocabulary.append(word.strip('\n'))

choice = input('Начать новую игру введите: "start", выйти из приложения введите: "exit" :')
while choice == "start":
    secret_word = random.choice(vocabulary)
    secret_word_hiding = len(secret_word) * "*"
    mistake_counter = 0
    print(secret_word_hiding)

    while secret_word != secret_word_hiding and mistake_counter < 6:
        answer = input('Введите букву: ')
        if answer in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == answer:
                    pos = i
                    secret_word_hiding = secret_word_hiding[:pos] + answer + secret_word_hiding[pos+1:]
            hangman_picture.hangman_picture(mistake_counter)
            print(f'Количество ошибок: {mistake_counter}')
            print(secret_word_hiding)
        elif answer not in secret_word:
            mistake_counter += 1
            hangman_picture.hangman_picture(mistake_counter)
            print(f'Количество ошибок: {mistake_counter}')
            print(secret_word_hiding)
    if secret_word == secret_word_hiding:
            print('Победа')
    if mistake_counter == 6:
            print('Поражение')
    choice = input('Начать новую игру введите: "start", выйти из приложения введите: "exit" :')