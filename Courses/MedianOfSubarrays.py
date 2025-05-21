'''
Find the sum of medians of all odd length subarrays
Given an array arr[] of size N, the task is to find the sum of medians of all sub-array of odd-length.

Input: arr[] = {4, 2, 5, 1}
Output: 18
Explanation : Sub-Arrays of odd length and their medians are :


[4]  -> Median is 4
[4, 2, 5]  -> Median is 4
[2]  -> Median is 2
[2, 5, 1]  -> Median is 2
[5]  -> Median is 5
[1]  -> Median is 1

Their sum = 4 + 4+ 2 + 2 + 5 +1 = 18


Input: arr[] = {1, 2}
Output: 3


'''

input = [1,2]

'''
finding: sum of median of all odd subarrays
need: all medians (probably)
naively: check every odd subarray and find its median (e.g. by sorting nlogn)

Finding a median
- sorting -> nlogn
- minheap and maxheap -> nlogn but we can reuse as we build subarrays
- heapify: O(n) into n/2 log n (nlogn)

idea: start at index 0. try each subarray [0], [0..2], [0..4], etc.
at each step we're adding 2 more elems, which we can put on our two min/maxheaps
overal, for this one case should be nlogn
overall n^2 logn


[2 4 5]
[2 4] [5]

[1 2 3 4 5 6]
[... 3] [4 ...]
add 4
[... 4] [4]
add 2
[ ..2,3] [4..]
'''

from heapq import heapify, heappush, heappop

i = 0 # start of subarrays, increases by 1 each time
j = 0 # end of subarrays

res = 0

n = len(input)
for i in range(n):
  cur = i
  leftheap = [] # a max heap
  rightheap = [] # a minheap
  while cur < n:
    median = -1
    cnum = input[cur]
    if (len(leftheap) < len(rightheap)):
      heappush(leftheap, -cnum)
    else:
      heappush(rightheap, cnum)
      

    # add cur to heap
    if (cur - i) % 2 == 0:
      res +=  median
    cur += 1