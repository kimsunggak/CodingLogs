"""
문제
- 숫자 N개가 주어졌을 때 i번째 수부터 j번째 수까지의 합을 구하는 문제

접근방식
- N개의 수 입력받기
- 합을 구해야 하는 범위 i,j를 입력받기
- 인덱싱을 이용하여 합구하기
시간초과가 발생함
- 인덱스 슬라이싱 사용하면 시간초과 발생함
- 누적합을 구해놓으면 가져다 쓰면 됨
- 시간 복잡도 O(N) + O(M) = O(N+M)

잘못 알고 있었던거거
- map객체 작동 방식 이해 : map(함수, iterable) -> iterable의 각 요소에 함수를 적용하여 새로운 iterable을 반환
- 지시자의 역할임
- map객체는 list로 변ㄴ환하지 않으면 주소값이 출력됨
- 그러면 [map]이랑 list(map) 이랑 똑같은거 아니냐?
- map 객체 자체가 리스트의 단일 원소로 들어가기 때문에 list(map)로 변환해야 함
"""
import sys
def add():
    N,M = map(int,sys.stdin.readline().split())
    num = list(map(int,sys.stdin.readline().split()))
    pre_sum = [0] * (N+1)
    # 누적합을 구하자
    for i in range(1, N+1):
        pre_sum[i] = pre_sum[i-1] + num[i-1]
    result = []
    for _ in range(M):
        i,j = map(int,sys.stdin.readline().split())
        result.append(pre_sum[j] - pre_sum[i-1]) # 왜 i-1이냐 -> 숫자 배열이 1부터 시작하기 때문
    for r in result:
        print(r)
if __name__ == "__main__":
    add()