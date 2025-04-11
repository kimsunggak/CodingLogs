"""
문제
- 2xn크기의 직사각형을 1x2 타일과 2x1 타일로 채우는 방법의 수를 구하여라

접근방식
- n이 짝수일 때와 홀수일 때를 나눠서 생각해보자
- 2x1타일과 1x2 타일을 i개 n-i개로 나누고 i는 0부터 n까지의 범위로 한다
- 타일들의 개수가 각각 a개 b개 이면은 a블록은 2개씩 하나로 묶어야 한다 -> 왜냐하면 2Xn 직사각형에서 2x1 타일은 2개씩 움직이기 때문이다
- 따라서 나열하는 경우의 수를 수식으로 나타내면 ((n+i)/2)!) / (n-i)/2! * i! 이다

시간초과
import sys
def rectangle():
    n = int(sys.stdin.readline().strip())
    def factorial(n):
        v = 1
        if n == 0 or n == 1:
            return v
        for i in range(2, n+1):
            v *= i
        return v
    result = 0
    if n % 2 ==0:
        for i in range(0,n+1,2):
            result += factorial((n+i)//2) // (factorial((n-i)//2) * factorial(i))
    else:
        for i in range(1,n+1,2):
            result += factorial((n+i)//2) // (factorial((n-i)//2) * factorial(i))
    return result
if __name__ == "__main__":
    print(rectangle())

-> 점화식을 DP로 구현해서 풀어보자
dp[n] = dp[n-1] + dp[n-2]
"""
import sys
def tile():
    n = int(sys.stdin.readline())
    if n == 1:
        print(1)
        return # 함수 종료 안하면 memory[2] 선언 때문에 인덱싱 오류 발생함!
    memory = [0]*(n+1)
    memory[1] = 1
    memory[2] = 2
    for i in range(3,n+1):
        memory[i] = memory[i-1] + memory[i-2]
    print(memory[n]%10007)
if __name__ == "__main__":
    tile()