"""
문제
- 입력된 수열을 만들기 위해 어떤 순서로 push와 pop을 수행해야 하는지 구하는 프로그램 작성

해결 방법
- 스택의 마지막 값이 입력된 수열 값과 같은지 확인
- 같으면 pop , 없으면 같은 값이 나올 때까지 push
- push와 pop을 수행하는 순서를 출력
- push와 pop 조건을 둘 다 만족하지 못하면 NO 출력
"""
import sys
def main():
    n = int(sys.stdin.readline())
    result = []
    stack = []
    answer = []
    i = 1
    for _ in range(n):
        result.append(int(sys.stdin.readline().strip()))
    while result:
        if not stack:
            stack.append(i)
            answer.append("+")
            i += 1
        #남아 있으면
        else:
            if stack[-1] == result[0]:
                stack.pop()
                result.pop(0)
                answer.append("-")
            else:
                if i > n:
                    break
                else:
                    stack.append(i)
                    answer.append("+")
                    i += 1
    if result :
        print("NO")
    else:
        for i in answer:
            print(i)

if __name__ == "__main__":
    main()
        