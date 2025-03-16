"""
문제 
- 포켓몬 도감에서 이름은 번호로 번호는 이름으로 맞추는 문제

시간초과 발생
input 이랑 sys.stdin.readline() 차이점
- input()은 입력을 받을 때마다 버퍼를 비우기 때문에 느리다.
- sys.stdin.readline()은 한 번에 버퍼를 비우기 때문에 빠르다.
- 버퍼는 데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 데이터를 보관하는 메모리 영역을 의미
- index함수로 찾는 방법 시간복잡도 O(n) -> 딕셔너리로 찾는 방법 시간복잡도 O(1)
- 이름 : 번호 딕셔너리 , 번호 : 이름 딕셔너리 생성
"""
import sys
def main():
    poketmon_name = {}
    poketmon_number = {}
    answer = []
    n,m = map(int, sys.stdin.readline().strip().split())
    for i in range(n):
        poketmon = sys.stdin.readline().strip()
        poketmon_name[i+1] = poketmon
        poketmon_number[poketmon] = i+1
    Q = [sys.stdin.readline().strip() for _ in range(m)]
    for q in Q:
        if q.isdigit():
            answer.append(poketmon_name[int(q)])
        else:
            answer.append(str(poketmon_number[q]))
    for a in answer:
        print(a)
if __name__ == "__main__":
    main()