from functools import cache

N = {'7':0, '8':1, '9':2, '4':1j, '5':1+1j, '6':2+1j, 
      '1':2j, '2':1+2j, '3':2+2j, ' ':3j, '0':1+3j, 'A':2+3j}
R = {' ':0, '^':1, 'A':2, '<':1j, 'v':1+1j, '>':2+1j}

@cache
def path(start, end):
    pad = N if (start in N and end in N) else R
    diff = pad[end] - pad[start]
    dx, dy = int(diff.real), int(diff.imag)
    yy = ("^"*-dy) + ("v"*dy)
    xx = ("<"*-dx) + (">"*dx)

    bad = pad[" "] - pad[start]
    prefer_yy_first = (dx>0 or bad==dx) and bad!=dy*1j
    return (yy+xx if prefer_yy_first else xx+yy) + "A"
    
@cache
def length(code, depth, s=0):
    if depth == 0: return len(code)
    for i, c in enumerate(code):
        s += length(path(code[i-1], c), depth-1)
    return s

codes = open(0).read().split()
print(sum(int(code[:-1]) * length(code, 3) for code in codes))
print(sum(int(code[:-1]) * length(code, 26) for code in codes))
