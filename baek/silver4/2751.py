import sys
def main():
    N = int(sys.stdin.readline().strip())
    num = []
    for _ in range(N):
        num.append(int(sys.stdin.readline().strip()))
    num.sort()
    for n in num:
        print(n)
if __name__ == "__main__":
    main()