from random import *
d = 0
while True:
    b = input('запустить программу?/run the program?( + or/или - ): ')
    if b == '+':
        print('ru(ру) or(или) eng(англ)')
        language = input()
        if language == 'ru' or language == 'ру':
            print('Добро пожаловать в числовую угадайку')
            c = int(input('задайте промежуток от одного до вашего числа: '))
            def is_valid(a):
                if a.isdigit() != True:
                    return False
                else: 
                    a = float(a)
                    return 1 <= a <= c
            win_num = randint(1, c)
            print(f'Как прочитаете напишите целое число от 1 до {c} для запуска')
            print(f'Просим вас угадать целые числа от 1 до {c} включительно')
            print('В случае если вы напишите не те символы - выйдет Falsе')
            print(f'числа меньше одного, больше {c} и все остальные символы запрещены')
            print('также идет подсчет попыток')
            a = input()
            if is_valid(a) == True:
                while True:
                    print('Игра началась, в случае не того символа игра не завершится')
                    print('в случае если число с плавающей точкой - мы округлим в меньшую сторону')
                    num = input('Введите число: ')
                    if is_valid(num) == False:
                        print(f'А может быть все-таки введем целое число от 1 до {c}?')
                    else:
                        num = int(num)
                        if num < win_num:
                            print('----------------------------------------------------')
                            print('Ваше число меньше загаданного, попробуйте еще разок')
                            print('----------------------------------------------------')
                            d += 1
                            print(f'Попытки: {d}')
                            print('----------------------------------------------------')
                        elif num > win_num:
                            print('----------------------------------------------------')
                            print('Ваше число больше загаданного, попробуйте еще разок')
                            print('----------------------------------------------------')
                            d += 1
                            print(f'Попытки: {d}')
                            print('----------------------------------------------------')
                        else:
                            print('Вы угадали, поздравляем!')
                            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                            d += 1
                            if d == 1:
                                print('Йоу чувак с первого раза, ты молодчина:)')
                            else:
                                print(f'Попытки: {d}')
                            break
            else:
                print('False')
                print('Начните заново программу')
        elif language == 'eng' or language == 'aнгл':
            print('Welcome to the numerical guessing game')
            c = int(input('set the interval from one to your number: '))
            def is_valid(a):
                if a.isdigit() != True:
                    return False
                else: 
                    a = float(a)
                    return 1 <= a <= c
            win_num = randint(1, c)
            print(f'As you read it, write an integer from 1 to {c} to run')
            print(f'Please guess the integers from 1 to {c} inclusive')
            print('If you write the wrong characters, it will be False.')
            print(f'numbers less than one, greater than {c} and all other characters are prohibited')
            print('Attempts are also being counted.')
            a = input()
            if is_valid(a) == True:
                while True:
                    print('The game has started, in case of the wrong symbol, the game will not end.')
                    print('if the number is floating-point, we will round it down.')
                    num = input('Enter a number: ')
                    if is_valid(num) == False:
                        print(f'Or maybe we can still enter an integer from 1 to {c}?')
                    else:
                        num = int(num)
                        if num < win_num:
                            print('----------------------------------------------------')
                            print('Your number is less than expected, try again.')
                            print('----------------------------------------------------')
                            d += 1
                            print(f'Attempts: {d}')
                            print('----------------------------------------------------')
                        elif num > win_num:
                            print('----------------------------------------------------')
                            print('Your number is higher than expected, try again.')
                            print('----------------------------------------------------')
                            d += 1
                            print(f'Attempts: {d}')
                            print('----------------------------------------------------')
                        else:
                            print('You guessed it, congratulations!')
                            print('Thanks for playing the numerical guessing game. I ll see you later...')
                            d += 1
                            if d == 1:
                                print('Yo, dude, you did great the first time :)')
                            else:
                                print(f'Attempts: {d}')
                            break  
        else:
            print('Повтори/repeat')                
    elif b == '-':
        print('Пока/Goodbye!')
        break
    else:
        print('Повтори/repeat')
        
