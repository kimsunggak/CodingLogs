"""
문제
- 정수 n이 주어졌을 때 1,2,3의 합으로 n을 만들 수 있는 경우의 수를 구하는 문제

접근 방식
- x+2y+3z = n , 3의 개수 z = 0 ~ n//3 , y의 개수 y = 0 ~ (n-3z)//2 , x의 개수 x = n - 2y - 3z
- z의 개수에 따라 y의 개수를 구하고, y의 개수에 따라 x의 개수를 구하는 방식으로 경우의 수를 구함
- x,y,z의 개수를 순열로 구하는 방법은 (x+y+z)! / (x! * y! * z!) 이므로, 이를 이용하여 경우의 수를 구함
"""
import sys
T =int(sys.stdin.readline().strip())
def factorical(x):
    factorial = 1
    while x > 1:
        factorial *= x
        x-= 1
    return factorial

def main():
    answer = []
    for _ in range(T):
        result = 0
        n = int(sys.stdin.readline().strip())
        for z in range(n//3+1): # z의 범위
            for y in range((n-3*z)//2+1):
                x = n - 2*y - 3*z
                result += (factorical(x+y+z) // (factorical(x) * factorical(y) * factorical(z)))
        answer.append(result)
    for a in answer:
        print(a)
if __name__ == "__main__":
    main()