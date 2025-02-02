import sys

if sys.version_info.major == 3:
    unichr = chr

FACES = 'FBA23456789TJCQK'
UNICODE_FACES = 'F0123456789ABCDE'
SUITS = 'SHDC'
UNICODE_SUITS = 'ABCD'
COLORS = ['\x1b[%dm' % c for c in (30, 31, 34, 32, 39)]


def unicard(card, color=False):
    if card[:2] == '10':
        card = 'T' + card[2]
    if card[:1].upper() == 'B':
        face, suit = 'BS'
    if card[:1].upper() == 'F':
        face, suit = 'FC'
    else:
        face, suit = card.upper()
    c = unichr(int('0001f0%s%s' % (
        UNICODE_SUITS[SUITS.index(suit)],
        UNICODE_FACES[FACES.index(face)]
    ), base=16))
