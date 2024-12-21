def solution(n, lost, reserve):
    answer = 0
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    save = 0
    for i in new_lost:
        if i-1 in new_reserve:
            new_reserve.remove(i-1)
            save +=1
        elif i+1 in new_reserve:
            new_reserve.remove(i+1)
            save +=1
    answer = n - len(new_lost) + save
    
    return answer
