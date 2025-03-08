"""
문제
- M이상 N이하의 소수를 모두 출력하는 프로그램을 작성

해결 방법
- 에라토스테네스의 체를 활용
"""
"""
시간초과
import sys
M,N = map(int,sys.stdin.readline().strip().split())
num_list = []
for a in range(M,N+1):
    if a == 1:
        continue
    else:
        num_list.append(a)
for i in range(2,int(N**0.5)+1):
    check = []
    for n in num_list:
        if n % i == 0 and n != i:
            continue
        else:
            check.append(n)
            num_list = check
for n in num_list:
    print(n)
"""
import sys
M,N = map(int,sys.stdin.readline().strip().split())
num_list = [True] * (N+1)
num_list[0] = num_list[1] = False
for i in range(2,int(N**0.5)+1):
    if num_list[i]:
        for j in range(2*i,N+1,i):
            num_list[j] = False
for n in range(M,N+1):
    if num_list[n]:
        print(n)   