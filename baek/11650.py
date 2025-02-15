"""
접근방식
- X좌표 오름차순 정렬 , x좌표가 같으면 y좌표 오름차순 정렬
"""
import sys
def main():
    N = int(sys.stdin.readline().strip())
    coordinates = []
    for _ in range(N):
        x,y = map(int,sys.stdin.readline().strip().split())
        coordinates.append((x,y))
    coordinates.sort(key = lambda x: (x[0],x[1]))
    for x,y in coordinates:
        print(x,y)
if __name__ == "__main__":
    main()