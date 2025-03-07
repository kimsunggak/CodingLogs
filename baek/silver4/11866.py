"""
문제
- 요세푸스 문제
- N 명의 사람이 원을 이루면서 앉아 있고 K번째 사람을 제거
- 제거되는 순서 출력

해결방식
- 큐를 사용하여 해결
- 큐에서 K만큼 숫자를 빼서 K번째를 제외한 나머지를 다시 큐에 push
- 큐의 길이가 0이 될 때까지 반복
"""
N,K = list(map(int,input().split()))
queue = [i for i in range(1,N+1)]
result = []
while queue:
    for i in range(K-1):
        queue.append(queue.pop(0))
    result.append(queue.pop(0))
print("<",end="")
print(", ".join(map(str,result)),end="")
print(">")