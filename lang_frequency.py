from collections import Counter
import sys
import re


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as file:
            file_data = file.read()
        return file_data
    except FileNotFoundError:
        return None


def get_most_frequent_words(raw_text, words_count=10):
    words_pattern = re.compile(r'[^\W_+]+')
    separated_words = re.findall(words_pattern, raw_text)
    return Counter(list(word for word in separated_words)).most_common(words_count)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = load_data(sys.argv[1])
        if text is not None:
            common_words = get_most_frequent_words(text)
            for common_word, count in common_words:
                print('Слово "{}" в тексте встречается {} раз{}'.format(common_word, count, 'а' if count % 2 == 0 else ''))
        else:
            print('Файл не найден')
    else:
        print('Укажите имя файла: python lang_frequency.py <filename>')
