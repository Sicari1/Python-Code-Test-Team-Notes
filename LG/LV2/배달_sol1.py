def solution(N, road, K):
    answer = 0
    
    import heapq
    from collections import defaultdict
    
    INF = 99999999
    graph = defaultdict(list)
    for from_node, to_node, weight in road:
        graph[from_node].append((to_node, weight))
        graph[to_node].append((from_node, weight))

    #print(graph)
    
    def Dijkstra(start, num_nodes):
        distances = [INF] * (num_nodes+1)
        visited = [False] * (num_nodes+1)
        distances[start] = 0
        priority_queue = [(0, start)] # (거리, 노드)
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if visited[current_node] == True:
                continue
                
            visited[current_node] = True # 순서를 잘 기억하고 싶음. Pop -> 방문확인 -> 방문 처리, 근데 어떤 알고리즘은 방문 처리 -> pop -> 뭐 그런것도 있지않나? 싹 정리좀 해줄래??
            for neighbor, weight in graph[current_node]: # 여기도 자꾸 까먹음. graph.items()이런식으로 자꾸 전체 반복을 돌려고 함. 이미 함수안에 들어가있어서 안쪽만 반복 돌리면 됨.
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]: # current_distance가 아니고 distances[neighbor]임 !!! 지금 인접 노드에 대한 거리를 업데이트 하고 있음!!
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
                    
        return distances
    
    
    distances = Dijkstra(1, N)
    #print(distances)
        
    return sum(1 for d in distances if d <= K)



# 어떤 문제에서, 어떤 방법에서(DFS, BFS, 다익스트라 등)는 함수를 짤 때 visited나 computers 혹은 maps 같은 함수를 함수 자체에 넣을 때가 있고, 안넣을때가 있는데
# 그런 기준을 잘 모르겠음. 시작점도 마찬가지. 이런 함수들을 잘 짜는 방법있을까? 어떤 값을 함수에 줘야하는지 잘 모르겠음.
# 일반적으로 생각해봤을 때는, 재귀 느낌이 있으면 함수에 distances나 map같은 것도 그대로 다 넣어줘야하는 것 같기도 함..
