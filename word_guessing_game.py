sec_word = input('enter random word: ')
sec_word_list = []

guess_word = []
differ = []

max_guesses = 15
num_of_guesses = 0

letter = ''
space = 11
i = 0

while i <= space:
    print(' ')
    i += 1

def create_lists(sec_word, sec_word_list, guess_word, differ):
    for i in sec_word:
        sec_word_list.append(i)

    for i in sec_word:
        guess_word.append('_')
        differ.append('_')

create_lists(sec_word, sec_word_list, guess_word, differ)

def difference():
    differ.clear()
    for i in guess_word:
        differ.append(i)
    return differ

while num_of_guesses <= max_guesses:
    letter = input('letter: ')
    len_of_let = len(letter)
    lifes = max_guesses - num_of_guesses
    differ = difference()
    a = 0

    while len_of_let < 1 or len_of_let > 1:
        print('you can enter exactly one letter not less not more')
        letter = input('letter: ')
        len_of_let = len(letter)

    for i in sec_word_list:
        if letter == i:
            Index = a
            guess_word[Index] = i
        a += 1

    print(guess_word)

    if guess_word == sec_word_list:
        num_of_guesses = max_guesses + 1
        print('you won')
    elif guess_word != differ:
        print('you got that')
    else:
        num_of_guesses += 1
        print('you have only ' + str(lifes) + ' lifes left')
