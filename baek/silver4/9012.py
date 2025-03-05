"""
문제
- 이전 문제와 유사 괄호가 짝지어졌는지 확인하는 문제
- 괄호의 종류는 '(', ')' 두가지

접근 방식
- 스택을 활용하여 해결
- '('가 나오면 스택에 추가, ')'가 나오면 스택에서 '(' pop
- 스택이 비어있으면 YES, 아니면 NO
"""
n = int(input())
ps = []
result = []
for _ in range(n):
    ps.append(input())
for a in ps:
    check = []
    for g in a:
        if check and g == ')':
            if check[-1] == '(':
                check.pop()
        else:
            check.append(g)
    if not check:
        result.append("YES")
    else:
        result.append("NO")
for r in result:
    print(r) 