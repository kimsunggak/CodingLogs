"""
문제
- N장의 카드를 위에서 아래로 순서대로 놓음
- 제일 위에 있는 카드를 버림
- 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
- 마지막에 남게 되는 카드 출력

해결 방안
- 큐를 이용하여 해결 -> 시간초과
"""
"""
시간초과
import sys
def main():
    N = int(sys.stdin.readline())
    num = [n+1 for n in range(N)]
    while len(num) > 1:
        num.pop(0) # O(n)이므로 시간초과
        num.append(num.pop(0))
    print(num[0])
if __name__ == "__main__":
    main()
    """
import sys
from collections import deque
def main():
    N = int(sys.stdin.readline())
    num = deque(n+1 for n in range(N))
    while len(num) > 1:
        # popleft()는 O(1)이므로 시간 단축
        num.popleft()
        num.append(num.popleft())
    print(num[0])
if __name__ == "__main__":
    main()