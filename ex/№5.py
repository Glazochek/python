def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    import random

    while n != 0:
        joke = [nouns[random.randint(0, len(nouns)-1)], adverbs[random.randint(0, len(adverbs)-1)], adjectives[random.randint(0, len(adjectives)-1)]]
        n -= 1
        print(*joke)

get_jokes(32)

