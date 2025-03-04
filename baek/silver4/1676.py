"""
접근 방법
1. N! 구하기
2. N!을 문자열로 바꾼 후 뒤집어서 0의 개수 세기
3. 0이 아닌 수가 나올 때까지 0의 개수 세기
"""

import sys
def main():
    N = int(sys.stdin.readline().strip())
    p = 1
    c = 0
    for i in range(1,N+1):
        p *=i
    p = list(str(p))[::-1]
    for i in p:    
        if i == '0':
            c +=1
        else:
            break
    print(c)
if __name__ == "__main__":
    main()