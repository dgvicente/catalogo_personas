import random, string

def random_word(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

def random_number(max = 100):
    return random.randrange(0, max)

def random_email():
    return "%s@%s.com" % (random_word(8), random_word(10))
