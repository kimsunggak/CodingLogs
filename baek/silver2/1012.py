"""
문제
<<<<<<< HEAD
MxN 크기의 배추밭에서 상하좌우로 인접한 배추의 집단이 몇개인지 구하는 프로그램을 작성하시오.

해결방법
- MxN 크기의 배추밭을 2차원 리스트로 표현한다.
- k번 반복하여 배추 밭에 배추를 1로 표시한다.
- 배추밭을 순회하며 1을 발견하면 DFS를 통해 인접한 배추를 모두 0으로 바꾼다.
- DFS를 통해 배추를 모두 0으로 바꾼 횟수를 result에 저장

부족한 부분
- 탐색하는 과정을 구현하지 못했다. 
- 재귀함수를 사용하여 인접한 배추 탐색을 구현해야 함
- 배추 밭의 범위를 넘어가거나 배추가 없는 경우를 조건문으로 처리하여
- 만족하지 않는경우 함수를 종료하도록 구현해야 함
- 인접한 배추를 모두 0으로 바꾼 후 result를 1 증가시켜야 함
"""
import sys
# 재귀 한도 늘리기
sys.setrecursionlimit(10000)

def dfs(x,y,m,n,field):
    if x <0 or x>=m or y <0 or y>=n or field[y][x] == 0:
        return
    field[y][x] = 0
    dfs(x+1,y,m,n,field)
    dfs(x-1,y,m,n,field)
    dfs(x,y+1,m,n,field)
    dfs(x,y-1,m,n,field)
 
def insect():
    m,n,k = map(int,sys.stdin.readline().split())
    field = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        field[y][x] = 1
    result = 0
    for i in range(n):
         for j in range(m):
             if field[i][j] == 1:
                 dfs(j,i,m,n,field)
                 result += 1
    print(result)    
if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        insect()
=======
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
>>>>>>> 64ec08b86bdcfd38e359ff12b26964a8841ba8df
