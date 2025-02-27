def solution(dirs):
    answer = 0
    grid = [[0] * 11 for _ in range(11)]
    c_x = 5
    c_y = 5
    
    def update(x, y):
        if grid[x][y] == 0:
            grid[x][y] = 1
            
    print('start', c_x, c_y)
    for dir in dirs:
        if dir == 'U':
            c_y += 1
        elif dir == 'D':
            c_y -= 1
        elif dir == 'R':
            c_x += 1
        elif dir == 'L':
            c_x -= 1
        c_x = min(c_x, 10)
        c_y = min(c_y, 10)
        c_x = max(c_x, 0)
        c_y = max(c_y, 0)
        
        print(dir, c_x, c_y)
        
        update(c_x, c_y)
    

    for i in range(11):
        for j in range(11):
            if grid[i][j] == 1:
                answer +=1
        
    print(grid)
    return answer
