import random, os

if not os.path.exists('generated'):
    os.mkdir('generated')

for i in [10, 100, 1000, 10000, 100000]:
    with open(f'generated/generated{i}.txt', 'w') as o:
        o.write(' '.join('x' * random.randrange(1, 20) for _ in range(i)))
