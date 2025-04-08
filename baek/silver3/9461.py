"""
문제 
- 나선형으로 커지는 삼각형의 변의 길이를 구하는 문제
- n이 주어지면 n번째 변의 길이를 구하는 문제
- n은 1부터 100까지의 자연수

접근 방법
- n>=5 부터 규칙적인 패턴이 보인다.
- 점화식 dp[n] = dp[n-1] + dp[n-5]
- DP를 이용하여 n번째 변의 길이를 구한다.

시간 초과 문제
- DP가 아니라 재귀함수로 구현해서 시간 초과가 발생함
- 메모이제이션을 사용하여 중복계산 방지
"""
import sys
T = int(sys.stdin.readline().strip())
memory = {}
def dp(n):
    if n in memory:
        return memory[n]
    else:
        if n <=3 :
            memory[n] = 1
            return memory[n]
        elif n == 4:
            memory[n] = 2
            return memory[n]
        elif n == 5:
            memory[n] = 2
            return memory[n]
        elif n >=6:
            memory[n] = dp(n-1) + dp(n-5)
            return memory[n]

if __name__ == "__main__":
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        print(dp(n))

"""
# 간결하게 코드 작성법
import sys
def main():
    T = int(sys.stdin.readline().strip())
    def dp(n):
        memory = [0,1,1,1,2,2] + [0] * 95 # dp[0]~dp[5]까지 초기화
        for i in range(6,n+1):
            memory[i] = memory[i-1] + memory[i-5]
            return memory[n]
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        print(dp(n))
if __name__ == "__main__":
    main()

"""