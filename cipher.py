import re
import string

bacon1_map_enc_bin = {'a': '00000', 'b': '00001', 'c': '00010', 'd': '00011', 'e': '00100',
                      'f': '00101', 'g': '00110', 'h': '00111', 'i': '01000', 'j': '01000',
                      'k': '01001', 'l': '01010', 'm': '01011', 'n': '01100', 'o': '01101',
                      'p': '01110', 'q': '01111', 'r': '10000', 's': '10001', 't': '10010',
                      'u': '10011', 'v': '10011', 'w': '10100', 'x': '10101', 'y': '10110',
                      'z': '10111', }

bacon1_map_dec_bin = {val: key for key, val in bacon1_map_enc_bin.items()}
bacon1_map_dec_bin[bacon1_map_enc_bin['i']] = 'i'
bacon1_map_dec_bin[bacon1_map_enc_bin['u']] = 'u'

bacon2_map_enc_bin = {'a': '00000', 'b': '00001', 'c': '00010', 'd': '00011', 'e': '00100',
                      'f': '00101', 'g': '00110', 'h': '00111', 'i': '01000', 'j': '01001',
                      'k': '01010', 'l': '01011', 'm': '01100', 'n': '01101', 'o': '01110',
                      'p': '01111', 'q': '10000', 'r': '10001', 's': '10010', 't': '10011',
                      'u': '10100', 'v': '10101', 'w': '10110', 'x': '10111', 'y': '11000',
                      'z': '11001', }

bacon2_map_dec_bin = {val: key for key, val in bacon2_map_enc_bin.items()}

def bacon_decrypt(text, version=1, swapAB=False):
    text = text.lower().strip()
    text = text.replace(' ', '')
    code = []
    result = []
    for c in text:
        if c.isalpha():
            if c in ['0', 'a']:
                code.append('0')
            elif c in ['1', 'b']:
                code.append('1')
            else:
                raise ('Not a valid bacon text!')
            if len(code) == 5:
                if swapAB:
                    code = ['1' if c == '0' else '0' for c in code]
                code5 = ''.join(code)
                if version == 1:
                    # Possible KeyError
                    result.append(bacon1_map_dec_bin[code5])
                else:
                    result.append(bacon2_map_dec_bin[code5])
                code = []
    return ''.join(result)

def bacon_encrypt(text, version=1, swapAB=False):
    text = list(text.lower())
    result = []
    while text:
        c = text.pop(0)
        if c.isalpha():
            if version == 1:
                code = bacon1_map_enc_bin[c]
            else:
                code = bacon2_map_enc_bin[c]
            result.append(code)
    result = ''.join(result)
    if swapAB:
        result = result.replace('0', 'B')
        result = result.replace('1', 'A')
    else:
        result = result.replace('0', 'A')
        result = result.replace('1', 'B')
    return result

