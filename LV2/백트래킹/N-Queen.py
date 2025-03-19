def solution(n):
  def is_safe(board, row, col):
    for i in range(row):
      if board[i] == col or abs(board[i] - col) == abs(i - row): # 각 행에 퀸이 하나씩 있는지 여부 체크위한 board[i], 
        return False
      return True

  def backtrack(board, row):
    nonlocal count
    if row == n:
      count += 1
      return
    for col in range(n):
      if is_safe(board, row, col):
        board[row] = col
        backtrack(board, row + 1)
        board[row] = -1

  count = 0
  board = [-1] * n # 초기 상태
  backtrack(board, 0)
  return count
