"""
문제
- N개의 동전으로 K를 만들기
- 개수가 최소가 되도록

해결 방법
- N개의 동전 가치 큰거부터 K에 나눔
- 몫이 0보다 크면 나눈 몫만큼 개수 추가
- K는 나머지 값으로 갱신
- K가 0이면 종료
"""
import sys
def main():
    n,k = map(int,sys.stdin.readline().strip().split())
    coin = [int(sys.stdin.readline().strip()) for _ in range(n)]
    coin.sort(reverse=True)
    answer = 0
    while k>0:
        for c in coin:
            if k // c > 0:
                answer += k // c
                k = k % c
            else:
                continue
    print(answer)
if __name__ == "__main__":
    main()