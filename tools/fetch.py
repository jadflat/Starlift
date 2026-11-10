"""STARLIFT's fetch-quest cargo (stage 3 on): 0-2 are lifted on the rope, 3-5 are landed on. Same HOUSE letters as life.py.
About 24 x 12: three times a pick-up, and big enough to read in the call-out's picture."""
FETCH = [
    ['.........kkkkkk.........',          # 0 rocket parts: a rocket engine, its bell and turbopump
     '........knnnnnnk........',
     '........knsssnnk...kk...',
     '.......kknnnnnnkk.knnk..',
     '.......ksyyyyyysk.knnk..',
     '......kssnnnnnnssknnnk..',
     '......ksnnnnnnnnsnnk....',
     '.....kssnnnnnnnnssk.....',
     '.....ksnnnnnnnnnnsk.....',
     '....kssnnnnnnnnnnssk....',
     '....ksnrrrrrrrrrrnsk....',
     '...kssssssssssssssssk...',
     '...kyyyykkkkkkkkyyyyk...',
     '...kkkkk........kkkkk...'],
    ['......kkkkkkkkkkkk......',          # 1 a reactor core: a glowing cylinder in a cradle
     '.....ksssssssssssk......',
     '....ksnnnnnnnnnnnsk.....',
     '....ksnkkkkkkkkknsk.....',
     '....ksnkgggggggknsk.....',
     '....ksnkgwwwwwgknsk.....',
     '....ksnkgggggggknsk.....',
     '....ksnkgwwwwwgknsk.....',
     '....ksnkgggggggknsk.....',
     '....ksnkkkkkkkkknsk.....',
     '....ksnnnnnnnnnnnsk.....',
     '.....ksssssssssssk......',
     '...kkkyykkkkkkkyykkk....',
     '...knnnnnnnnnnnnnnnk....'],
    ['kkkkkkkkkkkkkkkkkkkkkkkk',          # 2 a solar array on its mast
     'knwcwcwcwnnwcwcwcwnnwcwk',
     'kncwcwcwcnncwcwcwcnncwck',
     'knwcwcwcwnnwcwcwcwnnwcwk',
     'kncwcwcwcnncwcwcwcnncwck',
     'knwcwcwcwnnwcwcwcwnnwcwk',
     'kkkkkkkkkkkkkkkkkkkkkkkk',
     '..........kssk..........',
     '..........ksnk..........',
     '..........ksnk..........',
     '.......kkkksnkkkk.......',
     '......knnnnnnnnnnk......',
     '.....kssssssssssssk.....'],
    ['kkkkkkkkkkkkkkkkkkkkkkkk',          # 3 a supply crate: land on its lid
     'kyyyyyyyyyyyyyyyyyyyyyyk',
     'kynnnnnnnnnnnnnnnnnnnnyk',
     'kynyyyyyyyywwyyyyyyyynyk',
     'kynyyyyyyyywwyyyyyyyynyk',
     'kynyyyyywwwwwwwwyyyyynyk',
     'kynyyyyywwwwwwwwyyyyynyk',
     'kynyyyyyyyywwyyyyyyyynyk',
     'kynnnnnnnnnnnnnnnnnnnnyk',
     'kyyyyyyyyyyyyyyyyyyyyyyk',
     'kkkkkkkkkkkkkkkkkkkkkkkk'],
    ['..kkkkkkkkkkkkkkkkkkkk..',          # 4 a water tank on skids
     '.kwwssssssssssssssssssk.',
     'kwssssssssssssssssssssnk',
     'ksscccccccccccccccccccnk',
     'kscwwccccccccccccccccsnk',
     'ksccccccccccccccccccccnk',
     'ksscccccccccccccccccssnk',
     'kssssssssssssssssssssnnk',
     '.knnnnnnnnnnnnnnnnnnnnk.',
     '..kkkkkkkkkkkkkkkkkkkk..',
     '..knk..............knk..',
     'knnnnnk..........knnnnnk'],
    ['kkkkkkkkkkkkkkkkkkkkkkkk',          # 5 seed pods: a greenhouse kit
     'kwwwwwwwwwwwwwwwwwwwwwwk',
     'kwGGGGGwGGGGGwGGGGGwGGwk',
     'kwGgygGwGgrgGwGgygGwGgwk',
     'kwGgggGwGgggGwGgggGwGgwk',
     'kwGGGGGwGGGGGwGGGGGwGGwk',
     'kwwwwwwwwwwwwwwwwwwwwwwk',
     'knnnnnnnnnnnnnnnnnnnnnnk',
     'kkkkkkkkkkkkkkkkkkkkkkkk',
     '.knk................knk.'],
]


