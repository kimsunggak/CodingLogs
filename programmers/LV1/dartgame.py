"""
문제
- 3번의 다트를 던져 얻은 점수 구하기
- 점수는 0~10 , 세가지 영역 존재 (싱글, 더블, 트리플) -> 제곱
- 옵션 존재 (스타상, 아차상) -> 2배, -1배 (효과 중첩 가능) , 점수마다 하나씩 존재

접근 방식
- 점수를 저장할 리스트 생성
- 문자열을 순회하며 각 문자에 대한 조건문 생성
- 숫자인 경우 -> 리스트에 추가
- S,D,T인 경우 -> 리스트의 마지막 원소에 대해 제곱
- *,#인 경우 -> 리스트의 마지막 원소에 대해 적용 (단, *인 경우 이전 원소도 적용)

문제점
- 점수가 10인 경우를 고려하지 않음
-> 0일때 이전 원소가 1인 경우 10으로 처리 -> 오류 발생 -> 조건문 추가
-> 빈 리스트 접근 오류 -> score가 True일때만 조건문 실행
"""
def solution(dartResult):
    answer = 0
    score = []
    for n in dartResult:
        if n.isdigit():
            if n == '0':
                if score and score[-1] == 1:
                    score[-1] = 10
                else:
                    score.append(0)
            else:
                score.append(int(n))
        elif n == 'S':
            score[-1] = score[-1]
        elif n == 'D':
            score[-1] = score[-1] ** 2
        elif n == 'T':
            score[-1] = score[-1] ** 3
        elif n == '*':
            score[-1] = score[-1] * 2
            if len(score)>1:
                score[-2] = score[-2] * 2
        elif n == '#':
            score[-1] = score[-1] * -1
    answer = sum(score)
    return answer
