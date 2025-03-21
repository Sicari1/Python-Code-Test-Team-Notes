def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key=lambda x: len(x))
    # 3. 문자열 -> 리스트 of 리스트 of int
    s = [list(map(int, x.split(','))) for x in s]
    answer.append(s[0][0])    
    
    for i in range(0, len(s)-1):
        
        D = set(s[i+1]) - set(s[i])
        a = D.pop()
        answer.append(a)
        
    return answer
