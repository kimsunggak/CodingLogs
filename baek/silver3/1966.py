"""
문제
- N개의 문서에서 중요도가 M인 문서가 몇 번째로 인쇄되는지 찾는 문제

접근 방식
- N 만큼 문서의 개수 입력 받기
- 찾고자 하는 문서의 위치 M 입력 받기
- 값이 클수록 중요도가 높음
- 중요도 입력받기 (문서의 중요도는 1~9까지)
- 입력 받은 중요도에서 M번째 문서의 중요도가 몇번째로 출력되는지 찾기
    -> 중요도에 인덱스 번호 부여
    -> 중요도 내림차순으로 정렬
    -> 정렬된 중요도 리스트에서 인덱스가 M과 같을때까지 반복 
- 틀린이유 : 앞에 중요도가 높은 문서가 있으면 인쇄하고 정렬해야 함 -> 단순 중요도 기준 내림차순으로 정렬 후 인덱스 찾기로 풀어서 틀림
"""
test = int(input())
result = []
for _ in range(test):
    value = 1
    N,M = map(int, input().split())
    importance = list(map(int, input().split()))
    for idx,key in enumerate(importance):
        importance[idx] = (key, idx)
    while importance:
        current = importance[0]
        if current == max(importance,key = lambda x:x[0]):
            if current[1] == M:
                result.append(value)
                break
            else:
                value += 1
                importance.pop(0)
        else:
            importance.append(current)
            importance.pop(0)
for r in result:
    print(r)