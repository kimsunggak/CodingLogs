"""
문제
- 스택을 구현하여라
- 입력으로 주어지는 명령은 5가지 push,pop,size,empty,top이다.

접근방식
- stack 을 함수로 구현 
"""
import sys
def stack():
    n = int(sys.stdin.readline().strip())
    stack = []
    command = []
    for _ in range(n):
        #명령어 입력
        command.append(sys.stdin.readline().strip().split())
    for c in command:
        if c[0] =="push":
            stack.append(c[1])
        elif c[0] =="pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
                stack.pop()
        elif c[0] =="size":
            print(len(stack))
        elif c[0] =="empty":
            if len(stack) ==0:
                print(1)
            else:
                print(0)
        elif c[0] =="top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
if __name__ == "__main__":
    stack()
                