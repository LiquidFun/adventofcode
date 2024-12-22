from collections import Counter

s1 = [0]

def secret(num):
    prices = Counter()
    last4 = (10,10,10,10)
    for i in range(2000):
        prev = num%10
        num ^= (num*64) % 16777216
        num ^= (num//32) % 16777216
        num ^= (num*2048) % 16777216
        last4 = last4[1:] + (num%10 - prev,)
        if last4 not in prices:
            prices[last4] = num%10
    s1[0] += num
    return prices

ints = map(int, open(0))
c = sum(map(secret, ints), Counter())
print(s1[0])
print(sorted(c.values())[-1])
