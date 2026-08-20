class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(deque)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].popleft()
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        # Get the latest tweet of each followee and add to minHeap.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        # While minHeap is not empty and we don't have 10 yet...
        while minHeap and len(res) < 10:
            # Pop the latest tweet and add it to result.
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # Push the next latest tweet from that same followee.
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# OBSERVATIONS
# =========
# Data:
#   * users
#   * each users' tweets
#   * each users' followers
# Actions:
#   * can post a tweet
#   * can follow
#   * can unfollow
#   * can get news feed

# IDEA
# =========
#   For initialization:
#       Use a hashmap (user id --> hashset of follower IDs)
#       Use a hashmap (user id --> queue of (count, tweet IDs))
#   For post tweet:
#       Grab user and add tweet to user's tweets with time + id
#   For follow:
#       Add user to hashset.
#   For unfollow:
#       Remove user from hashset.
#   For getNewsFeed:
#       Keep min heap of latest tweets from all followees ALWAYS.
#       Pop from min heap to build result.
# TC: O(N log N) for each news feed call. O(1) for everything else.
# SC: O(N * m + N * M + n) s.t. n is # of followeeIds, m is max # of tweets for any user, N is total # of users, and M is max # of followees for any user.