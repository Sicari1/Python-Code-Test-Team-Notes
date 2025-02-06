def solution(progresses, speeds):
    answer = []
    from collections import deque
    Q = deque(progresses)
    number = 0
    while Q:
        if Q[0] >= 100:
            Q.popleft()
            number += 1
        else:
            number = 0
            for i in range(len(Q)):
                Q[i] += speeds[i]
        answer.append(number)
    return answer
