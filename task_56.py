def most_common_word(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = {}

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

            most_common_word = max(word_count, key=word_count.get)
            return most_common_word
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден.")


# Пример использования программы
try:
    file_name = input("Введите имя файла: ")
    most_common_word = most_common_word(file_name)
    print("Самое часто встречающееся слово:", most_common_word)
except FileNotFoundError as e:
    print(e)