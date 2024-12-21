def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    reserve = sorted(reserve)
    save = 0
    used = [0]* (n+1)
    for i in lost:
        if i == 1:
            if i in reserve and used[i] == 0:
                used[i] = 1
                save += 1
                continue

            elif i + 1 in reserve and used[i+1] == 0:
                used[i+1] = 1
                save += 1 
                continue

        elif 1<i<n:
            if i in reserve and used[i] == 0:
                used[i] = 1
                save +=1
                continue
            elif i-1 in reserve and used[i-1] == 0:
                used[i-1] = 1
                save +=1
                continue
            elif i+1 in reserve and used[i+1] == 0:
                used[i+1] = 1
                save +=1
                continue

        elif i == n:
            if i in reserve and used[i] == 0:
                used[i] = 1
                save +=1
                continue
            elif i-1 in reserve and used[i-1] == 0:
                used[i-1] = 1
                save +=1      
                continue

    answer = n - len(lost) + save
    
    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	실패 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	실패 (0.01ms, 10.4MB)
테스트 13 〉	통과 (0.01ms, 10.5MB)
테스트 14 〉	통과 (0.01ms, 10.5MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.4MB)
테스트 18 〉	통과 (0.01ms, 10.4MB)
테스트 19 〉	통과 (0.01ms, 10.5MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
테스트 21 〉	통과 (0.00ms, 10.3MB)
테스트 22 〉	통과 (0.00ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.4MB)
테스트 24 〉	통과 (0.01ms, 10.3MB)
테스트 25 〉	통과 (0.01ms, 10.3MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.5MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
테스트 29 〉	통과 (0.01ms, 10.4MB)
테스트 30 〉	통과 (0.01ms, 10.3MB)
채점 결과
정확성: 93.3
합계: 93.3 / 100.0

"""
