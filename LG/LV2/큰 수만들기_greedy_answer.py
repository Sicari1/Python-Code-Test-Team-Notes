def solution(number, k):
    answer = ""
    start = 0  # 탐색 시작 위치
    n = len(number)
    
    for _ in range(len(number) - k):
        # k+start까지 범위 내에서 가장 큰 값 선택
        max_digit = max(number[start:start + k + 1])
        # 가장 큰 숫자의 인덱스 찾기
        max_index = number.index(max_digit, start, start + k + 1)
        # 선택한 숫자 이후부터 탐색 시작
        start = max_index + 1
        # 결과에 숫자 추가
        answer += max_digit
        # 제거할 숫자 개수 감소
        k -= (max_index - start + 1) + (len(answer)-k)
        
    return answer




"""
Greedy 접근 방식
앞에서부터 확인:

k개의 숫자를 제거해야 하므로, 앞에서부터 k개의 범위 안에서 가장 큰 숫자를 선택합니다.
선택한 숫자 앞의 숫자는 모두 제거합니다.
반복 진행:

남은 숫자에서 같은 과정을 반복합니다.
숫자를 선택할 때 남은 범위를 고려하여 끝까지 숫자를 골라야 합니다.
"""
