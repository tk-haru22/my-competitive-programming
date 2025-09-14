
def main():
    N, R = map(int, input().split())
    doors = ''.join(input().split())
    left = doors[:R].lstrip('1')
    right = doors[R:].rstrip('1')

    count = left.count('1')
    count += len(left)
    count += right.count('1')
    count += len(right)

    print(count)


if __name__ == '__main__':
    main()
