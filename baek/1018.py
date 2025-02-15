"""
문제 
- N X M 크기의 보드가 주어짐
- 보드는 검은색과 흰색으로 칠해져있음
- 체스판은 8X8 크기 - 보드에서 잘라낸 조각
- 체스판으로 잘라낸 후 다시 칠해야 하는 정사각형의 최소 개수 구하기

접근 방식
- 8 x 8 크기의 체스판 (한 패턴은 맨 왼쪽 위 칸이 흰색(W)이고, 다른 하나는 검은색(B))
- 보드에서 8 x 8 크기의 체스판을 잘라내어서 체스판을 만들어야 함
- 각 8×8 조각과 체스판 패턴 비교
 -> 각 칸의 좌표 (x, y)를 생각했을 때, (x+y)가 짝수인 칸은 맨 왼쪽 위 칸과 같은 색이어야 하고, 
 (x+y)가 홀수인 칸은 반대 색이어야 함
- 최소 수정 횟수 찾기
"""
import sys
def main():
    N,M = map(int,sys.stdin.readline().strip().split())
    board = []
    result = float('inf')
    for _ in range(N):
        board.append(sys.stdin.readline().strip())
    for i in range(N-7):
        for j in range(M-7):
            c1,c2 = 0,0 # 첫번째 칸이 W인 경우, B인 경우
            for x in range(8):
                for y in range(8):
                    current_color = board[i+x][j+y]
                    #체스판은 색이 번갈아 나타나므로 (x+y)%2 == 0인 경우와 아닌 경우로 나누어서 계산
                    if (x+y)%2 == 0:
                        if current_color != 'W':
                            c1 += 1
                        if current_color != 'B':
                            c2 += 1
                    else:
                        if current_color != 'B':
                            c1 += 1
                        if current_color != 'W':
                            c2 += 1
            result = min(result, c1, c2)
    print(result)
if __name__ == "__main__":
    main()