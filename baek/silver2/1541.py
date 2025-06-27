"""
문제
입력 받은 수식의 최소값을 구하는 괄호의 위치를 찾는 문제

접근 방식
- 입력된 수식을 '-' 기준으로 분리한다 
- '-'가 어느 위치에 있든지 그 뒤에 오는 모든 '+'를 빼는 것이 최소값을 만드는 방법이다
- 그래서 분리후 계산한 값들을 빼면 최소값이 된다
- '-'가 없는 경우는 그냥 '+'를 모두 더하면 된다
"""
import sys

def calculate(expression):
    split_expression = expression.split('-')
    result = []
    for n in split_expression:
        result.append(sum(map(int, n.split('+'))))
    return result[0] - sum(result[1:])
if __name__ == "__main__":
    expression = sys.stdin.readline().strip()
    print(calculate(expression))