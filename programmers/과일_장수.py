def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        answer += m*score[(i+1)*m-1]
    return answer

print(solution(3,	4,	[1, 2, 3, 1, 2, 3, 1]))