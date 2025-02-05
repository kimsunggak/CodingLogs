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