"""
접근 방식
- 각 사람의 덩치 등수 계산
- 한 사람의 등수는 자신보다 몸무게와 키 모두 큰 사람 수에 1 더한 값
"""
import sys
def main():
    N = int(sys.stdin.readline().strip())
    people = []
    answer = []
    for _ in range(N):
        people.append(list(map(int,sys.stdin.readline().strip().split())))
    for i in range(N):
        k = 0
        for j in range(N):
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                k+=1
        answer.append(k)
    print(' '.join(str(x+1) for x in answer))    
if __name__ == "__main__":
    main()