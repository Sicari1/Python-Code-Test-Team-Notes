import heapq
from collections import defaultdict, deque

INF = 9999999999

def solution(start, num_nodes, edges):
  # 그래프 초기화(인접 리스트)
  graph = defaultdict(list)
  for from_node, to_node, weight in edges:
    graph[from_node].append((to_node, weight))

  # 최단 경로 길이 및 방문 이력 초기화
  distances = [INF] * num_nodes
  visited = [False] * num_nodes
  distances[start] = 0

  # 우선순위 큐
  priority_queue = [(0, start)] # (거리, 노드)

  while priority_queue:
    # 현재 노드 찾기
    current_distance, current_node = heapq.heappop(priority_queue)

    # 이미 방문한 노드는 무시
    if visited[current_node] = True:
      continue

    # 현재 노드 방문 처리
    visited[current_node] = True

    # 인접 노드에 대한 거리 업데이트
    for neighbor, weight in graph[current_node]:
      new_distance = distances[current_node] + weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heapq.heappush(priority_queue, (new_distance, neighbor))

  return distances








