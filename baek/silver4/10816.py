"""
문제
- M 개의 정수가 주어짐
- 상근이는 N 개의 정수 숫자카드를 가지고 있음
- N 개의 숫자 카드 중 주어진 M개의 정수가 몇 개 있는지 구해야 함

접근방식
- 하나씩 접근 즉 for문을 두개 사용하면 시간 복잡도 O(N^2)이므로 시간 초과
- 해시 테이블을 사용하여 O(N)으로 해결
"""
import sys
n = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int,sys.stdin.readline().strip().split()))
result = []
hash_table = {}
for i in a:
    if i in hash_table:
        hash_table[i] += 1
    else:
        hash_table[i] = 1
for j in b:
    if j in hash_table:
        result.append(hash_table[j])
    else:
        result.append(0)
print(' '.join(map(str,result)))