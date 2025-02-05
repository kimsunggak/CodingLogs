"""
문제: 백준 1181 - 단어 정렬
접근 방식: 중복 제거 후, 문자열 길이와 사전 순으로 정렬
사용 알고리즘: Python 내장 정렬 (Timsort), key에 람다 함수 사용
시간 복잡도: O(n log n)
개선 사항: 기존의 선택 정렬보다 효율적인 내장 함수 사용
### 배운 점
- 내장 함수를 사용하면 코드도 간결해지고 성능도 향상됨
- 람다 함수를 활용하여 정렬 기준을 명확하게 지정할 수 있음

"""
# 시간초과 
"""import sys
def main():
    N = int(sys.stdin.readline().strip())
    word = []
    for _ in range(N):
        word.append(sys.stdin.readline().strip())
    word = list(set(word)) # 중복 제거
    l = len(word)
    #선택 정렬 사용
    for i in range(l-1):
        min_s = word[i]
        for j in range(i+1,l):
            if len(min_s) > len(word[j]):
                min_s = word[j]
                word[i], word[j] = word[j], word[i]
    #사전 순 정렬
    for i in range(l-1):
        for j in range(i+1, l):
            if (len(word[i]) == len(word[j]) and word[i] > word[j]):
                word[i], word[j] = word[j], word[i]
    for a in word:
        print(a)
if __name__ == "__main__":
    main()"""
# 시간초과 해결
import sys
def main():
    N = int(sys.stdin.readline().strip())
    word = []
    for _ in range(N):
        word.append(sys.stdin.readline().strip())
    word = list(set(word)) # 중복 제거
    words = sorted(word, key = lambda x : (len(x),x)) # sort함수와 람다함수 이용
    for w in words:
        print(w)
if __name__ == "__main__":
    main()
