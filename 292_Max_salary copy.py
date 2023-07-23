def solution(T, N, jobs):
	m_t = min(jobs, key = lambda x: x['hour'])['hour'] # min hours of jobs
	# dp[i][j]: max wage in the first i jobs in j hours
	dp = [[0] * (T + 1) for _ in range(N + 1)]
	for j in range(1, N + 1): # job
		for t in range(m_t, T + 1): # time
			job = jobs[j - 1]
			w1 = dp[j - 1][t]
			w2 = job['wage'] + dp[j - 1][t - job['hour']] if job['hour'] <= t else 0
			# update max wage or not 
			dp[j][t] = max(w1, w2)
	return dp[N][T]

if __name__ == "__main__":
	T, N = map(int, input().split())
	jobs = [dict(zip(['hour', 'wage'], map(int, input().split()))) for _ in range(N)]
	res = solution(T, N, jobs)
	print(res)