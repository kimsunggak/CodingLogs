"""
문제
- 피보나치 수열에서 0과 1이 각각 몇 번 출력되는지 구하여라

해결방법
- 동적 프로그래밍을 사용하여 피보나치 수열 구현

배운점
- 동적 계획법 (Dynamic Programming) : 큰 문제를 작은 문제로 나누고, 작은 문제들의 답을 미리 계산하여
저장해둔 뒤 필요할 때마다 재활용하여 풀이하는 방법
- 중복 계산을 피하여 효율적으로 계산
"""
import sys
def main():
    T = int(sys.stdin.readline().strip())
    memory = {}
    def f(n):
        if n == 0:
            return (1, 0)
        elif n == 1:
            return (0, 1)
        if n in memory:
            return memory[n]  
        zero_n1, one_n1 = f(n-1)
        zero_n2, one_n2 = f(n-2)
        memory[n] = (zero_n1 + zero_n2, one_n1 + one_n2)
        return memory[n]
    result = []
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        print(" ".join(map(str, f(n))))
if __name__ == "__main__":
    main()