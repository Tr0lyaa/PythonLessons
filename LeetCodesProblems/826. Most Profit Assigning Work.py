class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        job_profiles = [(0, 0)]

        for i in range(len(difficulty)):
            job_profiles.append((difficulty[i], profit[i]))

        job_profiles.sort()
        total_profit = 0

        for i in range(len(job_profiles) - 1):
            job_profiles[i + 1] = (job_profiles[i + 1][0], max(job_profiles[i][1], job_profiles[i + 1][1]))

        for worker_ in worker:

            left = 0
            right = len(job_profiles) - 1
            max_profit = 0

            while left <= right:
                mid = (left + right) // 2

                if worker_ >= job_profiles[mid][0]:
                    max_profit = max(max_profit, job_profiles[mid][1])
                    left = mid + 1
                else:
                    right = mid - 1

            total_profit += max_profit

        return total_profit


s = Solution()
print(s.maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82]))