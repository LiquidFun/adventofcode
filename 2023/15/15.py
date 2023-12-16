from sys import stdin

def hash(s, val=0):
    return hash(s[1:], (val + ord(s[0])) * 17 % 256) if s else val

boxes = [{} for _ in range(256)]
s1 = s2 = 0
for step in stdin.read().strip().split(','):
    s1 += hash(step)
    match step.replace('-', '=').partition("="):
        case [label, "=", ""]:
            boxes[hash(label)].pop(label, None)
        case [label, "=", num]:
            boxes[hash(label)][label] = int(num)

for i, box in enumerate(boxes, 1):
    for j, num in enumerate(box.values(), 1):
        s2 += i * j * num

print(s1, s2, sep='\n')
