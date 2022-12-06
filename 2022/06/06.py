s = input()
def solve(n):
    for i in range(len(s)):
        if len(set(s[i:i+n])) == n:
            return i+n

print(solve(4))
print(solve(14))
