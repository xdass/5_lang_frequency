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
    separated_words = re.findall(r'[^\W_+]+', raw_text)
    return Counter(separated_words).most_common(words_count)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = load_data(sys.argv[1])
        if text:
            common_words = get_most_frequent_words(text)
            for common_word, count in common_words:
                print('Слово - "{common_word}" встречается {count} раз'.format(
                    common_word=common_word,
                    count=count)
                )
        else:
            print('Файл не найден')
    else:
        print('Укажите имя файла: python lang_frequency.py <filename>')
