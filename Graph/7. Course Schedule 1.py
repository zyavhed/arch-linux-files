from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            adjList[course].append(prereq)
        visited = set()
        def dfs(course):
            if adjList[course] == [] :
                return True
            if course in visited:
                return False
            visited.add(course)
            for pre_req in adjList[course]:
                if not dfs(pre_req):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True
    
        for cour in range(numCourses):
            if not dfs(cour):
                return False
        return True