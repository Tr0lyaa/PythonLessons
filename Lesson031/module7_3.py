class WordsFinder:

    def __init__(self, *file_name):
        self.file_names = []
        for name in file_name:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            alpha_line = ''
            with open(name, 'r', encoding='utf-8') as file:
                for line in file:
                    for i in range(len(line)):
                        if line[i] not in [',', '.', '=', '!', '?', ';', ':', '-'] \
                                or (line[i-1].isalpha() and line[i+1].isalpha() and line[i] == '-'):
                            alpha_line += line[i].lower()

                all_words.update({name: alpha_line.split()})

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        find_word = {}
        for name, words in all_words.items():
            if words.count(word.lower()) > 0:
                find_word.update({name: words.index(word.lower())+1})
            else:
                find_word.update({name: 'Такого слова нет'})

        return find_word

    def count(self, word):
        all_words = self.get_all_words()
        count_word = {}
        for name, words in all_words.items():
            count_word.update({name: words.count(word.lower())})

        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'), end='\n\n')

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
