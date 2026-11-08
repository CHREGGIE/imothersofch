# Generates the brownstone line drawing used in the site footer.
# Usage: python3 tools/brownstones.py assets/brownstones.svg
# (then set stroke="#c4a5ba" on the root <svg> element)
import sys
W, G = 1200, 214          # canvas width, ground line y
out = []
def add(s): out.append(s)

def house(x, w, floors, door_left, bay=False, mansard=False):
    fh = 36                 # floor height
    base = 22               # raised basement height
    top = G - base - floors*fh - 14
    # facade
    add(f'<rect x="{x}" y="{top}" width="{w}" height="{G-top}"/>')
    # cornice + dentils
    add(f'<path d="M{x-5} {top} h{w+10} v-7 h-{w+10} z"/>')
    add(f'<path d="M{x+2} {top+5} h{w-4}" stroke-dasharray="2 4"/>')
    if mansard:
        add(f'<path d="M{x-5} {top-7} l10 -14 h{w-10} l10 14"/>')
        add(f'<rect x="{x+w/2-9}" y="{top-18}" width="18" height="11" rx="1"/>')
    # basement band + windows
    add(f'<path d="M{x} {G-base} h{w}"/>')
    # door column and window columns
    stoop_w = 30
    dx = x + 8 if door_left else x + w - 8 - 22
    cols_x0 = x + 8 + (stoop_w if door_left else 0)
    cols_w = w - 16 - stoop_w
    # basement windows (under the window columns)
    for i in range(2):
        bx = cols_x0 + 6 + i*(cols_w/2)
        add(f'<rect x="{bx:.1f}" y="{G-base+6}" width="{cols_w/2-12:.1f}" height="9"/>')
    # floors
    for f in range(floors):
        fy = G - base - (f+1)*fh
        if f == 0:
            # parlor floor: tall windows + arched door
            add(f'<path d="M{dx} {fy+fh} v-24 a11 11 0 0 1 22 0 v24"/>')
            add(f'<path d="M{dx+11} {fy+fh} v-24"/>')
        else:
            add(f'<rect x="{dx+3}" y="{fy+7}" width="16" height="24"/>')
            add(f'<path d="M{dx+1} {fy+5} h20"/>')
        if bay and f < floors - 1:
            add(f'<path d="M{cols_x0} {fy+fh} v-{fh-2} h{cols_w} v{fh-2}"/>')
            n = 3
            for i in range(n):
                wx = cols_x0 + 5 + i*(cols_w-10)/n
                add(f'<rect x="{wx:.1f}" y="{fy+7}" width="{(cols_w-10)/n-5:.1f}" height="24"/>')
        else:
            n = 2
            for i in range(n):
                wx = cols_x0 + 4 + i*cols_w/n
                ww = cols_w/n - 10
                if f == floors - 1:
                    add(f'<path d="M{wx:.1f} {fy+31} v-19 a{ww/2:.1f} 6 0 0 1 {ww:.1f} 0 v19 z"/>')
                else:
                    add(f'<rect x="{wx:.1f}" y="{fy+7}" width="{ww:.1f}" height="24"/>')
                    add(f'<path d="M{wx-2:.1f} {fy+5} h{ww+4:.1f}"/>')
    # stoop: steps from ground up to the door, going outward
    sx = dx - 6 if door_left else dx + 28
    steps = 6
    d = f'M{dx} {G-base}'
    # step profile toward the street (to the left of door if door_left... keep stoop in front)
    sx0, sw = dx - 2, 26
    for i in range(steps):
        y = G - base + i*base/steps
        add(f'<path d="M{sx0} {y:.1f} h{sw}"/>')
    add(f'<path d="M{sx0} {G-base} v{base} M{sx0+sw} {G-base} v{base}"/>')
    # railings
    add(f'<path d="M{sx0-4} {G-base-10} l-8 {base+10} M{sx0+sw+4} {G-base-10} l8 {base+10}"/>')

def tree(x, h=70):
    add(f'<path d="M{x} {G} v-{h-26}"/>')
    add(f'<path d="M{x-20} {G-h+30} a20 20 0 0 1 6 -26 a18 18 0 0 1 30 2 a20 20 0 0 1 4 28 a16 16 0 0 1 -26 6 a16 16 0 0 1 -14 -10 z"/>')

specs = [  # width, floors, door_left, bay, mansard
    (112, 3, True, False, False),
    (112, 3, True, True, False),
    (118, 4, False, False, True),
    (112, 3, True, False, False),
    (112, 3, False, True, False),
    (112, 3, False, False, False),
    (118, 4, True, False, False),
    (112, 3, True, True, False),
    (112, 3, False, False, True),
]
total = sum(s[0] for s in specs)
x = (W - total) / 2
for w, fl, dl, bay, man in specs:
    house(round(x), w, fl, dl, bay, man)
    x += w
tree(66, 96); tree(1134, 90); tree(22, 70); tree(1178, 66)
add(f'<path d="M0 {G} H{W}"/>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {G-200} {W} 202" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" role="img" aria-label="Line drawing of a row of Crown Heights brownstones">
  {chr(10).join("  "+s for s in out).strip()}
</svg>
'''
open(sys.argv[1], 'w').write(svg)
