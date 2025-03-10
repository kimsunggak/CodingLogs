"""
문제
- N개의 수가 주어질 때, 산술평균, 중앙값, 최빈값, 범위를 구하는 프로그램을 작성하여라

해결 방법
- 산술평균 : N개의 수들의 합을 N으로 나눈 값
- 중앙값 : N개의 수들을 증가하는 순서로 나열했을 때 그 중앙에 위치하는 값
- 최빈값 : N개의 수들 중 가장 많이 나타나는 값
- 범위 : N개의 수들 중 최댓값과 최솟값의 차이
"""
import sys
def main():
    N = int(sys.stdin.readline())
    num_list = []
    result = [] 
    for _ in range(N):
        num_list.append(int(sys.stdin.readline()))
    # 산술평균
    if sum(num_list)/N >= 0 :
        result.append(int(sum(num_list)/N + 0.5))
    else:
        result.append(int(sum(num_list)/N - 0.5))
    # 중앙값
    num_list.sort()
    result.append(num_list[(N-1)//2])
    # 최빈값
    # 해시 테이블 사용
    if len(num_list) == 1:
        result.append(num_list[0])
    else:
        num_dict = {}
        for n in num_list:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1
        max_num = max(num_dict.values())
        max_list = []
        for key, value in num_dict.items():
            if value == max_num:
                max_list.append(key)
        if len(max_list) == 1:
            result.append(max_list[0])
        else:
            result.append(max_list[1])
    # 범위
    if len(num_list) == 1:
        result.append(0)
    else:
        result.append(num_list[-1]-num_list[0])
    for r in result:
        print(r)
if __name__ == "__main__":
    main()
    