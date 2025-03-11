"""
문제  *힌트 사용
- K개의 선 길이가 주어짐
- K개의 선을 동일한 길이로 나누어 N개의 선을 만들려고 함
- 이때 동일한 길이의 최대값을 구하여라

접근 방식:
1. 이진 탐색을 활용하여 가능한 최대 길이 찾기
   → 처음에 이진 탐색을 떠올리지 못함
    → 이진 탐색을 활용하여 최대 길이를 찾는 것이 핵심

2. 탐색 범위:
   - 최소 길이: 1 (0으로는 자를 수 없음)
   - 최대 길이: 가장 긴 랜선의 길이

3. 이진 탐색 과정:
   - 중간값(mid)으로 모든 랜선을 잘랐을 때 몇 개의 랜선이 나오는지 계산
   - N개 이상 나오면 → 더 긴 길이 시도 (left = mid + 1)
   - N개 미만 나오면 → 더 짧은 길이 시도 (right = mid - 1)

4. 언제 최대값에 도달?
   - left > right가 되는 시점에 right가 조건을 만족하는 최대 길이
"""
import sys
def main():
    K, N = map(int,sys.stdin.readline().split())
    lines = [int(sys.stdin.readline()) for _ in range(K)]
    left = 1
    right = max(lines)
    while left <= right:
        result = 0
        mid = (left + right) // 2
        for l in lines:
            result += l // mid
        if result < N:
            right = mid -1
        else:
            left = mid + 1
    return right

if __name__ == "__main__":
    print(main())