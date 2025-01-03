def solution(clothes):
    answer = 1
    from collections import defaultdict
    A = defaultdict(list)
    
    for cloth in clothes:
        name, kind = cloth[0], cloth[1]
        A[kind].append(name)
    
    for value in A.values():
        answer *= len(value) + 1
    return answer -1
