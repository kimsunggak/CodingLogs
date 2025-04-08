"""
문제
- 다양한 옷과 그 옷의 종류가 주어질 때, 서로 다른 옷을 입는 경우의 수를 구하는 문제
- 같은 종류의 옷은 하나만 입을 수 있음

접근방식
- 같은 종류의 옷끼리 묶기
- 안입는 경우 1가지 추가
- 각 종류의 옷 입는 경우의 수 곱하고 1을 빼기
"""
import sys
T = int(sys.stdin.readline().strip())
def main():
    answer = []
    for _ in range(T):
        result = 1
        clothes = {}
        n = int(sys.stdin.readline().strip())
        for _ in range(n):
            x,y = sys.stdin.readline().strip().split()
            # 같은 종류의 옷끼리 묶기
            if y in clothes:
                clothes[y].append(x)
            else:
                clothes[y] = [x]
        for k,v in clothes.items():
            result *= (len(v)+1)
        answer.append(result-1)
    for a in answer:
        print(a)
if __name__ == "__main__":
    main()