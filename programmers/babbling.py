"""
문제 이해
- 주어진 단어 목록을 이용해 발음할 수 있는 단어인지 확인해야 함
- 같은 단어가 연속해서 나오면 안됨

해결 전략
- 주어진 단어 목록에서 발음할 수 있는 단어를 찾아 공백으로 치환
- 공백만으로 이루어진단어는 발음 가능한 단어로 판단
- *공백제거하고 길이 계산해야함 - strip사용!
"""
def solution(babbling):
    answer = 0
    words = ["aya","ye","woo","ma"] 
    for word in babbling:
        for w in words:
            if w*2 in word: # 연속된 단어가 있으면 안됨
                continue
            word = word.replace(w," ") # 조합한 발음중에 말 할 수 있는 발음을 공백처리
        if len(word.strip()) == 0:
            answer+=1
    return answer