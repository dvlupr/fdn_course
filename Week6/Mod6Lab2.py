# open and read file
def fn_readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines


def fn_createwordlist(lines):
    word_list = []
    for line in lines:
        word_list.extend(line.strip().split(" "))
        return word_list


def fn_wordlisttodict(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    max_word = max(word_count, key=word_count.get)

    print("The word that occurs most is '{}' with count {}".format(
        max_word, word_count[max_word]))

    min_word_count = min(word_count.values())
    min_words = []
    for word, cnt in word_count.items():
        if cnt == min_word_count:
            min_words.append(word)

    print("The lowest word_count is {} and there are {}" +
          " words in the book with that word_count".format(
              min_word_count, len(min_words)))


if __name__ == __main__':

word_set = set(word_list)
print("There are {} words in the book and {} of them are unique".format(
    len(word_list), len(word_set)))
