"""
문제
- 큐를 구현
- 6가지의 명령을 처리하는 프로그램 작성


"""
import sys
def queue():
    n = int(sys.stdin.readline().strip())
    queue = []
    result = []
    for _ in range(n):
        command = sys.stdin.readline().split()
        if command[0] =="push":
            queue.append(command[1])
        elif command[0] == "pop":
            if not queue:
                result.append(-1)
            else:
                result.append(queue[0])
                queue = queue[1:]
        elif command[0] == "size":
            result.append(len(queue))
        elif command[0] == "empty":
            if queue:
                result.append(0)
            else:
                result.append(1)
        elif command[0] =="front":
            if not queue:
                result.append(-1)
            else:
                result.append(queue[0])
        elif command[0] == "back":
            if not queue:
                result.append(-1)
            else:
                result.append(queue[-1])
    for i in result:
        print(i)
if __name__ == "__main__":
    queue()