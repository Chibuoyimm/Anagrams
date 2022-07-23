from .models import Dictionary


def words(word):
    word = word.upper()
    word = [letter for letter in word]
    word_list = []
    len_list = []
    string = []

    for x in Dictionary.objects.all():
        string.append(x.word)

    letter_and_scores = dict()
    k = 0
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    scores = '133214241851311311114484'

    for letter in alphabets.upper():
        if letter == 'Q' or letter == 'Z':
            letter_and_scores[letter] = 10
        else:
            letter_and_scores[letter] = int(scores[k])
            k += 1

    def score(worrd):
        summ = len(worrd) * 1000
        summ += sum([letter_and_scores[x] for x in worrd])
        return summ

    for stuff in string:
        if '\n' in stuff:
            stuff = stuff.replace('\n', '')
        check = 0
        for letter in stuff:
            if stuff.count(letter) > word.count(letter):
                check = 1
                break

        if check == 0:
            if stuff not in word_list:

                # if len(stuff) == 7:
                word_list.append(stuff)
    word_list.sort(key=score, reverse=True)

    return word_list
    # for x in word_list:
    #     print(x)