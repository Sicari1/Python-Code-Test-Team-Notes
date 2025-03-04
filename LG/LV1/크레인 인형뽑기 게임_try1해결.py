def solution(board, moves):
    answer = 0
    
    n = len(board)
    m = len(board[0])
    
    stack = []
    
    for j in range(m): #4
        stack_inner = []
        for i in range(n): #3
            if board[i][j] != 0:
                stack_inner.append(board[i][j])
        stack.append(stack_inner)
    
    baguni = []    
    
    def zzipgi(num, stack):
        if stack and stack[-1] == num:
            stack.pop()
            nonlocal answer
            answer += 2
            return stack
        else:
            stack.append(num)
            return stack
    
    for i in moves:
        if stack[i-1]:
            char = stack[i-1].pop(0)    
            baguni = zzipgi(char, baguni)

    return answer
