import cipher
import utils

koek = '''7 1 13 21 4 2 18 25 6 19 1 3 5 7 9 23 2 4 6 8 24 26 11 12 23 7 8 9 17 10 4 5 6 18 11 11 12 13 10 9 14 13 12 11 10 1 22 19 7 8 4 10 26 21 12 11 6 13 14 6 4 24 5 25 6
9 1 11 19 6 20 10 5 1 25 4 18 19 10 5 2 4 16 24 8 18 9 18 18 9 20 15 10 5 1 1 5 10 20 10 25 10 5 5 20 26 18 10 2 26 9 3 18 12 26 26 25 13 12 24 13 12 11 14 13 11 10 9 19 8
2 3 4 14 5 26 25 24 23 1 17 16 7 6 15 5 9 18 10 25 3 23 24 9 10 7 8 18 16 11 8 6 4 16 2 12 24 9 18 6 21 22 1 2 21 1 5 15 9 19 7 2 11 17 11 12 13 20 10 7 21 11 9 7 5'''

'''
test = 'BAABBBBBBBBABBBABBAAABBBABBABBBBBABBAAABABBBABBBBABBABBBBBBBABABBABBABABABBABBBAABABBBAABABBBBBABBBABBBBAABBBABBABBBAAAABBABBABBBABBBABBBAAABBABB'
print(test)
print(cipher.bacon_decrypt(test, version=2, swapAB=True))
test = 'maitre corbeau sur un arbre perche'
print(cipher.bacon_encrypt(test, version=2, swapAB=False))
'''

def to_odd_even(text):
    koek_odd_even = []
    for l in koek.splitlines():
        koek_odd_even.append(' '.join(['A' if int(c)%2 == 0 else 'B' for c in l.split()]))
    return '\n'.join(koek_odd_even)


koek_odd_even = []
for l in koek.splitlines():
    koek_odd_even.append(['A' if int(c)%2 == 0 else 'B' for c in l.split()])
print(koek_odd_even)

koek_prime = []
for l in koek.splitlines():
    koek_prime.append(['B' if utils.isprime(int(c)) else 'A' for c in l.split()])

print('Converted to odd/even')
for koek_msg in [koek_odd_even, koek_prime]:

    print('Reading from left to right, horizontally, top to bottom')

    print(''.join(koek_msg))

    msg = ''.join([''.join(l) for l in koek_msg])
    print(msg)
    print('version1, noswap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=False)))
    print('version1,   swap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=True)))
    print('version2, noswap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=False)))
    print('version2,   swap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=True)))

    print('Reading from right to left, horizontally, top to bottom')
    msg = ''.join([''.join(l[::-1]) for l in koek_msg])
    print(msg)
    print('version1, noswap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=False)))
    print('version1,   swap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=True)))
    print('version2, noswap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=False)))
    print('version2,   swap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=True)))

    print('Reading from top to bottom, vertically, right to left')
    msg = []
    for x in range(len(koek_msg[0]) - 1, -1, -1):
        for y in range(len(koek_msg)):
            msg.append(koek_msg[y][x])
    msg = ''.join(msg)
    print(msg)
    print('version1, noswap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=False)))
    print('version1,   swap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=True)))
    print('version2, noswap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=False)))
    print('version2,   swap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=True)))

    print('Reading from bottom to top, vertically, right to left')
    msg = []
    for x in range(len(koek_msg[0]) - 1, -1, -1):
        for y in range(len(koek_msg)-1, -1, -1):
            msg.append(koek_msg[y][x])
    msg = ''.join(msg)
    print(msg)
    print('version1, noswap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=False)))
    print('version1,   swap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=True)))
    print('version2, noswap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=False)))
    print('version2,   swap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=True)))

    print('Reading from top to bottom, vertically, left to right')
    msg = []
    for x in range(len(koek_msg[0])):
        for y in range(len(koek_msg)):
            msg.append(koek_msg[y][x])
    msg = ''.join(msg)
    print(msg)
    print('version1, noswap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=False)))
    print('version1,   swap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=True)))
    print('version2, noswap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=False)))
    print('version2,   swap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=True)))

    print('Reading from bottom to top, vertically, left to right')
    msg = []
    for x in range(len(koek_msg[0])):
        for y in range(len(koek_msg)-1, -1, -1):
            msg.append(koek_msg[y][x])
    msg = ''.join(msg)
    print(msg)
    print('version1, noswap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=False)))
    print('version1,   swap: {}'.format(cipher.bacon_decrypt(msg, version=1, swapAB=True)))
    print('version2, noswap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=False)))
    print('version2,   swap: {}'.format(cipher.bacon_decrypt(msg, version=2, swapAB=True)))