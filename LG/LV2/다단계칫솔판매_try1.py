def solution(enroll, referral, seller, amount):
    answer = []
    from collections import defaultdict
    DB = defaultdict(int) 
    IV = defaultdict(str)
    
    for enr, ref in zip(enroll, referral):
        IV[enr] = ref
        DB[enr] = 0 
    
    def dist(receiver, amount):
        if IV[receiver] != '-'  : # 초대한 사람 있으면
            dist(IV[receiver], int(0.1 * amount))
            DB[receiver] += int(amount - int(0.1 * amount))
        elif IV[receiver] == '-':
            DB[receiver] += int(amount - int(0.1 * amount))
        else:
            DB[receiver] += amount
    
    for sell, amo in zip(seller, amount):
        dist(sell, amo*100)
    #print(IV)
    #print(DB)
    for value in DB.values():
        answer.append(value)
        
    return answer


    import sys
    sys.setrecursionlimit(10**6) # python에서 기본 recursion깊이가 1000으로 제한되어있는데, 이를 늘리면 런타임 에러가 발생하지 않을 경우도 있음.
