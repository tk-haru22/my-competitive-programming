money, fee = map(int, input().split())

a = int(money / (1000 + fee))
print(a * 1000)
