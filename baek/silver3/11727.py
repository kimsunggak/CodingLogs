"""
문제
- 타일 문제 2
- 이번에는 2xn 직사각형을 2x1,1x2,2x2 3개의 타일로 채우는 방법의 수를 구하는 프로그램

접근 방식
- DP(동적 계획법) 사용
- 이전 문제와 동일하게 일정한 패턴을 찾음
- 점화식 f(n) = f(n-1) + 2f(n-2)
"""
import sys
def f():
    n = int(sys.stdin.readline().strip())
    if n == 1:
        return 1
    elif n == 2:
        return 3
    memory = [0] * (n+1)
    memory[1] = 1
    memory[2] = 3
    for i in range(3,n+1):
        memory[i] = memory[i-1] + 2 * memory[i-2]
    return memory[n] % 10007
if __name__ == "__main__":
    print(f())