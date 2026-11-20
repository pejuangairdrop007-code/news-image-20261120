#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news poster (1024x1024 PNG).

Deterministic: fixed palette, fixed geometry, no randomness, no time.
Run:  python3 gen_image.py   (writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

PAPER = (248, 244, 233)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
NAVY_LT = (38, 58, 99)
RED = (178, 34, 24)
GOLD = (201, 162, 39)
GREY = (90, 90, 86)
LINE = (180, 172, 150)
CARD = (255, 253, 247)
TEAL = (14, 110, 105)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    lines = wrap(draw, text, fnt, max_w)
    lh = leading or int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def tag(draw, x, y, label, fill=RED):
    f = font(SANS_B, 15)
    draw.text((x, y), label, font=f, fill=fill)
    return y + 22


# ---------------------------------------------------------------- icons
def icon_scales(d, cx, cy, s, col):
    # scales of justice: post, beam, two pans
    d.line([(cx, cy - s), (cx, cy + s)], fill=col, width=5)
    d.line([(cx - s, cy - s + 12), (cx + s, cy - s + 12)], fill=col, width=5)
    d.ellipse([cx - 7, cy - s - 7, cx + 7, cy - s + 7], fill=col)
    for sx in (-1, 1):
        px = cx + sx * s
        d.line([(px, cy - s + 12), (px - 16, cy - 8)], fill=col, width=3)
        d.line([(px, cy - s + 12), (px + 16, cy - 8)], fill=col, width=3)
        d.arc([px - 22, cy - 14, px + 22, cy + 22], 0, 180, fill=col, width=4)
    d.rectangle([cx - 26, cy + s - 4, cx + 26, cy + s + 4], fill=col)


def icon_flags(d, x, y, w, h, cols):
    n = len(cols)
    fw = w // n
    for i, c in enumerate(cols):
        fx = x + i * fw + 4
        d.line([(fx + fw // 2, y), (fx + fw // 2, y + h)], fill=INK, width=3)
        d.polygon([(fx + fw // 2, y + 4), (fx + fw - 6, y + 12),
                   (fx + fw // 2, y + 22)], fill=c)


def icon_burst(d, cx, cy, r, col):
    pts = []
    import math
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=col)
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=PAPER)


def icon_tower(d, x, y, w, h, col):
    d.polygon([(x + w * 0.30, y + h), (x + w * 0.30, y + h * 0.25),
               (x + w * 0.50, y), (x + w * 0.70, y + h * 0.25),
               (x + w * 0.70, y + h)], fill=col)
    for i in range(5):
        yy = y + h * 0.30 + i * h * 0.13
        d.line([(x + w * 0.34, yy), (x + w * 0.66, yy)], fill=PAPER, width=2)
    d.line([(x + 4, y + h), (x + w - 4, y + h)], fill=col, width=4)


def icon_chart(d, x, y, w, h, col):
    pts = [(x + 6, y + h - 12), (x + w * 0.30, y + h * 0.55),
           (x + w * 0.52, y + h * 0.72), (x + w * 0.75, y + h * 0.28),
           (x + w - 8, y + 10)]
    d.line(pts, fill=col, width=6, joint="curve")
    d.polygon([(x + w - 20, y + 6), (x + w - 4, y + 6), (x + w - 4, y + 22)],
              fill=col)
    d.line([(x + 4, y + h - 6), (x + w - 4, y + h - 6)], fill=GREY, width=3)


def icon_check(d, cx, cy, r, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=6)
    d.line([(cx - r * 0.5, cy), (cx - r * 0.1, cy + r * 0.45),
            (cx + r * 0.55, cy - r * 0.45)], fill=col, width=7, joint="curve")


# ---------------------------------------------------------------- build
def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)
    d.rectangle([12, 12, W - 13, H - 13], outline=LINE, width=1)

    # ---- masthead
    d.rectangle([14, 14, W - 15, 148], fill=NAVY)
    d.text((512, 26), "THE WORLD TODAY", font=font(SERIF_B, 62),
           fill=(255, 255, 255), anchor="ma")
    d.line([(60, 104), (964, 104)], fill=GOLD, width=3)
    d.text((512, 114), "FRIDAY, 20 NOVEMBER 2026",
           font=font(SANS_B, 26), fill=GOLD, anchor="ma")

    # ---- lead story: ICJ / Myanmar
    y0 = 164
    d.rectangle([24, y0, 1000, 428], fill=CARD, outline=LINE, width=2)
    d.rectangle([40, y0 + 16, 218, y0 + 248], fill=(233, 226, 205))
    icon_scales(d, 129, y0 + 128, 62, NAVY)
    tag(d, 238, y0 + 18, "THE HAGUE  •  JUSTICE  •  LEAD STORY")
    y = text_block(d, 238, y0 + 46, "WORLD COURT: MYANMAR",
                   font(SERIF_B, 40), INK, 740)
    y = text_block(d, 238, y, "COMMITTED GENOCIDE",
                   font(SERIF_B, 40), INK, 740)
    y = text_block(d, 238, y + 8,
                   "The International Court of Justice rules Myanmar "
                   "committed genocide against the Rohingya — the first "
                   "such finding against a state.",
                   font(SANS, 21), INK, 740, leading=28)
    d.text((238, y + 10), "Ruling 9–6  •  Mass killings and sexual violence in "
           "Rakhine State, 2017",
           font=font(SANS_B, 16), fill=GREY)

    # ---- row 2: two half-width stories
    y1, y2 = 444, 690
    # summit
    d.rectangle([24, y1, 500, y2], fill=CARD, outline=LINE, width=2)
    icon_flags(d, 44, y1 + 20, 150, 74, [RED, GOLD, NAVY])
    tag(d, 44, y1 + 104, "SHENZHEN  •  DIPLOMACY")
    y = text_block(d, 44, y1 + 130, "TRUMP, XI & PUTIN HOLD FIRST THREE-WAY SUMMIT",
                   font(SERIF_B, 25), INK, 436, leading=30)
    text_block(d, 44, y + 6, "Leaders issue a joint peace declaration after "
               "70 minutes of talks.",
               font(SANS, 17), INK, 436, leading=22)
    # kyiv
    d.rectangle([524, y1, 1000, y2], fill=CARD, outline=LINE, width=2)
    icon_burst(d, 590, y1 + 58, 44, RED)
    tag(d, 660, y1 + 34, "KYIV  •  WAR")
    text_block(d, 660, y1 + 60, "OVERNIGHT STRIKES HIT KYIV",
               font(SERIF_B, 26), INK, 320, leading=32)
    text_block(d, 660, y1 + 126, "Russian missiles kill three and damage three "
               "Dnipro bridges; Ukraine hits the Kerch Bridge again.",
               font(SANS, 17), INK, 320, leading=23)
    d.text((544, y1 + 208), "Allies meet in Berlin: Europe ready to talk with Russia.",
           font=font(SANS_B, 15), fill=GREY)

    # ---- row 3: three stories
    y3, y4 = 706, 950
    cols = [(24, 336), (356, 668), (688, 1000)]
    # riyadh
    x0, x1 = cols[0]
    d.rectangle([x0, y3, x1, y4], fill=CARD, outline=LINE, width=2)
    icon_tower(d, x0 + 104, y3 + 12, 90, 92, NAVY)
    tag(d, x0 + 16, y3 + 112, "RIYADH  •  MIDDLE EAST")
    y = text_block(d, x0 + 16, y3 + 138, "HOUTHI MISSILE HITS RIYADH TOWER",
                   font(SERIF_B, 21), INK, x1 - x0 - 32, leading=26)
    text_block(d, x0 + 16, y + 6, "Saudi wealth-fund tower hit; more missiles "
               "intercepted Friday.",
               font(SANS, 15), INK, x1 - x0 - 32, leading=20)
    # markets
    x0, x1 = cols[1]
    d.rectangle([x0, y3, x1, y4], fill=CARD, outline=LINE, width=2)
    icon_chart(d, x0 + 92, y3 + 14, 130, 82, TEAL)
    tag(d, x0 + 16, y3 + 112, "NEW YORK  •  MARKETS")
    y = text_block(d, x0 + 16, y3 + 138, "ANTHROPIC SOARS ON NASDAQ DEBUT",
                   font(SERIF_B, 21), INK, x1 - x0 - 32, leading=26)
    text_block(d, x0 + 16, y + 6, "First pure AI listing closes 17% above IPO "
               "price; Nikkei down 4.8%.",
               font(SANS, 15), INK, x1 - x0 - 32, leading=20)
    # kenya
    x0, x1 = cols[2]
    d.rectangle([x0, y3, x1, y4], fill=CARD, outline=LINE, width=2)
    icon_check(d, x0 + 156, y3 + 58, 44, TEAL)
    tag(d, x0 + 16, y3 + 112, "KENYA  •  HEALTH")
    y = text_block(d, x0 + 16, y3 + 138, "KENYA'S LAST EBOLA PATIENT GOES HOME",
                   font(SERIF_B, 21), INK, x1 - x0 - 32, leading=26)
    text_block(d, x0 + 16, y + 6, "Outbreak ends 37 days after the first case — "
               "no new infections.",
               font(SANS, 15), INK, x1 - x0 - 32, leading=20)

    # ---- footer
    d.line([(24, 968), (1000, 968)], fill=LINE, width=2)
    d.text((512, 976), "Six stories that shaped the world  •  Friday 20 November 2026",
           font=font(SANS_B, 17), fill=GREY, anchor="ma")

    img.save(OUT, format="PNG", optimize=True)


if __name__ == "__main__":
    build()
    print("wrote", OUT)
