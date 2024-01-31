import random
import print_hangman_picture

mistake_counter_dict = {
    0: print_hangman_picture.print_hangman_picture_0,
    1: print_hangman_picture.print_hangman_picture_1,
    2: print_hangman_picture.print_hangman_picture_2,
    3: print_hangman_picture.print_hangman_picture_3,
    4: print_hangman_picture.print_hangman_picture_4,
    5: print_hangman_picture.print_hangman_picture_5,
    6: print_hangman_picture.print_hangman_picture_6,
}

vocabulary = []
with open('vocabulary.txt', encoding='UTF-8') as file:
    for word in file.readlines():
        vocabulary.append(word.strip('\n'))

choice = input('Начать новую игру введите: "start", выйти из приложения введите: "exit" :')
while choice != 'start' and choice != 'exit':
    choice = input('Начать новую игру введите: "start", выйти из приложения введите: "exit" :')
if choice == 'start':
    while choice == 'start':
        secret_word = random.choice(vocabulary)
        secret_word_hiding = len(secret_word) * "*"
        mistake_counter = 0
        print(secret_word)
        print(secret_word_hiding)

        while secret_word != secret_word_hiding and mistake_counter < 6:
            answer = input('Введите букву: ').lower()
            if answer == secret_word:
                secret_word = secret_word_hiding
                break
            elif answer in 'abcdefghijklmnopqrstuvwxyz':
                print('Вы ввели букву из английского алфавита. Введите букву из русского алфавита')
            elif answer in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == answer:
                        pos = i
                        secret_word_hiding = secret_word_hiding[:pos] + answer + secret_word_hiding[pos+1:]
                mistake_counter_dict.get(mistake_counter)(mistake_counter)
                print(f'Количество ошибок: {mistake_counter}')
                print(secret_word_hiding)
            elif answer not in secret_word:
                mistake_counter += 1
                mistake_counter_dict.get(mistake_counter)(mistake_counter)
                print(f'Количество ошибок: {mistake_counter}')
                print(secret_word_hiding)
        if secret_word == secret_word_hiding:
                print('Победа')
        if mistake_counter == 6:
                print(f'Поражение. Загаданное слово: {secret_word}')
        choice = input('Начать новую игру введите: "start", выйти из приложения введите: "exit" :')
elif choice == 'exit':
    print('Игра окончена')
