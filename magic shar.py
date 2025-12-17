from random import *
answers_ru = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
answers_eng = ["Absolutely", "I think so", "It's not clear yet, try again", "Don't even think about it",
"It's a foregone conclusion", "Most likely", "Ask later", "My answer is no",
"No doubt", "Good prospects", "Better not to tell", "According to my data - no",
"You can be sure of it", "Yes", "Concentrate and ask again", "Highly doubtful"]
while True:
    zapusk = input('+ or(или) - : ')
    if zapusk == '+':
        language = input('eng(англ) or рус(ru): ').lower()
        if language == 'ru' or language == 'рус':
            print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
            name = input('Как тебя зовут? ')
            print(f'Привет {name}!')
            while True:
                vopros = input('Задай вопрос, я дам тебе на него ответ ')
                a1 = input('Нажмите плюс для получения ответа! ')
                if a1 == '+':
                    print(choice(answers_ru))
                    print('---------------------------------')
                    a2 = input('Хотите ли еще задать вопрос?(нажмите для выхода клавишу - или остальное для повтора)')
                    if a2 == '-':
                        print('Возвращайся, если возникнут вопросы!')
                        break
                    else:
                        print('Продрожаем!')
                else:
                    print('Повтори и нажми +') 
        elif language == 'eng' or language == 'англ':
            print('Hello World, I am a magic ball and I know the answer to any question you may have.')
            name = input('What is your name? ')
            print(f'Hello {name}!')
            while True:
                vopros = input('Ask a question, I will give you an answer. ')
                a1 = input('Click plus to get the answer! ')
                if a1 == '+':
                    print(choice(answers_eng))
                    print('---------------------------------')
                    a2 = input('Would you like to ask another question? (Press the - key to exit, or the rest key to repeat)')
                    if a2 == '-':
                        print('Come back if you have any questions!')
                        break
                    else:
                        print('We are shivering!')
                else:
                    print('Repeat and press +')
        else:
            print('Повтори/repeat')
    elif zapusk == '-':
        print('Goodbye/пока!')
        break
    else:
        print('Повтори/repeat')