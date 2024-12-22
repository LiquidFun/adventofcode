s1, s2 = 0, {}
for num in map(int, open(0)):
    seen = set()
    last4 = (10, 10, 10, 10)
    for _ in range(2000):
        prev = num%10
        num ^= num*64 % 16777216
        num ^= num//32
        num ^= num*2048 % 16777216
        last4 = last4[1:] + (num%10 - prev,)
        if last4 not in seen:
            seen.add(last4)
            s2[last4] = s2.get(last4, 0) + num%10
    s1 += num

print(s1)
print(max(s2.values()))
