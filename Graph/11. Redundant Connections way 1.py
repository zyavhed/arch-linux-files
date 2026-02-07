class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = {i:[] for i in range(1,n+1)}
        print(adjList)

        visited = set()
        def dfs(u,v):
            if u in visited:
                return False
            if u == v:
                return True
            visited.add(u)
            for new_u in adjList[u]:
                if dfs(new_u,v):
                    return True
            visited.remove(u)
            return False

        for u,v in edges:
            if dfs(u,v):
                return [u,v]
            adjList[u].append(v)
            adjList[v].append(u)