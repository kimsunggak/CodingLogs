"""
문제
- 주어진 정수 N을 3과 5의 합으로 나타내되, 사용한 항의 개수가 최소가 되도록 하여라.
- 방법이 없다면 -1을 출력

접근 방식
- 5로 나누어 가며 3으로 나누어 떨어지는 수를 찾는다. 
- 예외처리 하지 않아서 오류 발생 -> 3으로만 나누어 떨어지는 경우 추가
"""
import sys
def main():
    result = []
    n = int(sys.stdin.readline().strip())
    s = (n // 5 + 1)
    if n % 3 == 0:
            result.append(n // 3)
    if n % 5 == 0:
            result.append(n // 5)
    for i in range(1,s):
        if (n - 5 * i) % 3 == 0:
            result.append(i + (n - 5 * i) // 3)
    if not result:
        print(-1)   
    else:
        print(min(result))
if __name__ == "__main__":
    main()