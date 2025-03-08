"""
문제
- 모든 사람의 난이도 의견의 30% 절사평균으로 문제 난이도 결정
- n개의 난이도 의견이 주어짐
- 모든 난이도는 1 이상 30이하

접근방식
- n개의 난이도를 정렬
- n*0.3 /2 만큼의 사람 수 제거 (소수점 반올림)
- 나머지 의견 난이도 평균 계산
- round함수 사용해서 오류 발생 -> round(0.5) = 0
- 새로운 반올림 함수 선언
"""
import sys
def rounding(x):
    return int(x+0.5)
def main():
    levels = []
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        levels.append(int(sys.stdin.readline().strip()))
    levels.sort()
    k = rounding(n * 0.3 / 2)
    levels = levels[k:n-k]
    if levels:
        print(rounding(sum(levels) / len(levels)))
    else:
        print(0)
    
if __name__ == "__main__":
    main()