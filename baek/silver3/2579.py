"""
문제
- 계단의 개수와 각 계단에 대한 점수가 주어짐
- 연속된 3개의 계단을 밟을 수 없고 , 마지막 계단은 반드시 밟아야 함
- 얻은 점수의 최대값을 구하는 프로그램을 작성

접근방식
- dp를 이용하여 점수를 구하는 문제
- dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
"""
import sys
n = int(sys.stdin.readline().strip())
stair = [int(sys.stdin.readline().strip()) for _ in range(n)]
def main():
    if n == 1:
        print(stair[0])
        return
    elif n == 2:
        print(stair[0] + stair[1])
        return
    max_score = [0] * (n+1)
    max_score[1] = stair[0]
    max_score[2] = stair[0] + stair[1]
    for i in range(3,n+1):
        max_score[i] = max(max_score[i-2]+stair[i-1],max_score[i-3]+stair[i-1]+stair[i-2])
    print(max_score[n])
if __name__ == "__main__":
    main()
