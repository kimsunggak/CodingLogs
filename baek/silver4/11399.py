"""
문제
- N명의 사람이 돈을 인출하는데 소요되는 시간의 합 최솟값을 구하여라

해결방법
- 각 사람이 돈을 인출하는데 걸리는 시간을 오름차순으로 정렬한다.
-
"""
import sys
def main():
    N = int(sys.stdin.readline().strip())
    minute = list(map(int,sys.stdin.readline().strip().split()))
    minute.sort()
    total = 0
    result = 0
    for m in minute:
        total +=m
        result += total
    print(result)
if __name__ == "__main__":
    main()