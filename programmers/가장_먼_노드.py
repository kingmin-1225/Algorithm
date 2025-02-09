def solution(n, edge):
    from collections import deque
    answer = 0
    M = 0
    graph = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    visited = [0 for _ in range(n+1)]
    distances = [0 for _ in range(n+1)]
    q = deque([1])
    visited[1] = 1
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                distances[neighbor] = distances[node]+1
                if M < distances[node]+1:
                    M = distances[node]+1
                    answer = 0
                answer += 1
                visited[neighbor] = 1
                q.append(neighbor)

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))