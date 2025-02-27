def is_valid_move(nx, ny): # 좌표평면을 벗어나는지 체크하는 함수
        return 0 <= nx < 11 and 0 <= ny < 11 # Bool을 and로 연결
    
def update_location(x, y, dir): # 명령어를 통해 다음 좌표 결정
    if dir == 'U':
        nx, ny = x, y+1
    elif dir == 'D':
        nx, ny = x, y-1
    elif dir == 'R':
        nx, ny = x+1, y
    elif dir == 'L':
        nx, ny = x-1, y
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    ans = set() # 겹치는 좌표는 1개로 처리하기 위함
    for dir in dirs: # 주어진 명령어로 움직이면서 좌표 저장
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny): # 벗어난 좌표는 움직이지 않음
            continue
        # A에서 B로 간 경우 B에서 A도 추가해야함(총 경로의 개수는 방향성이 없음)
        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y))
        x, y = nx, ny # 좌표를 이동했으므로 업데이트
    return len(ans)/2
