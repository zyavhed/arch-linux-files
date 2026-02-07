from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Prepare adjancy List
        if endWord not in wordList:
            return 0

        adjacencyList = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adjacencyList[pattern].append(word)
        
        #BFS
        q = deque()
        visited = set()
        q.append(beginWord)
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                front = q.popleft()
                if front == endWord:
                    return level
                for i in range(len(front)):
                    pattern = front[:i] + '*' + front[i+1:]
                    for wrd in adjacencyList[pattern]:
                        if wrd not in visited:
                            visited.add(wrd)
                            q.append(wrd)

        return 0