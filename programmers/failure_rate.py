def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        a,b = 0,0
        for s in stages:
            if i <= s:
                b += 1 # 분모
            if i == s:
                a +=1 # 분자
        if b ==0 :
            answer.append(0)
        else:
            answer.append(a/b) # 실패율 추가
    answer = sorted(range(1,N+1),key=lambda i:(answer[i-1]),reverse=True)
    return answer

#실패율에 대한 스테이지 정렬하는 방법론
#1. 실패율을 계산한다.
#2. 실패율을 기준으로 정렬한다.
#3. 실패율이 같다면 스테이지 번호가 작은 것부터 정렬한다.