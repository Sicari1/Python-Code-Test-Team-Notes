# 수학적으로 풀었음
def solution(n, stations, w):
    answer = 0
    import math
        
    if stations[0]-w <= 1:
        pass
    else:
        answer += math.ceil((stations[0]-w-1) / (2*w+1))
    
    if stations[-1]+w >= n:
        pass
    
    else:
        answer += math.ceil((n-stations[-1]-w) / (2*w+1))
    
    for i in range(len(stations)-1):
        answer += math.ceil(((stations[i+1]-w) - (stations[i]+w) - 1) / (2*w+1))
        
    
    return answer
