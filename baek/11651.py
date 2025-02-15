import sys
def main():
    n = int(sys.stdin.readline().strip())
    coordinates = []
    for _ in range(n):
        x,y = map(int,sys.stdin.readline().strip().split())
        coordinates.append((x,y))
    coordinates.sort(key = lambda x : (x[1],x[0]))
    for x,y in coordinates:
        print(x,y)
if __name__ == "__main__":
    main()