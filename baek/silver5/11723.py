"""
문제
- 비어있는 공집합 S가 주어짐
- add : S에  X를 추가 - S에 이미x가 있는 경우에는 연산 무시
- remove : S에서 x를 제거 -S에 x가 없는 경우에는 연산 무시
- check : S에 x가 있으면 1을 없으면 0을 출력
- toggle : S에 x가 있으면 x를 제거, 없으면 x를 추가
- all : S를 {1~20} 으로 바꿈
- empty : S를 공집합으로 바꿈

배운점
- |=(합집합 연산자)
- 메모리 초과 발생 -> readline() 으로 모든 명령어를 메모리에 저장했기 때문
- 숫자형은 웬만하면 int로 변환해주는 것이 좋다

해결방법
- 명령어를 입력받을 때마다 처리하도록 수정
"""
import sys
def main():
    m = int(sys.stdin.readline())
    s = set()
    for _ in range(m):
        command = sys.stdin.readline().strip().split()
        if command[0] == "add":
            if int(command[1]) not in s:
                s |= {int(command[1])}
            else:
                continue
        elif command[0] == "remove":
            if int(command[1]) in s:
                s -= {int(command[1])}
            else:
                continue
        elif command[0] == "check":
            if int(command[1]) in s:
                print(1)
            else:
                print(0)
        elif command[0] == "toggle":
            if int(command[1]) in s:
                s -= {int(command[1])}
            else:
                s |= {int(command[1])}
        elif command[0] == "all":
            s = set([i for i in range(1,21)])
        elif command[0] == "empty":
            s = set()
if __name__ == "__main__":
    main()