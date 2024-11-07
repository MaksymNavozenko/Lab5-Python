import re

# Функція для сортування українських і англійських слів
def custom_sort(words):
    ukr_words = sorted([w for w in words if re.search(r'[А-Яа-яЇїЄєІі]', w)], key=str.casefold)
    eng_words = sorted([w for w in words if re.search(r'[A-Za-z]', w)], key=str.casefold)
    return ukr_words + eng_words

# Функція для обробки тексту з файлу
def process_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Зчитуємо перше речення
            text = file.read()
            first_sentence = re.split(r'[.!?]', text)[0]
            print("Перше речення:", first_sentence)

            # Видаляємо пунктуацію та розбиваємо на слова
            words = re.findall(r'\b\w+\b', first_sentence)
            sorted_words = custom_sort(words)

            print("Відсортовані слова:", sorted_words)
            print("Кількість слів:", len(sorted_words))

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print("Помилка при читанні файлу:", e)

# Виклик функції для обробки тексту
process_text('input.txt')
