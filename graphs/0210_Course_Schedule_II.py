class Solution(object):
    def solve(self, graph, cnt, nums):
        from collections import deque
        q = deque()
        anss = [0] * nums
        k = 0
        i = 0
        ans = 0
        for x in cnt:
            if x == 0:
                q.append(i)
                ans += 1
                anss[k] = i
                k += 1
            i += 1
        while q:
            y = q.popleft()
            for x in graph[y]:
                cnt[x] -= 1
                if cnt[x] == 0:
                    q.append(x)
                    ans += 1
                    anss[k] = x
                    k += 1
        if ans == nums:
            return anss
        return []
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        cnt = [0] * numCourses
        for x in prerequisites:
            graph[x[1]].append(x[0])
            cnt[x[0]] += 1
        return self.solve(graph, cnt, numCourses)