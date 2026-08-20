class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-count for count in count.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time

# GOAL
# ========
# Given a list of characters and an int m that stands for
# idle time needed inbetween identical tasks, return
# the minimum # of steps needed to process all tasks.

# OBSERVATIONS
# ========
# Since we're looking for minimum steps, we should process 
#   the most frequent tasks first to reduce to idle time.

# IDEA
# ========
# Use a max heap to track the most frequent tasks first
# + use a queue to track tasks in idle time:
#   While max heap and queue are not empty:
#       If max heap not empty, pop it and add to queue
#           decremented, w/ time to be used next if not 0.
#       If queue not empty and first element is the same as
#           time, pop it and add to heap.
#   Return time
# TC: O(N * M) s.t. N is # of tasks and M is idle time 
# SC: O(1) b/c only 26 chars
