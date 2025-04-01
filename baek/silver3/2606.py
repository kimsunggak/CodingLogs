"""
문제
- 컴퓨터가 n 개 주어짐
- s개의 쌍만큼 연결되어 있음
- 1번 컴퓨터와 연결되어 있는 컴퓨터의 수를 구하는 프로그램을 작성

접근 방식
- 컴퓨터들을 노드로 생각하고 연결된 쌍을 간선으로 생각 , 무방향 그래프
- 연결되어 있으면 1 , 아니면 0
- n+1 크기의 2차원 배열 생성
- DFS(깊이 우선 탐색)으로 1번 컴퓨터와 연결된 컴퓨터를 찾기
- node 리스트에 탐색할 노드 저장
- 연결된 컴퓨터를 찾으면 node에 추가하고 카운트 +1 , 연결된 컴퓨터 체크 (True)

DFS vs BFS 간단 비교
- DFS (깊이 우선 탐색)
    - 스택(LIFO) 구조 사용 (`list.pop()` 이용)
    - 가능한 깊이까지 먼저 탐색한 후, 다시 돌아가며 다른 경로 탐색
    - 구현이 간단하고 재귀로도 가능
- BFS (너비 우선 탐색)
    - 큐(FIFO) 구조 사용 (`list.pop(0)` 또는 `collections.deque`)
    - 가까운 노드부터 차례대로 탐색
    - 최단 거리 문제에 적합

잘못 생각한 부분
- 처음에는 연결 여부를 확인하기 위해 in list를 사용했으나 이는 리스트 크기가 커질수록 오래걸려 비효율적임
- 불리언 리스트로 연결된 컴퓨터를 체크하는 것이 더 효율적임
- `append()`만 하고 방문 체크를 나중에 하면 중복 탐색 발생 가능성 있음  → 리스트에 넣기 **전에** 방문 체크를 수행해야 함
- *현재 연결된 컴퓨터의 위치를 저장하는 변수 마련해야 함
"""
import sys
n = int(sys.stdin.readline().strip()) # 컴퓨터의 개수
s = int(sys.stdin.readline().strip()) # 연결된 쌍의 개수
def main():
    graph = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(s):
        a,b = map(int,sys.stdin.readline().strip().split())
        graph[a][b] = 1
        graph[b][a] = 1
    # 1번 컴퓨터와 연결
    node = [1]
    result = 0
    connected = [False] * (n+1) # 연결된 컴퓨터 체크
    while node:
        current = node.pop() # 꺼내는 방식에 따라 DFS/BFS 결정될 수 있음
        for i in range(2,n+1):
            if graph[current][i] == 1 and not connected[i]:
                node.append(i)
                connected[i] = True
                result += 1
    print(result)
if __name__ == "__main__":
    main()        