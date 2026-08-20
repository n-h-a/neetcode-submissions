class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.time_map[key]

        lo = 0
        hi = len(pairs) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_ts = pairs[mid][0]

            if mid_ts <= timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return "" if hi < 0 else pairs[hi][1]
        
# GOAL
# ========
# Create a DS that can...
#   1) store multiple values for the same key at diff timestamps
#   2) retrieve the key's value at a certain timestamp
# set(key, value, timestamp):
#   Stores key with the value at given timestamp.
# get(key, timestamp):
#   Returns largest value that set called previously s.t.
#   timestamp_prev <= timestamp. If none, returns "".

# NOTES
# ========
# key, value only lowercase and digits, never empty
# timestamp is nonnegative
# timestamps are strictly increasing

# BRUTE FORCE
# ========
# set():
#   Given key, append value and timestamp to list.
# TC: O(1)
# SC: O(1)
# 
# get():
#   Given key and timestamp,
#       Retrieve list of pairs at key -- O(1),
#       Loop through list of pairs backwards -- O(T)
#           If timestamp <= current timestamp,
#               Return value at current timestamp.
# TC: O(T) s.t. T is the timestamp.
# SC: O(1)

# IDEA
# ========
# Why is brute force suboptimal?
#   get() goes through every timestamp for a key, but
#   b/c the timestamps are strictly increasing, we can
#   can actually eliminate half of the timestamps at
#   every iteration.
# We use binary search to find largest <= timestamp.
# We use a hash map instead of a list for faster retrieval.
# 
# set():
#   Given key, append value and timestamp to hash set.
# TC: O(1)
# SC: O(1)
# 
# get():
#   Timestamps are in increasing order.
#   What are we looking for?
#       The largest timestamp <= timestamp.
#   We do the whole search space for timestamps [0, timestamp].
#       If mid == timestamp, return value.
#       If mid > timestamp, move hi to mid - 1.
#       If mid < timestamp, 
#           If there is a value and update minimum.
#           Move lo to mid + 1.
#   If value not found, return value at minimum.
# TC: log(T) st. T is the timestamp.
# SC: O(1)

# BETTER
# ========
# set():
#   Given key, append value and timestamp to list.
# TC: O(1)
# SC: O(1)
# 
# get():
#   Indices are in increasing order.
#   What are we looking for?
#       The largest timestamp <= timestamp.
#   We do the whole search space for indices.
#       Retrieve mid timestamp.
#       If mid <= timestamp, move lo to mid + 1.
#       If mid > timestamp, move hi to mid - 1.
#   Return "" if hi is negative. Otherwise, return value at hi.
# TC: log(K) st. K is the # of set calls for that key.
# SC: O(1)