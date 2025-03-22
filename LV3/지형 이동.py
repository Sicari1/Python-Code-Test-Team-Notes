from heapq import heappush, heappop

def solution(land, height):
    n = len(land)
    answer = 0

    # 방문 체크 배열
    visited = [[False]*n for _ in range(n)]

    # 우선순위 큐 (최소 힙)
    q = []
    heappush(q, [0, 0, 0])  # 시작점: [비용, i, j]

    # 4방향 이동
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    while q:
        cost, i, j = heappop(q)

        if visited[i][j]:
            continue

        visited[i][j] = True
        answer += cost  # 해당 칸으로 오는데 든 비용을 누적

        # 상하좌우 인접한 칸 탐색
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                height_diff = abs(land[i][j] - land[ni][nj])
                if height_diff > height:
                    # 사다리 설치가 필요한 경우 → 비용 발생
                    heappush(q, [height_diff, ni, nj])
                else:
                    # 사다리 없이 이동 가능 → 비용 0
                    heappush(q, [0, ni, nj])

    return answer
