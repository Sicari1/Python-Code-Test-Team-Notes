def solution(number, k):
    answer = ''
    
    while k: # while문처럼 써서 줄어들 때 까지 하는 게 좋을 것 같음.
        minnum = min(number)
        print("minnum :", minnum)
        #number = number - minnum # number에서 minnum을 하나 빼고싶은데 방법 모르니까 일단 반복문으로 하자
        # 앞에서 부터 빼는게 맞을듯
        index = number.find(minnum)
        number = number[:index] + number[index+1:]
        
        # 이거는 왜 안됐는지도 확인해봐야함 
#         for i in range(0,len(number)):
#             if minnum == number[i]:
#                 number = number[:i] + number[i+1:]
        k += -1

# 근데 앞에서 부터 제거했는데도 길이가 같아서 다른 큰 수가 첫째자리에 오는게 더 클 경우를 생각해야함.
# 근데 뭔가 시작부터 좀 잘못된 것 같음 ..ㅠㅠ
    answer = number

    return answer
