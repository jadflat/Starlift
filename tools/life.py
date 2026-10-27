"""STARLIFT's living things and logos, pictures for the card.

  critters: two frames each (the game moves them): fliers BAT, JELLY, RAY and crawlers HOPPER, BEETLE, SNAIL
  giants:   one great creature (or machine) drifting through each world's sky, far away
  logos:    STARLIFT and GAME OVER in a chunky outlined pixel font with a gold-to-red fade

HOUSE letters: 'k' ink, 'w' white, 's' silver, 'n' steel, 'y' gold, 'r' red, 'g' green, 'G' dark green, 'c' the world's
accent, 'm' the upper sky, 'b' far hills, 'o' light ground.
"""
T = 15
KEY = {'.': T, 'k': 0, 'w': 1, 'G': 2, 'g': 3, 'l': 4, 's': 5, 'r': 6, 'm': 7, 'y': 8, 'b': 9, 'u': 10, 'n': 11, 'o': 12, 'c': 13}


def g(rows):
    w = max(len(r) for r in rows)
    return [[KEY[ch] for ch in r.ljust(w, '.')] for r in rows]


CRITTERS = {
    'BAT': (['k.......k', 'rk.....kr', '.rrkykrr.', '..rrrrr..', '...k.k...'],
            ['...kyk...', '..rrrrr..', '.rrk.krr.', 'rk.....kr', 'k.......k']),
    'JELLY': (['..ccc..', '.cwccc.', 'ccccccc', 'c.c.c.c', '.g.g.g.', 'g.g.g.g', '.g...g.'],
              ['.ccccc.', 'cwccccc', 'ccccccc', '.c.c.c.', '.g.g.g.', '.g.g.g.', 'g..g..g']),
    'RAY': (['k.........k', 'ck.......kc', '.cck.w.kcc.', '..ccccccc..', '....ccc....', '.....c.....', '......c....'],
            ['...........', '...........', 'kcck.w.kcck', '.ccccccccc.', '....ccc....', '.....c.....', '....c......']),
    'HOPPER': (['..ggg..', '.gwkgg.', 'gggggggG', '.GgggG..', '.G...G..'],
               ['.......', '.gggg..', 'gwkgggg', 'ggggggG', 'GGgggGG']),
    'BEETLE': (['..kkk...', '.krryrk.', 'krryrrrk', 'krrrrryk', '.k.k.k..'],
               ['..kkk...', '.krryrk.', 'krryrrrk', 'krrrrryk', 'k.k.k.k.']),
    'SNAIL': (['..yyy....', '.yykyy...', '.ykyky.w.', '.yyyyy.c.', 'ccccccccc'],
              ['..yyy....', '.yykyy..w', '.ykyky..c', '.yyyyy.c.', '.cccccccc']),
}
FLY_ORDER = ['BAT', 'JELLY', 'RAY']               # make_card.py's FLY numbers 1, 2, 3
CRAWL_ORDER = ['HOPPER', 'BEETLE', 'SNAIL']       # CRAWL numbers 1, 2, 3

