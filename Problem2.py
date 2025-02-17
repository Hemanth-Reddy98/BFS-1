class Solution:
    # Time Complexity: O(V+E)
    # Space Complexity: O(V+E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}
        indegrees = [0] * numCourses
        for i in prerequisites:
            indegrees[i[0]] += 1
            if i[1] not in hashmap:
                hashmap[i[1]] = []
            hashmap[i[1]].append(i[0])

        count = 0
        q = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                count += 1

        if count == numCourses:
            return True

        while q:
            curr = q.pop()
            children = hashmap.get(curr, [])
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)
                    count += 1
                    if count == numCourses:
                        return True

        return False
