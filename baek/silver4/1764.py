"""
문제
- N명단과 M명단에 모두 포함되는 사람의 수와 이름을 출력하는 프로그램을 작성

해결방법
- N명단 순회하며 M명단에 있는지 확인
- M명단에 있는 경우, 결과 리스트에 추가
-> 교집합으로 푸는 방법도 있음
"""
import sys
def main():
    n,m = map(int,sys.stdin.readline().strip().split())
    n_list = [sys.stdin.readline().strip() for _ in range(n)]
    m_list = {sys.stdin.readline().strip() for _ in range(m)}
    result = []
    i= 0
    for s in n_list:
        if s in m_list:
            result.append(s)
            i+=1
    print(i)
    result.sort()
    for s in result:
        print(s)
if __name__ == "__main__":
    main()