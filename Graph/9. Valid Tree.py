class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        # Two ways adjency list
        for f,t in edges:
            adjList[f].append(t)
            adjList[t].append(f)

        visited = set()
        # print(adjList)
        def dfs(f,prev):
            if f in visited:
                return False
            visited.add(f)
            for t in adjList[f]:
                # meaning lets not go back to where we came from
                if t == prev:
                    continue
                # meaning there was a cycle in the graph. so it cant be tree
                if not dfs(t,f):
                    return False
            return True

        # dfs from one node only is enough
        if not dfs(0, None):
            return False
        # have we seen all the numbers in dfs? if yes, the graph is connected
        return len(visited) == n