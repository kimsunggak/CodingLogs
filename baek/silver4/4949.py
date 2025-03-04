"""
문제
- 괄호들의 짝이 맞는지 확인하는 프로그램을 작성하시오.
- 괄호는 소괄호 ( ) 와 대괄호 [ ] 두 종류 

접근 방식
- 문자열 순회하며 괄호를 찾아 리스트에 저장
- 괄호가 짝이 맞는지 확인 , 짝이 맞으면 pop
- 모든 괄호를 확인했을 때 리스트가 비어있으면 yes, 아니면 no

피드백
결과 초기화 위치 주의 -> check 리스트가 잘못 초기화 되어서 틀림
"""
sen_list = []
parentheses = ['(', ')', '[', ']']
while True:
    sen = input()
    if sen == '.':
        break
    sen_list.append(sen)
for s in sen_list:
    check = []
    for i in s:
        if i in parentheses:
            check.append(i)
        if len(check) >= 2:
            if check[-1] == ')' and check[-2] == '(':
                check.pop()
                check.pop()
            elif check[-1] == ']' and check[-2] == '[':
                check.pop()
                check.pop()
    if len(check) == 0:
        print('yes')
    else:
        print('no')