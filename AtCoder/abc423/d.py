
# n, k = map(int, input().split())
# chairs = k
# time = 0
# q = [list(map(int, input().split())) for _ in range(n)]
# q[0] = q[0]
# customers = []
# next_come = [q[0]]
# next_come_time = q[0][0]
# next_leave = None

# while q:
#     if next_leave is not None and next_leave[1] == time:
#         chairs += next_leave[2]
#         next_leave = None
#     if time >= next_come_time and chairs >= :
#         customers.append()
#     for i in q:
#         if q[0][0] <= time and chairs >= q[0][2]:
#             print(time)
#             q[0][1] += time
#             chairs -= q[0][2]
#             customers.append(q.pop(0))
#         else:
#             break
#     time += 1

# 途中でタイムアップ