GIANTS = {
    'SATELLITE': ['.ccc.....ccc.',
                  '.cwc.....cwc.',
                  '.ccc.sss.ccc.',
                  '.ccssywsscc..',
                  '.ccc.sns.ccc.',
                  '.cwc..s..cwc.',
                  '.ccc..r..ccc.'],
    'WORM': ['........oooo........',
             '......oobbbboo......',
             '....oobb....bboo....',
             '...obb........bbo...',
             '..obb..........bbo..',
             '.obb............bbo.',
             'obb..............bbo',
             'bb................bb'],
    'WHALE': ['......mmmmmm..........',
              '...mmmmmmmmmmmm.......',
              '.mmwmmmmmmmmmmmmmm..mm',
              'mmkmmmmmmmmmmmmmmmmmm.',
              '.mmmmmmmmmmmmmmmmm..mm',
              '..bbbbbbbbbbbbbb......',
              '....b..b..b...........'],
    'BIGJELLY': ['....ccccc....',
                 '..ccwcccccc..',
                 '.ccwccccccccc',
                 'ccccccccccccc',
                 'c.c.c.c.c.c.c',
                 '.g.g.g.g.g.g.',
                 '.g..g..g..g..',
                 'g...g...g..g.',
                 '.g.....g...g.'],
    'DRAGON': ['.........rr.......',
               'rr.....rrrrrk.....',
               '.rrr..rryrrrrrr...',
               '..rrrrrrrrrrrrrrrr',
               '...rrryyrrr...rr..',
               '....rr.rr..ry.....',
               '..........yy......'],
    'MOTHER': ['.......nnnn.......',
               '.....ncwwccn......',
               '..nnnnnnnnnnnnnn..',
               'nssssssssssssssssn',
               'syswsyswsyswsysws.',
               '.nnnnnnnnnnnnnnnn.',
               '....g..g..g..g....'],
    'MOTH': ['c.......c',
             'cc.....cc',
             'cwc.k.cwc',
             'cccckcccc',
             '.cc.k.cc.',
             '.c.....c.'],
}
# one per world, in WORLDS order (make_card.py): the Moon, Sabulon, Cryo, Verda, Vulcan, Titan, Prism, Zorg
GIANT_OF = ['SATELLITE', 'WORM', 'WHALE', 'BIGJELLY', 'DRAGON', 'WHALE', 'MOTH', 'MOTHER']
GIANT_ORDER = ['SATELLITE', 'WORM', 'WHALE', 'BIGJELLY', 'DRAGON', 'MOTHER', 'MOTH']

# a chunky 5 x 7 pixel font for the logos
FONT = {
    'S': ['.###.', '#...#', '#....', '.###.', '....#', '#...#', '.###.'],
    'T': ['#####', '..#..', '..#..', '..#..', '..#..', '..#..', '..#..'],
    'A': ['.###.', '#...#', '#...#', '#####', '#...#', '#...#', '#...#'],
    'R': ['####.', '#...#', '#...#', '####.', '#.#..', '#..#.', '#...#'],
    'L': ['#....', '#....', '#....', '#....', '#....', '#....', '#####'],
    'I': ['###', '.#.', '.#.', '.#.', '.#.', '.#.', '###'],
    'F': ['#####', '#....', '#....', '####.', '#....', '#....', '#....'],
    'G': ['.###.', '#...#', '#....', '#.###', '#...#', '#...#', '.###.'],
    'M': ['#...#', '##.##', '#.#.#', '#.#.#', '#...#', '#...#', '#...#'],
    'E': ['#####', '#....', '#....', '####.', '#....', '#....', '#####'],
    'O': ['.###.', '#...#', '#...#', '#...#', '#...#', '#...#', '.###.'],
    'V': ['#...#', '#...#', '#...#', '#...#', '.#.#.', '.#.#.', '..#..'],
    ' ': ['...', '...', '...', '...', '...', '...', '...'],
}


