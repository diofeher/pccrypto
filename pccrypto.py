#! /usr/bin/python
import re
import argparse
import copy

BIGGER = {
    'P2C559CK': 'dele',
    'VC8': 'm',
    '6559': 't',
    '659': 'r',
    '959': 'r',
    '854': 'c',
    '723': 'g',
    '491': 'z',
    '148': 'j',
    ' ': ' '
}

DIGRAPH = {
    '9C': 'a',
    '6C': 'a',
    'K9': 'l',
    'CK': 'e',
    'M5': 'f',
    '4M': 's',
    'F7': 'v',
    'XT': 'i',
    'P2': 'd',
    'HN': 'u',
    'B5': 'p',
    'D2': 'q',
    'G3': 't',
    'W2': 'n',
    'A3': 'o',
    'Z3': 'o',
    'V8': 'm',
    'X1': 'b',
    'OP': 'w',
    '8A': 't',
}

tmp = copy.copy(BIGGER)
tmp.update(DIGRAPH)
TO_PCC = dict((v,k) for k,v in tmp.items())
del tmp

class PCCrypto(object):
    def encrypt(self, text):
        text = text.lower()
        res = []
        for ch in text:
            res.append(TO_PCC[ch])
        return ''.join(res)

    def decrypt(self, enc_text):
        final_text = []
        for key, value in BIGGER.items():
            enc_text = enc_text.replace(key, value)

        for word in enc_text.split():
            result = []
            for sylab in re.split('([A-Z0-9]{2})', word):
                if DIGRAPH.get(sylab):
                    result.append(DIGRAPH[sylab])
                else:
                    result.append(sylab)
            final_text.append(''.join(result))

        return ' '.join(final_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encriptar/Decriptar mensagens do PCC')
    parser.add_argument('cmd', choices=['encrypt', 'decrypt'],
        help='encriptar ou decriptar')
    parser.add_argument('text', type=str, help='Texto')

    args = parser.parse_args()
    pcc = PCCrypto()
    print( getattr(pcc, args.cmd)(args.text) )
