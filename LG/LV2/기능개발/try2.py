def solution(progresses, speeds):
    answer = []
    import math
    days = []
    for p, s in zip(progresses, speeds):
        num = math.ceil((100-p)/s)
        days.append(num)
        
    temp = days[0]
    for i in range(1, len(days)):
        if days[i] <= temp:
            
    return answer
