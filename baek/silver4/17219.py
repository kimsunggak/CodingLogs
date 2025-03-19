"""
문제
-N개의 사이트 주소와 찾으려는 M개의 사이트 주소가 주어졌을 때,
M개 사이트 각각의 비밀번호를 구하는 프로그램을 작성하라

해결방법
- 딕셔너리로 사이트 주소와 비밀번호를 저장
"""
import sys
def main():
    N,M = map(int,sys.stdin.readline().strip().split())
    site = {}
    result = []
    for _ in range(N):
        site_name,site_pw = sys.stdin.readline().strip().split()
        site[site_name] = site_pw
    for _ in range(M):
        pw = sys.stdin.readline().strip()
        result.append(site[pw])
    for r in result:
        print(r)
if __name__ == "__main__":
    main()