from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.user_posts = defaultdict(list)
        self.followerlists = defaultdict(set)  # use set to avoid duplicates
        self.tweetcount = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetcount += 1
        self.user_posts[userId].append((-1*self.tweetcount, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        h = []

        # Include tweets from followees
        for followee in self.followerlists[userId]:
            h.extend(self.user_posts[followee])
        
        # Include user's own tweets
        h.extend(self.user_posts[userId])

        # Heapify all the values to min heap
        heapq.heapify(h)
        
        # Get 10 most recent tweets based on timestamp
        recent = []
        while h and len(recent) < 10:
            count,tweetId = heapq.heappop(h)
            recent.append(tweetId)
        return recent

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # prevent self-follow
            self.followerlists[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerlists[followerId].discard(followeeId)
