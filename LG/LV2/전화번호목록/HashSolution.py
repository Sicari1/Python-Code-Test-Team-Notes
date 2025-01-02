def solution(phone_book):
    # 1. 전화번호를 해시 테이블에 저장
    phone_hash = set(phone_book)
    
    # 2. 각 번호의 접두사 확인
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in phone_hash:
                return False
    return True
