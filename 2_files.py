"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r') as file:
        text = file.read()
        text_length = len(text)
        print(f'Кол-во символов (с учетом пробелов и знаков препинания): {text_length}')
        
        words_amount = len(text.split())
        print(f'Кол-во слов: {words_amount}')
        
        text2 = open('referat2.txt', 'w')
        text2.write(text.replace('.', '!'))
        text2.close()


if __name__ == "__main__":
    main()
