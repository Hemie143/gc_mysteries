import re
import string


def bacon2text(bacon):
    """ This function converts a string in bacon (a lot of 'a's and 'b's) to
        plain text. The plaintext is returned. If a character can't be
        translated, a space will be inserted. """

    bacondict = {}
    plaintext = ""

    bacon = bacon.lower()
    bacon = re.sub("[\W\d]", "", bacon.strip())
    for i in range(0, 26):
        tmp = bin(i)[2:].zfill(5)
        tmp = tmp.replace('0', 'a')
        tmp = tmp.replace('1', 'b')
        bacondict[tmp] = chr(65 + i)

    for i in range(0, len(bacon) // 5):
        plaintext = plaintext + bacondict.get(bacon[i * 5:i * 5 + 5], ' ')
    return plaintext


crypto = """BAABBAABBBABAAABAABA ABAAABAABA AAAAA AAAABAAAAAAAABAABBBAABBAB AAABAABAAAABBBBAABBBAABAABAAAB ABBAAAABAABAABABAABAAAAAAAABBAAABAA"""
crypto = """BAABBAABBBABAAABAABAABAAABAABAAAAAAAAAABAAAAAAAABAABBBAABBABAAABAABAAAABBBBAABBBAABAABAAABABBAAAABAABAABABAABAAAAAAAABBAAABAA"""
print(bacon2text(crypto))


sometext = """All children, except one, grow up. They soon know that they will grow
up, and the way Wendy knew was this. One day when she was two years old
she was playing in a garden, and she plucked another flower and ran with
it to her mother. I suppose she must have looked rather delightful, for
Mrs. Darling put her hand to her heart and cried, "Oh, why can't you
remain like this for ever!" This was all that passed between them on
the subject, but henceforth Wendy knew that she must grow up. You always
know after you are two. Two is the beginning of the end.

Of course they lived at 14 [their house number on their street], and
until Wendy came her mother was the chief one. She was a lovely lady,
with a romantic mind and such a sweet mocking mouth. Her romantic
mind was like the tiny boxes, one within the other, that come from the
puzzling East, however many you discover there is always one more; and
her sweet mocking mouth had one kiss on it that Wendy could never get,
though there it was, perfectly conspicuous in the right-hand corner.""".lower()

lc2bin = {ch: '{:05b}'.format(i)
          for i, ch in enumerate(string.ascii_lowercase + ' .')}
bin2lc = {val: key for key, val in lc2bin.items()}

print(lc2bin)
print(bin2lc)

phrase = 'Rosetta code Bacon cipher example secret phrase to encode in the capitalisation of peter pan'.lower()


def to_5binary(msg):
    return (ch == '1' for ch in ''.join(lc2bin.get(ch, '') for ch in msg.lower()))


def encrypt(message, text):
    bin5 = to_5binary(message)
    textlist = list(text.lower())
    out = []
    for capitalise in bin5:
        while textlist:
            ch = textlist.pop(0)
            if ch.isalpha():
                if capitalise:
                    ch = ch.upper()
                out.append(ch)
                break
            else:
                out.append(ch)
        else:
            raise Exception('ERROR: Ran out of characters in sometext')
    return ''.join(out) + '...'


def decrypt(bacontext):
    binary = []
    bin5 = []
    out = []
    for ch in bacontext:
        if ch.isalpha():
            binary.append('1' if ch.isupper() else '0')
            if len(binary) == 5:
                bin5 = ''.join(binary)
                out.append(bin2lc[bin5])
                binary = []
    return ''.join(out)

'''
print('PLAINTEXT = \n%s\n' % phrase)
encrypted = encrypt(phrase, sometext)
print('ENCRYPTED = \n%s\n' % encrypted)
decrypted = decrypt(encrypted)
print('DECRYPTED = \n%s\n' % decrypted)
assert phrase == decrypted, 'Round-tripping error'
'''



'''
Comment encoder avec Bacon ? (Principe de chiffrement)
Le chiffrement utilise un alphabet de substitution simple, il n'y a pas de V (on utilise le U) ni de J (on utilise le I) basé sur 2 lettres (ici A et B)

A	AAAAA	B	AAAAB
C	AAABA	D	AAABB
E	AABAA	F	AABAB
G	AABBA	H	AABBB
I=J	ABAAA	K	ABAAB
L	ABABA	M	ABABB
N	ABBAA	O	ABBAB
P	ABBBA	Q	ABBBB
R	BAAAA	S	BAAAB
T	BAABA	U=V	BAABB
W	BABAA	X	BABAB
Y	BABBA	Z	BABBB
Exemple : DCODE est chiffré AAABB,AAABA,ABBAB,AAABB,AABAA

Un second alphabet est parfois préféré, il utilise un code pour chaque lettre :

A	AAAAA	B	AAAAB
C	AAABA	D	AAABB
E	AABAA	F	AABAB
G	AABBA	H	AABBB
I	ABAAA	J	ABAAB
K	ABABA	L	ABABB
M	ABBAA	N	ABBAB
O	ABBBA	P	ABBBB
Q	BAAAA	R	BAAAB
S	BAABA	T	BAABB
U	BABAA	V	BABAB
W	BABBA	X	BABBB
Y	BBAAA	Z	BBAAB
Comment décoder par Bacon ? (Principe de déchiffrement)
Le déchiffrement est une substitution simple avec l'alphabet Bilitère de Bacon.
'''


'''
Key
Original:  	a	b	c	d	e	f	g	h
Substitution:  	AAAAA	AAAAB	AAABA	AAABB	AABAA	AABAB	AABBA	AABBB
Original:  	i-j	k	l	m	n	o	p	q
Substitution:  	ABAAA	ABAAB	ABABA	ABABB	ABBAA	ABBAB	ABBBA	ABBBB
Original:  	r	s	t	u-v	w	x	y	z
Substitution:  	BAAAA	BAAAB	BAABA	BAABB	BABAA	BABAB	BABBA	BABBB


Key
Original:  	a	b	c	d	e	f	g	h	i
Substitution:  	AAAAA	AAAAB	AAABA	AAABB	AABAA	AABAB	AABBA	AABBB	ABAAA
Original:  	j	k	l	m	n	o	p	q	r
Substitution:  	ABAAB	ABABA	ABABB	ABBAA	ABBAB	ABBBA	ABBBB	BAAAA	BAAAB
Original:  	s	t	u	u	w	x	y	z
Substitution:  	BAABA	BAABB	BABAA	BABAB	BABBA	BABBB	BBAAA	BBAAB
'''


'''
To encode a message each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'.
'''