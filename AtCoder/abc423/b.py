from collections import deque

def main():
    input()
    doors = deque(map(int, input().split()))

    if 1 not in doors:
        print(0)
        return

    while doors[0] == 0:
        doors.popleft()
    while doors[-1] == 0:
        doors.pop()

    print(len(doors) - 1)

if __name__ == '__main__':
    main()
