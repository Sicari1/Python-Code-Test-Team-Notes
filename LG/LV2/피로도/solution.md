# 피로도(프로그래머스 완전탐색) 문제 정리

<br />

## 1. 문제 요약

- 현재 피로도 `k`가 주어집니다.
- 여러 개의 던전이 있고, 각 던전은 `[최소 필요 피로도, 소모 피로도]` 형태로 주어집니다.
- 던전을 탐험하기 위해서는 **현재 피로도가 ‘최소 필요 피로도 이상’** 이어야 합니다.
- 던전을 탐험하면 **‘소모 피로도’** 만큼 현재 피로도가 감소합니다.
- 주어진 던전들을 **최대한 많이** 탐험하고 싶을 때, 최대로 탐험할 수 있는 던전의 **개수**를 구하는 문제입니다.

<br />

---

## 2. 문제 분석

- 던전의 개수 `N`은 최대 8개입니다.
- 순서를 어떻게 정하느냐에 따라, 탐험할 수 있는 던전 수가 달라질 수 있습니다.
- 던전 개수가 최대 8이므로, **모든 순열**(8! = 40320가지)을 시도하더라도 계산 가능 → 완전탐색(브루트 포스)이 가능합니다.

<br />

---

## 3. 풀이 방법 1) DFS(백트래킹) 활용

### 3.1 알고리즘 개념

1. **방문 배열**(visited)을 사용하여, 어떤 던전을 이미 탐험했는지 표시합니다.
2. 현재 피로도가 `dungeons[i]`의 “최소 필요 피로도” 이상이면, 그 던전을 탐험할 수 있습니다.
   - 피로도를 “소모 피로도”만큼 감소시키고,
   - `visited[i] = True` 표시 후, DFS(재귀)로 다음 던전을 계속 탐색합니다.
   - 탐색 후에는 원상복구(백트래킹)합니다.
3. 이렇게 해서 가능한 모든 경로(순서)를 탐색하며, **가장 많이 탐험한 던전 수**(count)의 최대값을 찾습니다.

### 3.2 의사 코드

~~~~python
max_count = 0

def dfs(cur_fatigue, dungeons, visited, count):
    global max_count
    max_count = max(max_count, count)
    
    for i in range(len(dungeons)):
        min_req = dungeons[i][0]
        consume = dungeons[i][1]
        
        # 아직 방문 안 했고, 현재 피로도가 최소 필요 피로도 이상이면 탐험
        if not visited[i] and cur_fatigue >= min_req:
            visited[i] = True
            dfs(cur_fatigue - consume, dungeons, visited, count + 1)
            visited[i] = False

def solution(k, dungeons):
    global max_count
    max_count = 0
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    return max_count
~~~~

### 3.3 복잡도

- 던전 개수 N이 최대 8이므로, 최악의 경우 `O(N!)`가지 경우를 DFS로 탐색합니다.
- 8! = 40,320 정도는 충분히 연산 가능한 범위입니다.

<br />

---

## 4. 풀이 방법 2) `itertools.permutations` 활용

`itertools.permutations`를 이용해 **모든 던전 순열**을 생성하여 탐색합니다.

1. 모든 순열을 생성 (`permutations(dungeons, len(dungeons))`).
2. 순열(배치)마다 **앞에서부터** 순서대로:
   - 현재 피로도로 해당 던전을 갈 수 있는지(`현재 피로도 >= 최소 필요 피로도`) 체크
   - 가능하다면 피로도 감소, `count += 1`
   - 불가능하면 그 순열에서 더 이상 진행 불가
3. 모든 순열을 시도하며 최댓값을 갱신합니다.

### 4.1 예시 코드

~~~~python
from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    for perm in permutations(dungeons, len(dungeons)):
        cur_fatigue = k
        count = 0
        for min_req, consume in perm:
            if cur_fatigue >= min_req:
                cur_fatigue -= consume
                count += 1
            else:
                break
        max_count = max(max_count, count)
    return max_count
~~~~

<br />

---

## 5. 최종 정리

- 던전 개수가 최대 8개이므로 **완전탐색**이 가능.
- **DFS(백트래킹)** 방식 또는 **`itertools.permutations`**를 사용한 순열 탐색 방식 중 편한 것으로 풀 수 있음.
- **시간 복잡도**: 최대 `O(N!)`, N=8이면 충분히 가능한 연산량.
- 핵심 포인트:
  - **현재 피로도**가 **최소 필요 피로도** 이상이어야 던전 탐험 가능
  - 던전을 탐험하면 피로도가 **소모 피로도**만큼 감소
  - **가장 많은 던전**을 돌 수 있는 순서를 찾으면 됨

<br />

---

## 예시 DFS 코드

~~~~python
def solution(k, dungeons):
    visited = [False] * len(dungeons)
    max_count = 0
    
    def dfs(cur_fatigue, count):
        nonlocal max_count
        max_count = max(max_count, count)
        
        for i in range(len(dungeons)):
            min_req, consume = dungeons[i]
            if not visited[i] and cur_fatigue >= min_req:
                visited[i] = True
                dfs(cur_fatigue - consume, count + 1)
                visited[i] = False
    
    dfs(k, 0)
    return max_count
~~~~

- 문제 예시:
  - `k = 80`
  - `dungeons = [[80,20],[50,40],[30,10]]`
  - 결과: `3` (최대 3개 던전 모두 탐험 가능)
