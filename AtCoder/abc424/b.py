N, num_tasks, num_events = map(int, input().split())

acs = [[False] * num_tasks for _ in range(N)]
completed = []

for _ in range(num_events):
    idx, tsk = map(int, input().split())
    tasks = acs[idx - 1]
    tasks[tsk - 1] = True
    if all(tasks):
        completed.append(idx)

if completed:
    print(*completed)
