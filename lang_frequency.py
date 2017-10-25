from collections import Counter
import re


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        file_data = file.read()
    return file_data


def get_most_frequent_words(text, words_count=10):
    words_pattern = re.compile(r'[^\W_+]+')
    separated_words = re.findall(words_pattern, text)
    return Counter(list(word for word in separated_words)).most_common(words_count)


if __name__ == '__main__':
    text = load_data('text.txt')
    common_words = get_most_frequent_words(text)
    for common_word, count in common_words:
        print('Слово "{}" в тексте встречается {} раз{}'.format(common_word, count, 'а' if count % 2 == 0 else ''))
