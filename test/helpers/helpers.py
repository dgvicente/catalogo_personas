import random, string

def random_word(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))
