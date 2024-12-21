def solution(number, k):
    stack = []  # 큰 숫자를 저장할 스택
    
    for num in number:
        # 스택의 마지막 숫자가 현재 숫자보다 작고, 제거할 숫자가 남아 있다면 제거
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)  # 현재 숫자를 스택에 추가
    
    # 아직 제거할 숫자가 남아 있다면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
    
    # 스택을 문자열로 변환하여 반환
    return ''.join(stack)

"""
예제 1: number="1924", k=2
초기: stack=[], k=2
'1' → 스택에 추가 → stack=['1']
'9' → '9' > '1', '1' 제거, k=1 → stack=['9']
'2' → 스택에 추가 → stack=['9', '2']
'4' → '4' > '2', '2' 제거, k=0 → stack=['9', '4']
결과: stack=['9', '4']
예제 2: number="1231234", k=3
초기: stack=[], k=3
'1' → 스택에 추가 → stack=['1']
'2' → '2' > '1', '1' 제거, k=2 → stack=['2']
'3' → '3' > '2', '2' 제거, k=1 → stack=['3']
'1' → 스택에 추가 → stack=['3', '1']
'2' → '2' > '1', '1' 제거, k=0 → stack=['3', '2']
'3' → 스택에 추가 → stack=['3', '2', '3']
'4' → 스택에 추가 → stack=['3', '2', '3', '4']
결과: stack=['3', '2', '3', '4']

"""
