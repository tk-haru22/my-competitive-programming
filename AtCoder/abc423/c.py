# これはバックアップ
# AC したコードは c2.py

def main():
    _, now = map(int, input().split())
    doors = ''.join(input().split())
    if now == 0:
        doors = doors.rstrip('1')
    elif now == len(doors):
        doors = doors.lstrip('1')
    else:
        doors = doors.strip('1')
    print(len(doors) + doors.count('1'))


if __name__ == '__main__':
    main()