def _flag(kind, phase):
    """The three flags (0 the base's, 1 the aliens', 2 the Moon's), 11 x 9, the cloth waving: two frames (0.45: from code to the card)."""
    WAVE = [0, 0, 1, 1, 1, 0, 0, -1]
    g = [['.'] * 11 for _ in range(9)]
    for c in range(11):
        off = WAVE[(c + phase) & 7] if c > 1 else 0
        for r in range(7):
            if kind == 2:
                col = ('w' if (((c + r) & 1) and c and r and r < 3) else 'c') if (c < 5 and r < 4) else ('w' if r & 1 else 'r')
            elif kind == 1:
                d = (c - 5) ** 2 + (r - 3) ** 2 * 2
                col = 'k' if d == 0 else 'r' if d < 3 else 'w' if d < 9 else 'g'
            else:
                col = 'c' if r in (0, 6) else 'w'
                if (c == 5 and 2 <= r <= 4) or (r == 3 and 4 <= c <= 6): col = 'y'
            g[r + off + 1][c] = col
    return [''.join(x) for x in g]


FLAGS = [_flag(k, p) for k in range(3) for p in (0, 4)]


def _maw():
    """The hanging sandworm's head: a maw, pink inside, teeth top and bottom, 15 x 6 (0.45: from code to the card)."""
    g = [['k'] * 15 for _ in range(6)]
    for r in range(1, 5):
        for c in range(2, 13): g[r][c] = 'r' if (c + r) & 1 else 'w'
    for c in range(1, 14, 2): g[0][c] = g[1][c] = 'w'
    for c in range(0, 13, 2): g[5][c] = 'w'
    return [''.join(x) for x in g]


MAW = _maw()


WORM_UP = ['..kwkwkwkwk.',                  # the sandworm fully risen, for the who's-who (drawn from the game's own)
           '..kyyyyyyyk.',
           '..kyyyyyyyk.',
           '..kkkkkkkkk.',
           '..ssnnnnnnn.',
           '..kkkkkkkkk.',
           '.ssnnnnnnn..',
           '.kkkkkkkkk..',
           '.ssnnnnnnn..',
           'kkkkkkkkk...',
           'ssnnnnnnn...',
           'kkkkkkkkk...',
           '.ssnnnnnnn..',
           '.kkkkkkkkk..',
           'oooooooooooo']


HAZ_ICONS = {                               # the who's-who hazards page (0.46), about 12 x 10
    'HZ_LEAK':   ['....y.......', '...yy.......', '..yyyy......', '..yyyy...y..', '...yy...yyy.', '........yyy.', '.........y..'],
    'HZ_SNIPER': ['r...........', '.r..........', '..r.........', '...r........', '....r.......', '.....r.nn...', '......nssn..', '.....nnnnnn.', '....kkkkkkkk'],
    'HZ_TUNNEL': ['..w..w..w...', '..w..w..w...', '.www.w.www..', '..w.www.w...', '..w..w..w...', 'nnnnnnnnnnn.', 'nyyyyyyyyyn.', 'nnnnnnnnnnn.'],
    'HZ_MAG':    ['....yy......', '...yy.......', '..yyyyy.....', '....yy......', '...yy.......', '..yyyyy.....', '....yy......', '...y........'],
    'HZ_VENTS':  ['....rr......', '...ryyr.....', '...ryyr.....', '...rwyr.....', '...rwyr.....', '..rrwyrr....', 'kkkkkkkkkk..'],
    'HZ_METEORS':['y...........', '.r..........', '..r.........', '...yy.......', '...nns......', '..nnnns.....', '..nnnnn.....', '...nnn......'],
    'HZ_EVAC':   ['..kkkkkk....', '.kwwwwwwk...', 'kwwwkwwwwk..', 'kwwwkwwwwk..', 'kwwwkkkwwk..', 'kwwwwwwwwk..', '.kwwwwwwk...', '..kkkkkk....'],
}
