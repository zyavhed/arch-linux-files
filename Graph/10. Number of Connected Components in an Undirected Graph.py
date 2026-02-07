class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        # Two ways adjency list
        for f,t in edges:
            adjList[f].append(t)
            adjList[t].append(f)

        all_nodes = set(range(n))

        def dfs(node):
            all_nodes.remove(node)
            for nei in adjList[node]:
                if nei in all_nodes:
                    dfs(nei)

        count = 0
        while all_nodes:
            count += 1
            first = next(iter(all_nodes))
            dfs(first)
        return count
