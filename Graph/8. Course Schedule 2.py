class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            adjList[course].append(prereq)
        visited = set()
        res = []
        # meaning, the courses which doesnt have any pre-requisites
        for cour, pre in adjList.items():
            if pre == []:
                res.append(cour)
                
        def dfs(course):
            if adjList[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for pre_req in adjList[course]:
                if not dfs(pre_req):
                    return False
            visited.remove(course)
            # meaning yes, this course can be completed. so no need of any pre-requisites now. thank you
            adjList[course] = []
            res.append(course)
            return True
    
        for cour in range(numCourses):
            if not dfs(cour):
                return []
        return res