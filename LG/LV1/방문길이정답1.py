def solution(dirs):
    visited = set() # 방문한 길 (간선) 저장
    c_x, c_y = 5, 5 # 시작 좌표 (5,5)
    
    move = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L':(-1,0)}
    
    for dir in dirs:
        dx, dy = move[dir]
        nx, ny = c_x + dx, c_y + dy # 이동할 위치 계산
        
        # 범위 확인 (0,0) ~ (10,10) 내에서만 이동
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            # (현재위치 -> 이동 위치)와 (이동 위치 -> 현재 위치) 둘 다 저장 (중복 방지)
            visited.add((c_x, c_y, nx, ny))
            visited.add((nx, ny, c_x, c_y))
            
            c_x, c_y = nx, ny # 위치 업데이트
            
    return len(visited) // 2 # 양방향 저장했으므로 2로 나눠 반환
