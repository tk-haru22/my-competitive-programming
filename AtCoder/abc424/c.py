import sys
N = int(input())

skills: dict[int, tuple] = {i: tuple(map(int, input().split())) for i in range(1, N + 1)}

sys.setrecursionlimit(10 ** 6)

def check(s: dict[int, tuple], k: int, visited=None):
    if visited is None:
        visited = set()
    visited.add(k)
    if s[k] == (0, 0):
        return s, True
    if s[k][0] != k and s[k][0] not in visited:
        s, result = check(s, s[k][0], visited)
        if result:
            s[k] = (0, 0)
            return s, True
    if s[k][1] != k and s[k][1] not in visited:
        s, result = check(s, s[k][1], visited)
        if result:
            s[k] = (0, 0)
            return s, True
    return s, False

for i in range(1, N + 1):
    skills, _ = check(skills, i)

c = 0
for v in skills.values():
    if v == (0, 0):
        c += 1

print(c)