def logo(text, top, bottom):
    """The text at 2x, each row of the font its own colour (top..bottom fade), an ink outline and a drop shadow."""
    cols = []
    for ch in text:
        for c in range(len(FONT[ch][0])):
            cols.append([FONT[ch][r][c] == '#' for r in range(7)])
        cols.append([False] * 7)
    w, h = len(cols) * 2 + 4, 7 * 2 + 4
    p = [[T] * w for _ in range(h)]
    fade = top + bottom
    for x, col in enumerate(cols):
        for r in range(7):
            if col[r]:
                c = fade[min(len(fade) - 1, r * len(fade) // 7)]
                for dy in range(2):
                    for dx in range(2):
                        p[1 + r * 2 + dy][1 + x * 2 + dx] = KEY[c]
    q = [row[:] for row in p]
    for y in range(h):                                   # an ink outline, and a steel shadow down and right
        for x in range(w):
            if p[y][x] == T:
                if any(0 <= x + dx < w and 0 <= y + dy < h and p[y + dy][x + dx] not in (T, KEY['k'], KEY['n'])
                       for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    q[y][x] = KEY['k']
    for y in range(h - 1, 0, -1):
        for x in range(w - 1, 0, -1):
            if q[y][x] == T and q[y - 1][x - 1] == KEY['k'] and p[y - 1][x - 1] == T:
                q[y][x] = KEY['n']
    return q


LOGOS = {'STARLIFT': logo('STARLIFT', 'wyy', 'yyrr'), 'GAMEOVER': logo('GAME OVER', 'wrr', 'rrrm')}

# the giant food on each takeaway's pole (12 x 9), in make_card.py's FOOD order
FOODS = [
    ['..yyyyyyyy..', '.yyywyyywyy.', 'yyyyyyyyyyyy', 'gggggggggggg', 'rrrrrrrrrrrr', 'nnnnnnnnnnnn', 'yyyyyyyyyyyy', '.yyyyyyyyyy.'],   # a burger
    ['.......n..s.', '.......n.s..', '.yy.yy.ns...', 'y..y..y.y...', 'wwwwwwwwwwww', '.rrrrrrrrrr.', '..rrrrrrrr..', '...rrrrrr...'],   # noodles
    ['......r.....', '....wwww....', '...wwcwww...', '...wwwwww...', '....wwww....', '...yyyyyy...', '....ywyy....', '.....yy.....', '.....y......'],   # ice cream
    ['rrrrrrrrrrrr', '.yyyyyyyyyy.', '.yrryyyyrry.', '..yyyyyyyy..', '..yyyrryyy..', '...yyyyyy...', '....yyyy....', '.....yy.....'],   # pizza
    ['.rrrrrrrrrr.', 'rryrryrryrrr', 'rrrrrrrrrrrr', '.yyyyyyyyyy.', 'ywwwwwwwwwwy', '.yyyyyyyyyy.'],                                 # a hot dog
    ['.........y.y', '..sss...yyy.', '.ssssss.yyy.', 'skssssssrrr.', '.ssssss.rrr.', '..sss...rrr.', '........rrr.'],                  # fish and chips
    ['.kkk...kkk..', 'kwwwk.kwwwk.', 'kwrwk.kwcwk.', 'kwwwk.kwwwk.', '.kkk...kkk..'],                                               # sushi
    ['...g...g....', '....yyyy....', '..yyyyyyyy..', '.yynyynyyny.', 'yyyyyyyyyyyy', '.yyyyyyyyyy.'],                                 # a glorp pie
]
DESCENT = ['..wyyyyyyyyyyr..',                              # the old descent stage left on the Moon
           '..yyyyyyyyyyyr..',
           '..yynyyyyynyyr..',
           '..yyyyyyyyyyyr..',
           '..yyyynnnyyyyr..',
           '..n...nnn....n..',
           '.n...........n..',
           '.n............n.',
           'ss............ss']

GANTRY = ['..r...',                                         # the launch gantry by the start pad (the game blinks its light)
          '..n...'] + ['nnnnnn', 'n.n..n', 'n..n.n', 'n.n..n', 'n..n.n'] * 6
PUMP = ['wwww', 'yyyy', 'yyyy', 'ykky', 'ykky', 'yyyy', 'yyyy', 'ynny', 'yyyy']   # the fuel pump by the base pad

MOTHERSHIP = ['...............kkkkkkk...............',      # the boss: a mothership over the aliens' collector
              '.............kkcwwgggckk.............',
              '............kcwwgggggggck............',
              '............kggggggggggggk...........',
              '......kkkkkkkkkkkkkkkkkkkkkkkkk......',
              '...kkkwwssssssssssssssssssssssnnkkk..',
              '.kkwwssssssssssssssssssssssssssssnnkk',
              'kwsysssysssysssysssysssysssysssyssnnk',
              'knnsssssssssssssssssssssssssssssssnnk',
              '.kknnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnkk.',
              '...kkknnnnrnnnnnnnrnnnnnnnrnnnnkkk...',
              '......kkkkkkknngggggggnnkkkkkkk......',
              '............kkgglllllggkk............',
              '..............kkgggggkk..............']

SCOOTER = ['......kkk...........',                           # a takeaway speeder bike: a rider in a white helmet, a long fork
           '.....kwwwk..........',
           '.....kwkkk..........',
           '....kwwwk...........',
           '...kwwswk...k.......',
           '..kssssssskksk......',
           'kkssssssssssskkkkkkk',
           'kmnnnnssnnnnk...kssk',
           '.kk..kmmk.......kkk.']

COW = ['...........k.k', '.kkkkkkkkkkwwk', 'kwwwkkwwwwkwkw', 'kwwkkkwwwwkwwo', 'kwwwwwwkkwkwoo', '.kwwwwwwwwkkk.', '.kk.k...kk.k..', '.kk.k...kk.k..']   # a cow (beamed up by a saucer, knocked loose)
COWEAT = ['..............', '.kkkkkkkkkk...', 'kwwwkkwwwwkk..', 'kwwkkkwwwwkwk.', 'kwwwwwwkkwkwwk', '.kwwwwwwwwkwko', '.kk.k...kk.koo', '.kk.k...kk.k..']   # grazing, head down
COWUP = COW[::-1]   # tumbling: legs up

# the other three bosses (0.19): the Hive, the Prism warship, the Dreadnought
BOSS_HIVE = ['............kkkkkkkkkkkkk............', '.........kkkrrrrmrrrrmrrrkkk.........', '........krrwwrrmmrrrrrmmrrrrk........', '.......krwwrrrrrrrrrrrrrrrrrrk.......', '.....kkrrykkyrrrrykkyrrrrykkyrrk.....', '....krrrrkkrrrrrrkkrrrrrrkkrrrrrk....', '...kmrrrrrrrrrrrrrrrrrrrrrrrrrrrmk...', '...kmmrrmrrmrrmrrmrrmrrmrrmrrmrrmmk..', '....kmmmmmmmmmmmmmmmmmmmmmmmmmmmmk...', '....kkkkmkkkkmkkkkmkkkkmkkkkmkkkk....', '.......kmk..kmk..kmk..kmk..kmk.......', '.......k.....k.....k.....k....k......', '.........k.....k.....k.....k.........']
BOSS_PRISM = ['.................kkk.................', '................kkwcck...............', '..............kkwwcccckk.............', '............kkwwscccccsskk...........', '.........kkwwsssccccsssssnkk.........', '.......kkwssssssccssssssssnnkk.......', '.....kkwsssysssssssssssysssssnnkk....', '...kkwsssssssssskkkssssssssssssnnkk..', '.kkwssssssssssskkrkkssssssssssssnnkk.', '...kknnnnnnnnnnnkkknnnnnnnnnnnnnkk...', '.....kknnnnnnnnnnnnnnnnnnnnnnnkk.....', '.......kkkkcckkkkkkkkkkcckkkkk.......', '...........kcck.......kcck...........', '............kk.........kk............']
BOSS_DREAD = ['.........kkkkkkkkkkkkkkkkkkk.........', '......kkkwwsssssssssssssssnnkkk......', '.....kkwwssssssssssssssssssssnnkk....', '....kwsssskkkkksssssssskkkkkssssnk...', '...kwssskkrrrkksssssskkrrrkkssssnk...', '...kwssskrryrrksssssskrryrrkssssnk...', '...kwssskkrrrkkssskssskkrrrkkssssnk..', '..kkssssskkksssskkksssskkkssssssnkk..', '..kysssssssssssskkkkkssssssssssssyk..', '..knnsssskwkwkwkwkwkwkwkwkwssssssnnk.', '..kknnnnnkkkkkkkkkkkkkkkkknnnnnnnkk..', '....kkknnnnrnnnnnnnrnnnnnnnrnnnkkk...', '.......kkkkkkkkkkkkkkkkkkkkkkkk......']
