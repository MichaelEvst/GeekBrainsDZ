from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def matches(words, jokes_list):
    for word in words:
        for fun in jokes_list:
            if word == fun:
                words.remove(word)


def get_jokes(n, flag):
    for i in range(n):
        fst_random_word = choice(nouns)
        snd_random_word = choice(adverbs)
        trd_random_word = choice(adjectives)
        joke = f'{fst_random_word} {snd_random_word} {trd_random_word}'
        jokes_list = []
        print(joke)
        if flag:
            jokes_list = joke.split()
            matches(nouns, jokes_list)
            matches(adverbs, jokes_list)
            matches(adjectives, jokes_list)


get_jokes(n=5, flag=True)
