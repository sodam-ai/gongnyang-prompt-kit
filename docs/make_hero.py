#!/usr/bin/env python3
"""docs/hero.gif — 공냥 프롬프트 킷 컴파일 데모 (거친 요청 → 완성 프롬프트 타이핑).
의존성: Pillow + Malgun(한글) + D2Coding(한글 모노).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 600
BG, PANEL, PAN2, LINE = (11,13,18), (19,22,31), (23,27,38), (36,41,56)
INK, DIM, MINT, GOLD = (238,241,247), (139,147,167), (94,234,212), (244,207,122)

MAL  = "/mnt/c/Windows/Fonts/malgun.ttf"
MALB = "/mnt/c/Windows/Fonts/malgunbd.ttf"
D2   = "/home/seunghyeong/.fonts/d2coding/D2Coding-Ver1.3.2-20180524.ttf"
f_word = ImageFont.truetype(MALB, 30)
f_tag  = ImageFont.truetype(MAL, 15)
f_sm   = ImageFont.truetype(MAL, 15)
f_rough= ImageFont.truetype(MALB, 29)
f_code = ImageFont.truetype(D2, 19)
f_arr  = ImageFont.truetype(D2, 40)

def rr(d, box, r, **kw): d.rounded_rectangle(box, radius=r, **kw)

def cat_mark(d, cx, cy, s, col):
    d.polygon([(cx-s,cy-s*0.2),(cx-s*0.55,cy-s*1.05),(cx-s*0.15,cy-s*0.35)], outline=col, width=3)
    d.polygon([(cx+s,cy-s*0.2),(cx+s*0.55,cy-s*1.05),(cx+s*0.15,cy-s*0.35)], outline=col, width=3)
    d.ellipse([cx-s,cy-s*0.5,cx+s,cy+s*0.9], outline=col, width=3)
    d.ellipse([cx-s*0.42-2,cy+s*0.05-2,cx-s*0.42+2,cy+s*0.05+2], fill=col)
    d.ellipse([cx+s*0.42-2,cy+s*0.05-2,cx+s*0.42+2,cy+s*0.05+2], fill=col)

# 완성 프롬프트 → (글자, 색) 토큰 + 줄바꿈 마커 "\n"
LINES = [
    ("Scene: ", "상단 굵은 세리프 타이틀, 중앙 달·야시장 일러스트, 하단 카피 여백.", MINT),
    ("Camera: ", "정면 중앙 정렬, 풀블리드.", MINT),
    ("Lighting: ", "부드러운 소프트박스 균등광, 옅은 콘택트 섀도.", MINT),
    ("Color: ", "#0F1D30 · #F7F4EC · #B76E79.", MINT),
    ("Text: ", '"봄밤 야시장" 상단, 한 번씩만 또렷하게.', MINT),
    ("AR 4:5", "", GOLD),
]
tokens = []  # (char, color) ; ('\n', None) = 줄바꿈
for lbl, body, col in LINES:
    for ch in lbl: tokens.append((ch, col))
    for ch in body: tokens.append((ch, INK if body else col))
    tokens.append(("\n", None))
TOTAL = sum(1 for c,_ in tokens if c != "\n")

CARD_L, CARD_R = 578, 1240
TX0, TXMAX = 604, 1212
LINE_H = 30

def draw_tokens(d, n, show_cursor):
    """앞에서 n글자(줄바꿈 제외)까지 그린다. 폭 넘으면 자동 줄바꿈."""
    x, y = TX0, 200
    drawn = 0
    last = (x, y)
    for ch, col in tokens:
        if ch == "\n":
            x = TX0; y += LINE_H; continue
        if drawn >= n: break
        w = f_code.getbbox(ch)[2]
        if x + w > TXMAX:
            x = TX0; y += LINE_H
        d.text((x, y), ch, font=f_code, fill=col)
        x += w; drawn += 1; last = (x, y)
    if show_cursor:
        d.text((last[0]+2, last[1]), "▌", font=f_code, fill=MINT)

FRAMES, TYPE_F = 56, 40
frames = []
for fi in range(FRAMES):
    img = Image.new("RGB", (W, H), BG)
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); do = ImageDraw.Draw(ov)
    do.ellipse([850,-180,1500,360], fill=(94,234,212,16))
    do.ellipse([-260,80,360,560], fill=(244,207,122,10))
    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(img)

    cat_mark(d, 52, 44, 16, MINT)
    d.text((78, 30), "공냥 프롬프트 킷", font=f_word, fill=INK)
    rt = "Claude Code Skill · gpt-image-2"
    d.text((W-40-d.textlength(rt, font=f_sm), 40), rt, font=f_sm, fill=DIM)
    d.line([(40,84),(W-40,84)], fill=LINE, width=1)

    rr(d, [40,130,520,470], 16, fill=PANEL, outline=LINE, width=1)
    d.text((64,154), "거친 요청", font=f_tag, fill=DIM)
    for i, ln in enumerate(['"봄밤 야시장','포스터 하나','만들어줘"']):
        d.text((64, 222+i*52), ln, font=f_rough, fill=INK)

    puls = 0.55 + 0.45*abs(((fi%20)/20)*2-1)
    acol = tuple(int(MINT[k]*puls + DIM[k]*(1-puls)) for k in range(3))
    d.text((540, 278), "→", font=f_arr, fill=acol)

    rr(d, [CARD_L,130,1240,560], 16, fill=PAN2, outline=LINE, width=1)
    d.text((604,154), "완성 프롬프트 · C3 한국어 포스터", font=f_tag, fill=DIM)

    n = TOTAL if fi >= TYPE_F else int(TOTAL*(fi+1)/TYPE_F)
    blink = (fi < TYPE_F) or ((fi//3) % 2 == 0)
    draw_tokens(d, n, show_cursor=blink)

    frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=72))

frames[0].save("docs/hero.gif", save_all=True, append_images=frames[1:],
               duration=90, loop=0, optimize=True, disposal=2)
print("wrote docs/hero.gif frames=", len(frames))
