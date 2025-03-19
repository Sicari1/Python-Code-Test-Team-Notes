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



'''
🔥 DFS (백트래킹) 함수의 설계가 막막할 때?
어떤 인수가 들어가야 하는지, 변수를 어디서 선언해야 하는지 고민되는 상황이구나!
이런 문제를 풀 때 "어떻게 하면 DFS를 바로 떠올릴 수 있을까?" 라는 고민이 많을 거야.

✅ 핵심은 "문제 풀이의 흐름"을 먼저 잡고, 그다음에 DFS 함수의 인자를 정하는 것!
✔️ DFS를 바로 짜려 하지 말고, 먼저 "탐색 흐름"을 단계별로 정리하는 연습을 하면 좋아!
✔️ "필요한 데이터"를 먼저 정리하고, 그 데이터를 어떻게 넘길지 생각하면 훨씬 쉽게 짤 수 있어.

🎯 DFS 같은 함수를 바로 짜려면? (한 단계씩 생각하는 방법)
✅ Step 1: "탐색의 흐름"을 먼저 글로 정리하기
DFS(백트래킹)는 "어떤 데이터를 탐색할 것인가?" 가 가장 중요해.
→ 이 문제에서는 "퀸을 배치할 행(row)과 열(col)을 결정하는 것"이 탐색의 핵심!

💡 예제: N-Queen 문제에서 탐색 흐름을 먼저 정리해보자!

1. 행(row)을 0부터 N-1까지 하나씩 채운다.
2. 각 행에서 모든 열(col) 중 퀸을 놓을 수 있는 위치를 탐색한다.
3. 퀸을 놓을 수 있다면 해당 위치에 배치하고 다음 행(row+1)으로 이동한다.
4. 만약 N개의 퀸을 모두 배치했다면 해답(count++)을 증가시킨다.
5. 한 경우의 탐색이 끝나면 이전 상태로 돌아가서(col을 변경하고) 다시 탐색한다. (백트래킹)
✔️ 이렇게 탐색 흐름을 먼저 글로 정리하면, DFS 함수에 들어갈 인자가 확실해짐!

✅ Step 2: "DFS 함수의 역할"을 정하고 필요한 인자 추출하기
✔️ DFS 함수가 하는 역할은 "row번째 행에서 퀸을 배치하고 다음 행을 탐색하는 것"
✔️ 그러면 DFS 함수에 들어갈 인자는 무엇이 필요할까?

💡 N-Queen에서 필요한 정보

현재 row (탐색하는 행)
board (현재까지 배치된 퀸들의 정보)
count (정답 개수를 저장할 변수) → 리스트 사용 (전역 변수로 안 쓰려면 count[0] += 1)
'''
