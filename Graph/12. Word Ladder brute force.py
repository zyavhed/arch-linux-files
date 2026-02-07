from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def does_differ_by_unit_character(s,t):
            if len(s) != len(t):
                return False
            diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return True
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque()
        q.append(beginWord)
        
        level = 0
        while q:
            size = len(q)
            for i in range(size):
                front = q.popleft()
                if front == endWord:
                    return level + 1
                to_be_removed = []
                for val in wordSet:
                    if does_differ_by_unit_character(front,val):
                        q.append(val)
                        to_be_removed.append(val)
                for val in to_be_removed:
                    wordSet.remove(val)
            level += 1
        return 0
            
