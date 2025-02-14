"""
문제
- 나이순으로 정렬하기
- 나이가 같으면 먼저 가입한 순으로 정렬하기

해결방법
- 나이를 정렬 기준으로 사용 -> 리스트에 저장된 튜플의 첫번째 인덱스를 기준으로 정렬
"""
import sys
def main():
    N = int(sys.stdin.readline().strip())
    people = []
    for _ in range(N):
        age,name = map(str,sys.stdin.readline().strip().split())
        people.append((age,name))
    people.sort(key = lambda x : int(x[0]))
    for i in people:
        print(i[0],i[1])
if __name__ == "__main__":
    main()
