class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = {i:[] for i in range(1,n+1)}

        
        def dfs(u,v):
            if u == v:
                return True
            visited.add(u)
            for new_u in adjList[u]:
                if new_u in visited:
                    continue
                if dfs(new_u,v):
                    return True
            return False

        for u,v in edges:
            visited = set()
            if dfs(u,v):
                return [u,v]
            adjList[u].append(v)
            adjList[v].append(u)