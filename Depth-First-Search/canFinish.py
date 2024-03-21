from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        request_dict = {}
        for i in range(numCourses):
            request_dict[i] = []
        for course, pre in prerequisites:
            request_dict[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if request_dict[course] == []:
                return True
            
            visited.add(course)
            for pre in request_dict[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            
            request_dict[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


if __name__ == "__main__":
    numCourses = 3
    prerequisites = [[1, 0], [2, 1]]
    r = Solution().canFinish(numCourses, prerequisites)
    print(r)
