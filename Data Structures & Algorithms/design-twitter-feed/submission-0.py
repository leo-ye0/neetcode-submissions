class Twitter:

    def __init__(self):
        # Global counter to assign unique, increasing timestamps to tweets
        self.timestamp = 0
        
        # Maps userId -> list of tuples: [(timestamp, tweetId), ...]
        self.tweets = defaultdict(list)
        
        # Maps userId -> set of followeeIds: {followeeId1, followeeId2, ...}
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        # Store the tweet at the end of the user's personal tweet list
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        
        # A user always automatically "follows" themselves to see their own tweets
        self.following[userId].add(userId)
        
        # 1. Initialize the Max-Heap with the absolute newest tweet from each followee
        for followeeId in self.following[userId]:
            if followeeId in self.tweets and self.tweets[followeeId]:
                # Get the index of the very last tweet in their list
                last_idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][last_idx]
                
                # Push into heap: (-time, tweetId, followeeId, next_index_to_look_at)
                # We use negative time to turn Python's min-heap into a max-heap
                heapq.heappush(max_heap, (-time, tweetId, followeeId, last_idx - 1))
                
        # 2. Extract the top 10 most recent tweets
        while max_heap and len(res) < 10:
            neg_time, tweetId, followeeId, idx = heapq.heappop(max_heap)
            res.append(tweetId)
            
            # If this followee has more historical tweets left, push the next newest one
            if idx >= 0:
                time, next_tweetId = self.tweets[followeeId][idx]
                heapq.heappush(max_heap, (-time, next_tweetId, followeeId, idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent users from causing weird loop bugs by trying to follow themselves
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Use discard instead of remove to safely handle cases where they weren't following
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
