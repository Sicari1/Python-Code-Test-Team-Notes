def solution(progresses, speeds):
    answer = []
    from collections import deque
    queue = deque(progresses)
    speed = deque(speeds)
    while queue:
        count = 0
        for i in range(len(queue)):
            queue[i] = queue[i] + speed[i]
        while queue and queue[0] >= 100:
            queue.popleft()
            speed.popleft()
            count += 1
        if count:
            answer.append(count)    
    
    
    return answer
