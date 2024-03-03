from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for course, dependency in prerequisites:
            adjacency[course].append(dependency)

        def dfs(course):
            if flags[course] == 1:
                return False
            elif flags[course] == -1:
                return True
            flags[course] = 1
            for dependency in adjacency[course]:
                if not dfs(dependency): return False
            flags[course] = -1
            return True

        for course in range(numCourses):
            # print(course, dfs(course), flags)
            if not dfs(course): return False
        return True

if __name__ == "__main__":
    prerequisites = [[1,0]]
    numCourses = 2
    r = Solution().canFinish(numCourses, prerequisites)
    print(r)