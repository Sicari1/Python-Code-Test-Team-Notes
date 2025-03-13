# 그래프를 인접 리스트로 표현
graph = {
  1: [4, 5],
  2: [3],
  3: [],
  4: [2, 3],
  5: [4]
}

# 방문 여부를 표시하는 배열
visited = [False] * (len(graph) + 1)

# DFS
def dfs(current_node):
  # 현재 노드 방문
  visited[current_node] = True
  print(current_node)

  # 현재 노드와 인접한 노드 순회
  for adj_node in graph[current_node]:
    if not visited[adj_node]:
      dfs(adj_node)

# DFS 알고리즘 실행
dfs(1) # 출력값 : 1 4 2 3 5

# BFS
from collections import deque
def bfs(start_node):
  visited = [False] * (len(graph) + 1)

# 시작노드 방문 처리
queue = deque([start_node])
visited[start_node] = True

while queue:
  # 가장 먼저 푸시된 노드 방문
  node = queue.popleft()
  print(node)

  # 인접한 노드 순회
  for adj_node in graph[node]:
    if not visited[adj_node]:
      queue.append(adj_node)
      visited[adj_node] = True

# BFS 알고리즘 실행
bfs(1) # 1 4 5 2 3
