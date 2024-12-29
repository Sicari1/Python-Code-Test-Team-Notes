def solution(people, limit):
    answer = 0
    people = sorted(people)
    print(people)
    while people:
        if len(people) == 1:
            people.pop()
            answer += 1
        elif people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop(-1)
            answer += 1
        else:
            people.pop(-1)
            answer +=1
    
    return answer 


채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (1.62ms, 10.1MB)
테스트 2 〉	통과 (1.15ms, 10.2MB)
테스트 3 〉	통과 (1.11ms, 10.1MB)
테스트 4 〉	통과 (1.04ms, 10MB)
테스트 5 〉	통과 (0.62ms, 9.96MB)
테스트 6 〉	통과 (0.35ms, 9.92MB)
테스트 7 〉	통과 (0.54ms, 10.1MB)
테스트 8 〉	통과 (0.06ms, 10.1MB)
테스트 9 〉	통과 (0.09ms, 10MB)
테스트 10 〉	통과 (1.05ms, 10.1MB)
테스트 11 〉	통과 (0.91ms, 10.2MB)
테스트 12 〉	통과 (0.82ms, 10.2MB)
테스트 13 〉	통과 (1.06ms, 10.1MB)
테스트 14 〉	통과 (1.34ms, 10.2MB)
테스트 15 〉	통과 (0.22ms, 10MB)
테스트 16 〉	통과 (0.04ms, 10.1MB)
테스트 17 〉	통과 (0.03ms, 9.95MB)
테스트 18 〉	통과 (0.03ms, 9.98MB)
테스트 19 〉	통과 (0.03ms, 10.1MB)
테스트 20 〉	통과 (0.03ms, 10.1MB)
테스트 21 〉	통과 (0.03ms, 10.1MB)
테스트 22 〉	통과 (0.03ms, 10.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	통과 (15.55ms, 11MB)
테스트 3 〉	통과 (31.40ms, 11MB)
테스트 4 〉	통과 (16.11ms, 11.2MB)
테스트 5 〉	통과 (14.21ms, 10.7MB)
채점 결과
정확성: 81.5
효율성: 14.8
합계: 96.3 / 100.0
