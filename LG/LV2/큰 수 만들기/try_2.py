def solution(number, k):
    answer = []
    n = k
    length = len(number) - k
    while len(answer) != length:
        headn = number[:n+1]        
        maxn = max(headn)
        index = headn.find(maxn)
        answer.append(maxn)
        number = number[index+1:]
        n = n - index
        
    answer2= ''
    for i in answer:
        answer2 += i
    return answer2


# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 9.99MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.38ms, 10.1MB)
# 테스트 5 〉	통과 (0.61ms, 10.1MB)
# 테스트 6 〉	통과 (117.25ms, 10.2MB)
# 테스트 7 〉	통과 (327.11ms, 10.4MB)
# 테스트 8 〉	통과 (3093.87ms, 10.5MB)
# 테스트 9 〉	통과 (1308.66ms, 12.7MB)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	통과 (0.01ms, 10MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 채점 결과
# 정확성: 91.7
# 합계: 91.7 / 100.0
