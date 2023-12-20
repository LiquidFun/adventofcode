from collections import deque
import math

modules = {}
flipflops = {}
conjunctions = {}
rx_parent = ''

for line in open(0):
    name, destinations = line.strip().split(" -> ")
    pure_name = name.strip("&%")
    modules[pure_name] = destinations.split(', ')
    if name[0] == '%':
        flipflops[pure_name] = False
    elif name[0] == '&':
        conjunctions[pure_name] = {}

for name, destinations in modules.items():
    for dest in destinations:
        if dest in conjunctions:
            conjunctions[dest][name] = False
        if dest == 'rx':
            rx_parent = name

q = deque()
counts = [0, 0]
rx_repeats = [False] * len(conjunctions[rx_parent])

def push(name, i, send=False):
    if name in flipflops:
        send = flipflops[name]
    elif name in conjunctions:
        send = not all(conjunctions[name].values())

    if name == rx_parent:
        for j, is_good in enumerate(conjunctions[rx_parent].values()):
            if is_good:
                rx_repeats[j] = i

    for dest in modules.get(name, []):
        counts[send] += 1
        if dest in flipflops:
            if not send:
                flipflops[dest] = not flipflops[dest]
                q.append(dest)
        elif dest in conjunctions:
            conjunctions[dest][name] = send
            q.append(dest)

for i in range(1, 100000):
    q.append("broadcaster")
    counts[0] += 1
    while q:
        push(q.popleft(), i)

    if i == 1000:
        print(counts[0] * counts[1])

    if all(rx_repeats):
        print(math.prod(rx_repeats))
        break
