"""
문제
- 정수 개수N과 N개의 정수가 주어짐
- N개의 정수 중에 M개의 정수가 존재하는지 확인하기

접근 방법
- N개의 정수 리스트 생성 정렬 (존재하는지만 확인하면 되기 때문에) -> 빠르게 찾기 위해
- M개의 정수 리스트 생성
- N 리스트 안에 M 리스트의 원소가 있으면 1 출력, 없으면 0 출력

해결 방안
- 집합은 내부적으로 해시 테이블을 사용하기 때문에 시간복잡도가 O(1)이다.
- 따라서 집합으로 변경하여 시간복잡도를 줄인다.
"""
"""
시간초과 발생
import sys
def main():
    N = int(sys.stdin.readline())
    N_list = list(map(int,sys.stdin.readline().split()))
    N_list.sort()
    M = int(sys.stdin.readline())
    M_list = list(map(int,sys.stdin.readline().split()))
    for i in M_list:
        if i in N_list: #선형 탐색이라 시간초과 발생
            print(1)
        else:
            print(0)
if __name__ == "__main__":
    main()
"""
import sys
def main():
    N = int(sys.stdin.readline())
    N_list = set(map(int,sys.stdin.readline().split())) # 집합으로 변경하여 시간복잡도 줄이기
    M = int(sys.stdin.readline())
    M_list = list(map(int,sys.stdin.readline().split()))
    for i in M_list:
        if i in N_list: 
            print(1)
        else:
            print(0)
if __name__ == "__main__":
    main()