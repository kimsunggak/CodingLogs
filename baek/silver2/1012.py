"""
문제
- M x N 크기의 배추밭에서 배추가 심어져 있는 곳은 1, 심어져 있지 않은 곳은 0으로 표시된다.
- 밀집되어있는 배추 집단의 개수를 구하여라 

접근방법
- 지렁이 개수를 구하는 문제지만 인접된 배추 집단 하나당 지렁이 한마리로 처리할 수 있으므로 같은 거임
- 밭 전체를 0으로 초기화한다
- 배추가 심어져 있는 곳은 1로 표시한다.



"""
import sys
def worm(m,n,cabbage):
    field = [[0]*m for _ in range(n)]
    for x,y in cabbage:
        field[x][y] = 1
    

if __name__ == "__main__":
    for i in range(int(sys.stdin.readline().strip())):
        cabbage = []
        m,n,k = map(int,sys.stdin.readline().split())
        for _ in range(k):
            cabbage.append(list(map(int,sys.stdin.readline().split())))