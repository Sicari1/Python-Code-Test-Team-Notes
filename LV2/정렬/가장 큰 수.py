from functools import cmp_to_key

def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))

    # 커스텀 비교 함수: 두 수를 합쳤을 때 더 큰 쪽을 앞으로
    def compare(x, y):
        if x+y > y+x:
            return -1
        elif x+y < y+x:
            return 1
        else:
            return 0
    
    numbers.sort(key=cmp_to_key(compare))
    return str(int(''.join(numbers)))
