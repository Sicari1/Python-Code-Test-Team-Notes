def solution(N, stages):
    answer = []
    스테이지도달클리어 = [0 for _ in range(N)]
    스테이지도달수 = [0 for _ in range(N)]
    f_rate = [0 for _ in range(N)]
    
    for i in range(len(stages)):
        for j in range(0, min(stages[i],N)):
            스테이지도달수[j] += 1
            if stages[i] -1 > j:
                스테이지도달클리어[j] += 1
    
    for k in range(N):
        if 스테이지도달수[k] == 0:
            f_rate[k] = 0
        else:
            f_rate[k] = 1 - (스테이지도달클리어[k]/스테이지도달수[k])       
   # enumerate(f_rate) 하면 (0,값) 형태의 tuple이 됨.
    
    sorted_indices = sorted(enumerate(f_rate), key=lambda x: x[1], reverse=True)
    answer = [idx+1 for idx, _ in (sorted_indices)]
                                 
    return answer
                            
