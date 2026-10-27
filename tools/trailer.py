"""STARLIFT's 15-second trailer: simulator clips cut with B-movie title cards, over the game's own INVASION march.

Needs the clips in CHStarlift/out/trailer (recorded with the t_*.txt scripts in CHStarlift/tools/scripts, see below) and
out/music_preview/song5.wav (sh tools/synthcheck.sh). Writes docs/trailer.mp4 (1024x1024, 30 fps). Run from the project:
    python tools/trailer.py

Clips: cl run CHStarlift/tools/scripts/t_title.txt out/trailer/title, t_dlv.txt out/trailer/dlv -D SL_DLV=1,
t_feast.txt out/trailer/feast -D SL_DLV=2, t_charge.txt out/trailer/charge, and t_bot.txt out/trailer/botN -D SL_BOT
-D SL_START=N for N = 2, 4, 5 (all with --card out/card/STARLIFT.DAT).
"""
import os
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageSequence

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIPS = os.path.join(ROOT, 'CHStarlift', 'out', 'trailer')
FR = os.path.join(CLIPS, 'frames')
S = 1024
GOLD, RED, WHITE, GREEN = (255, 204, 34), (238, 17, 34), (255, 255, 255), (123, 226, 106)
FONT = 'C:/Windows/Fonts/impact.ttf'


def clip(name, a, b, box=None):
    """frames a..b of a clip; box: a part of the 128x128 screen (x0, y0, x1, y1) to punch in on."""
    g = Image.open(os.path.join(CLIPS, name, ('bot' if name.startswith('bot') else name) + '.gif'))
    fr = [f.convert('RGB') for f in ImageSequence.Iterator(g)]
    if box:
        fr = [f.crop(tuple(v * 2 for v in box)) for f in fr]
    return [f.resize((S, S), Image.Resampling.NEAREST) for f in fr[a:b]]


def scan(im):                                        # faint scan lines, a CRT feel
    d = ImageDraw.Draw(im, 'RGBA')
    for y in range(0, S, 8):
        d.rectangle((0, y + 6, S, y + 7), fill=(0, 0, 0, 46))
    return im


def card(lines, n, bg=None, zoom=0.08):
    """n frames of big text, punching in a little; bg: frames to show darkened behind it."""
    out = []
    for i in range(n):
        im = bg[i % len(bg)].copy() if bg else Image.new('RGB', (S, S), (8, 6, 20))
        if bg:
            im = Image.blend(im, Image.new('RGB', (S, S), (0, 0, 0)), 0.45)
        d = ImageDraw.Draw(im)
        k = 1 + zoom * i / max(1, n - 1)
        total = sum(int(sz * k) + 18 for _, sz, _ in lines)
        y = (S - total) // 2
        for text, sz, col in lines:
            f = ImageFont.truetype(FONT, int(sz * k))
            w = d.textlength(text, font=f)
            x = (S - w) / 2
            d.text((x + 6, y + 6), text, font=f, fill=(0, 0, 0))
            d.text((x, y), text, font=f, fill=col)
            y += int(sz * k) + 18
        out.append(im)
    return out


def flash(fr, n=2):                                   # a white flash on the cut
    for i in range(min(n, len(fr))):
        fr[i] = Image.blend(fr[i], Image.new('RGB', (S, S), WHITE), 0.7 - i * 0.3)
    return fr


title = clip('title', 0, 90)
seq = []
seq += card([("THEY CAME FOR", 110, WHITE), ("OUR COLONISTS...", 120, GOLD)], 36)
seq += flash(clip('bot4', 40, 94))
seq += card([("...AND OUR", 110, WHITE), ("TAKEAWAY!", 170, RED)], 24)
seq += flash(clip('dlv', 12, 72))
seq += card([("ONE LANDER.", 150, GOLD)], 18)
seq += flash(clip('bot5', 240, 285))
seq += card([("BIG GUNS.", 160, RED)], 15)
seq += flash(clip('charge', 6, 44))
seq += card([("SANDWORMS!", 160, GOLD)], 15)
seq += flash(clip('bot2', 395, 435))
seq += card([("COWS?!", 200, WHITE)], 15)
seq += flash(clip('dlv', 84, 109, box=(72, 64, 120, 112)))   # punch in on the cow
seq += card([("FEAST", 170, GOLD), ("FIESTA!", 170, GREEN)], 30, bg=clip('feast', 20, 50), zoom=0.05)
end = []                                              # the real title screen, a strip along the bottom
for i in range(450 - len(seq)):
    im = title[(i + 20) % len(title)].copy()
    d = ImageDraw.Draw(im)
    d.rectangle((0, S - 84, S, S), fill=(8, 6, 20))
    f = ImageFont.truetype(FONT, 60)
    t = "A CHGAME ORIGINAL"
    d.text(((S - d.textlength(t, font=f)) / 2, S - 76), t, font=f, fill=GOLD if (i // 8) % 2 else WHITE)
    end.append(im)
seq += flash(end)
assert len(seq) == 450, len(seq)

shutil.rmtree(FR, ignore_errors=True)
os.makedirs(FR, exist_ok=True)
for i, im in enumerate(seq):
    scan(im).save(os.path.join(FR, 'f%03d.png' % i))
song = os.path.join(ROOT, 'out', 'music_preview', 'song5.wav')
out = os.path.join(ROOT, 'docs', 'trailer.mp4')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '30', '-i', os.path.join(FR, 'f%03d.png'), '-i', song,
                '-filter_complex', '[1:a]aresample=44100,atrim=0:15,afade=t=in:d=0.2,afade=t=out:st=14:d=1,volume=0.9[a]',
                '-map', '0:v', '-map', '[a]', '-c:v', 'libopenh264', '-pix_fmt', 'yuv420p', '-b:v', '6M', '-c:a', 'aac', '-b:a', '160k',
                '-shortest', out], check=True)
print('wrote', out)
