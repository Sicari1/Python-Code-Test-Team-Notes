def solution(phone_book):
    # 1. 전화번호 정렬
    phone_book.sort()
    
    # 2. 인접한 번호들 비교
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


