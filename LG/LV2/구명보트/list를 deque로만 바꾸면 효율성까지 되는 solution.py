def solution(people, limit):
    answer = 0
    from collections import deque 
    people = sorted(people)
    people = deque(people)
    while people:
        if len(people) == 1:
            people.pop()
            answer += 1
        elif people[0] + people[-1] <= limit:
            people.popleft()
            people.pop() 
            answer += 1
        else:
            people.pop()
            answer += 1     
    
    return answer 




채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (1.14ms, 10.3MB)
테스트 2 〉	통과 (0.96ms, 10.3MB)
테스트 3 〉	통과 (0.87ms, 10.2MB)
테스트 4 〉	통과 (0.72ms, 10.1MB)
테스트 5 〉	통과 (0.48ms, 10.4MB)
테스트 6 〉	통과 (0.27ms, 10.2MB)
테스트 7 〉	통과 (0.73ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.1MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.77ms, 10.1MB)
테스트 11 〉	통과 (0.64ms, 10.2MB)
테스트 12 〉	통과 (0.60ms, 10.2MB)
테스트 13 〉	통과 (0.80ms, 10.3MB)
테스트 14 〉	통과 (1.08ms, 10.2MB)
테스트 15 〉	통과 (0.12ms, 10.1MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (0.04ms, 10.1MB)
테스트 20 〉	통과 (0.03ms, 10.2MB)
테스트 21 〉	통과 (0.03ms, 10.1MB)
테스트 22 〉	통과 (0.03ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (10.76ms, 11.1MB)
테스트 2 〉	통과 (12.89ms, 11.1MB)
테스트 3 〉	통과 (10.67ms, 11.1MB)
테스트 4 〉	통과 (12.82ms, 11.1MB)
테스트 5 〉	통과 (11.14ms, 10.9MB)
채점 결과
정확성: 81.5
효율성: 18.5
합계: 100.0 / 100.0
