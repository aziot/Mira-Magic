import random

suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1]
deck = 4 * suit

def walk(deck, start):
    """returns final position for deck from start position"""
    pos = start
    while pos + deck[pos] < len(deck):
        pos += deck[pos]
    return pos

def couples(deck):
    """return True if two random starts in 0:4 of a shuffled deck couple"""
    random.shuffle(deck)
    starts = random.sample(range(5), 2)
    end1 = walk(deck, starts[0])
    end2 = walk(deck, starts[1])
    return end1 == end2

N = 10**6
successes = 0
for _ in range(N):
    successes += couples(deck)

rate = successes / N    
var = rate * (1 - rate) * N
sd = var**0.5
se = sd / N
conf_lb = rate - 1.96 * se
conf_ub = rate + 1.96 * se

print(f'Based on {N} simulations:')
print(f'  probability of coupling: {rate:5.3f}')
print(f'  se: {se:7.5f}')
print(f'  95% confidence interval = ({conf_lb:6.4f}, {conf_ub:6.4f})')
