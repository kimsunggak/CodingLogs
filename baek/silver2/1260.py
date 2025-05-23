"""
문제
- 정점의 개수 N과 간선의 개수 M, 시작 정점 번호 V가 주어짐
- 간선이 연결하는 두 정점의 번호가 M개 주어짐
- DFS와 BFS를 수행한 결과를 프로그램으로 구현하라

접근 방법
- 2차원 리스트로 그래프를 표현
- BFS와 DFS를 각각 함수로 구현

배운점
- 그래프를 2차원 리스트로 표현했는데 어떻게 탐색하는지 접근을 못함
- 방문했던 노드에 대한 처리를 어떻게 해야하는지 고민함
- 노드에서 다음 노드로 가는 방법을 queue와 스택을 이용해서 구현해야 했음
- 개선사항으로 BFS구현할 때는 deque를 사용하는게 좋음
- queue.pop(0)으로 하면 시간복잡도가 O(n)임
- queue.popleft()로 하면 O(1)임
"""
import sys
def graph(n,m):
    node = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        node[a].append(b)
        node[b].append(a)
    for node_list in node:
        node_list.sort()
    return node
def bfs(Node,n,v):
    result = []
    visited = [False] * (n+1)
    queue = [v]
    visited[v] = True
    front = 0
    # queue의 길이만큼 앞에꺼부터 빼기
    # 이렇게하면 시작 복잡도가 O(1)임
    while front < len(queue):
        cur = queue[front]
        front += 1
        result.append(cur)
        for i in Node[cur]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    print(*result)
        
def dfs(Node,n,v):
    visited = [False] * (n+1)  
    stack = [v]
    result = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            result.append(v)
            for i in reversed(Node[v]):
                if not visited[i]:
                    stack.append(i)
    print(*result)
if __name__ == "__main__":
    n,m,v = map(int,sys.stdin.readline().split())
    field = graph(n,m)
    dfs(field,n,v)
    bfs(field,n,v)

"""
BFS deque로 구현
라이브러리 안쓰고
def bfs(Node,n,v):
    result = []
    visited = [False] * (n+1)
    queue = [v]
    visited[v] = True
    front = 0
    # queue의 길이만큼 앞에꺼부터 빼기
    # 이렇게하면 시작 복잡도가 O(1)임
    while front < len(queue):
        cur = queue[front]
        front += 1
        result.append(cur)
        for i in Node[cur]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    for r in result:
        print(r,end=' ')
"""