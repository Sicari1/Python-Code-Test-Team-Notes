# Find & Union, 탐색과 합치기
# 탐색 알고리즘

def find(x, parents):
  if parents[x] != x: # 루트가 본인이 아니면
    parents[x] = find(parents[x], parents) # 경로 압축
  return parents[x]

def union_set(x, y, parents, rank_data):
  root1 = find(x, parents)
  root2 = find(y, parents)

# 랭크 알고리즘
  if root1 != root2:
    if rank_data[root1] < rank_data[root2]:
      parents[root1] = root2
    elif rank_data[root1] > rank_data[root2]:
      parents[root2] = root1
    else:
      parents[root2] = root1
      rank_data[root1] += 1

def solution(k, operations):
  # 초기의 각 부모노드의 값은 현재 노드(인덱스)로 설정
  parents = list(range(k))
  rank_data = [0] * k

  results = []
  for op in operations:
    if op[0] == 'u':
      x = int(op[1])
      y = int(op[2])
      union_set(x, y, parents, rank_data)
    elif op[0] == 'f':
      x = int(op[1])
      y = int(op[2])
      # 파인드 연산을 통해 x, y의 루트노드가 같은지 확인해서 결과 저장
      result.append(find(x, parents) == find(y, parents))

  return results
