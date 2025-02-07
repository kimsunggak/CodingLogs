"""
접근 방식 : N만큼 반복하면서 6의 개수만큼 앞자리 뒷자리 더해 나가기
-> 6이 들어간 수를 만나면 6의 개수만큼 뒷자리에 0~9까지 붙여서 더해주기
->자리수 문제 해결 못함 

문제의 본질은 666이 포함된 숫자 중 N번째를 찾는 것
-> 해결 방법론 : 666부터 1씩 증가시키면서 666이 포함된 숫자인지 확인

"""

import sys
def main():
    N = int(sys.stdin.readline().strip())
    num = 666
    c = 0
    while True:
        if '666' in str(num):
            c +=1
            if c == N:
                print(num)
                break
        num +=1
if __name__ == "__main__":
    main()