"""
문제
- 자연수 n이 주어질 때 최소 개수의 제곱수 합으로 표현하는 프로그램을 작성
- 제곱수들의 최소 개수를 구해야 함

접근 방식
- n보다 작은 수 중에 가장 큰 제곱수를 구함
- n에서 제곱수를 빼고 남은 수에 대해 재귀적으로 같은 작업을 반복함
- n이 0이 될 때까지 반복
- 이 과정이 항상 최소개수를 보장하는 것은 아님
- 예를 들어 12를 위 방법으로 하면 9+1+1+1 이지만 최소는 4+4+4임

-동적 계획법을 사용하여 제곱수의 합을 구해보아라
import sys
import math
def min_squares(n):
    dp = [0] * (n + 1)
    for i in range(1,n+1):
        cnt = i
        k = 1
        while k*k <= i:
            # 최솟값 찾아가기
            cnt = min(cnt,dp[i-k*k]+1)
            k += 1
        dp[i] = cnt
    print(dp[n])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    min_squares(n)

- DP했는데도 시간초과 남 - why? 지금 시간복잡도가 O(n*sqrt(n))임
- n 이 50000이면 50000*sqrt(50000) = 50000*224 = 11200000 이고 이건 략 0.5~1.2초 정도 걸림

-
"""
import sys
def min_squares(n):
    dp = [0] * (n + 1)
    for i in range(1,n+1):
        cnt = i
        k = 1
        while k*k <= i:
            # 최솟값 찾아가기
            cnt = min(cnt,dp[i-k*k]+1)
            k += 1
        dp[i] = cnt
    print(dp[n])

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    min_squares(n)