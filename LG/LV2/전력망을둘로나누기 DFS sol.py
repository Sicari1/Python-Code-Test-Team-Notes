def build_graph(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def dfs(node, parent, graph):
    cnt = 1
    for child in graph[node]:
        if child != parent: # 부모 노드가 아닌경우에만 탐색 -> 왔던 노드로 돌아가지 않도록 (무한 루프 방지), 어디서 왔는지를 기록한 거라고 생각하면 됨.
            cnt += dfs(child, node, graph)
            
    return cnt


def solution(n, wires):
    graph = build_graph(n, wires)
    min_diff = float('inf')
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        cnt_a = dfs(a, b, graph)
        cnt_b = n - cnt_a
    
        min_diff = min(min_diff, abs(cnt_a - cnt_b))
        
        graph[a].append(b)
        graph[b].append(a) 
        
    return min_diff


    return answer
