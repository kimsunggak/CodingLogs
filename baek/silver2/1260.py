"""
문제
- 정점의 개수 N과 간선의 개수 M, 시작 정점 번호 V가 주어짐
- 간선이 연결하는 두 정점의 번호가 M개 주어짐
- DFS와 BFS를 수행한 결과를 프로그램으로 구현하라

접근 방법

"""
import sys
def graph():
    n,m,v = map(int,sys.stdin.readline().split())
    node = [[0]*(n+1) for _ in range(n+1)]
    node[0][v] = v
    for i in range(m):
        x,y = map(int,sys.stdin.readline().split())
        node[x][y] = y
    print(node)

if __name__ == "__main__":
    graph()
