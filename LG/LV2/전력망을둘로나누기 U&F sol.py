def solution(n, wires):
    answer = -1
    
    def find(node):
        if roots[node] != node:
            roots[node] = find(roots[node])
        return roots[node]
    
    def union(x, y):
        root1 = find(x)
        root2 = find(y)
        if root1 != root2:
            if chasu[root1] > chasu[root2]:
                roots[root2] = root1
            elif chasu[root1] < chasu[root2]:
                roots[root1] = root2
            else:
                roots[root2] = root1
                chasu[root1] += 1
    
    min_difference = float("inf")
    
    for i in range(len(wires)):
        roots = [i for i in range(n+1)] # 0 ~ n
        chasu = [0] * (n+1)
        
        for j, (a, b) in enumerate(wires):
            if i == j:
                continue
            union(a,b)
    
        from collections import Counter
        group_count = Counter(find(node) for node in range(1, n+1))
        group_sizes = list(group_count.values())
        if len(group_sizes) == 2:
            diff = abs(group_sizes[0] - group_sizes[1])
            min_difference = min(min_difference, diff)
        
    return min_difference
