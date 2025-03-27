def solution(k, dungeons):
    from itertools import permutations
    answer = 0
    start = k
    for perm in list(permutations(dungeons)):
        count = 0
        k = start
        #print(perm)
        for i in range(len(perm)):
            if k >= perm[i][0]:
                k -= perm[i][1]
                count +=1
                #print(perm[i], k, count)
            else:
                #print('break')
                break
        answer = max(answer, count)      
        #print(answer)
            
    return answer
