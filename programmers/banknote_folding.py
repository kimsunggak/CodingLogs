"""
문제
- 주어진 크기에 들어갈 때까지 지폐를 반으로 접음
- 접는 횟수를 구해야 함

접근방식
- 지폐의 크기를 반으로 나누어 가며 지갑의 크기와 비교
- 지갑의 크기보다 작아질 때까지 반복
""" 
def solution(wallet, bill):
    answer = 0
    while max(wallet) < max(bill) or min(wallet) < min(bill):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
    return answer
