from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for course, dependency in prerequisites:
            adjacency[course].append(dependency)
        res = []
        
        def dfs(course):
            if flags[course] == 1:
                return False
            elif flags[course] == -1:
                return True
            
            flags[course] = 1
            for dependency in adjacency[course]:
                if not dfs(dependency): return False
            flags[course] = -1
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return []
            print(course, res)
        return res

if __name__ == "__main__":
    numCourses, prerequisites = 5, [[1,0],[2,1],[3,2],[4,3]]
    print(numCourses, prerequisites)
    r = Solution().findOrder(numCourses, prerequisites)
    print(r)