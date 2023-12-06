import re
get_nums = lambda string: [int(a) for a in re.findall("\d+", string)]

def solve(times, distances):
    times, distances = get_nums(times), get_nums(distances)
    result = 1
    for time, dist in zip(times, distances):
        result *= sum((time - start) * start > dist for start in range(time))
    return result

times, distances = input(), input()
print(solve(times, distances))
print(solve(times.replace(' ', ''), distances.replace(' ', '')))

