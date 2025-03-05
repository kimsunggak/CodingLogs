"""
문제
- 정수가 1개씩 주어지는데 정수가 0이면 가장 최근의 쓴 수를 지우고 아니면 해당 수를 쓴다
- 쓴 수들의 합을 구하라

접근 방식
- 스택을 활용하여 해결
"""
import sys
K = int(sys.stdin.readline().strip())
check = []
for _ in range(K):
    n = int(sys.stdin.readline().strip())
    if check and n == 0:
        check.pop()
    else:
        check.append(n)
print(sum(check))
    