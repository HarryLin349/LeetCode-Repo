'''
Job Sequencing Problem
Given two arrays: deadline[] and profit[], where the index of deadline[] represents a job ID, 
and deadline[i] denotes the deadline for that job and profit[i] represents profit of doing ith job. Each job takes exactly one unit of time to complete, and only one job can be scheduled at a time. A job earns its corresponding profit only if it is completed within its deadline.

The objective is to determine:

The maximum profit that can be obtained by scheduling the jobs optimally.
The total number of jobs completed to achieve this maximum profit.

Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: 2 60
Explanation: We select 1st and 3rd jobs. All jobs except first job have a deadline of 1, thus only one of these can be selected along with the first job with the total profit gain of 20 + 40 = 60.


Input: deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: 2 127
Explanation: The first and third job have a deadline of 2, thus both of them can be completed and other jobs have a deadline of 1, thus any one of them can be completed. Both the jobs with a deadline of 2 is having the maximum associated profit, so these two will be completed, with the total profit gain of 100 + 27 = 127.
'''

# deadline = [4,1,1,1]
# profit = [20,10,40,30]

deadline = [2, 1, 2, 1, 1]
profit = [100, 19, 27, 25, 15]

def findProfit(deadline, profit):
  '''
  idea: greedy? sort by job time
  - take most profit X 
  - take first deadline X

  idea: dp?
  dp(i) -> most profit given current time of i given taken jobs xyz..
  at each choice we take a random valid job O(n)
  dp (i) = profit + dp(i+1)
  O(n^2)

  sort the jobs list by deadline? then we can dp ?
  choice is either take or dont take, either way you're passing the job (no repeats)
  dp[i][j] max profit from i..n given time is j.
  recurrence:
    either dont take job
    dp(i,j) = dp(i+1,j)
    or do
    dp(i,j) = profit + dp(i+1, j+1)
  '''
  n = len(deadline)
  memo = [[-1 for _ in range(n)] for _ in range(n)]
  jobs = []
  for i in range(n):
    jobs.append((deadline[i], profit[i]))
  
  jobs.sort(key=lambda x: x[0])
  print(jobs)
  def dp(i,j):
    # base case, i >= n
    if i >= n or j >= n:
      return 0
    if memo[i][j] != -1:
      return memo[i][j]

    sol1, sol2 = 0,0
    # case 1: skip the cur job
    sol1 = dp(i+1, j)
    # case 2: take the cur job
    if (j < jobs[i][0]):
      sol2 = jobs[i][1] + dp(i+1, j+1)
    
    memo[i][j] = max (sol1, sol2)
    return memo[i][j]
  return dp(0,0)

print(findProfit(deadline, profit))