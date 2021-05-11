import collections
import heapq


class Solution:
    # kruskal
    def getMinRiskValue(self, n, m, x, y, w):  # n个位置， m条无向边，每条边表示位置x到位置y，权重w
        parent = [i for i in range(n + 1)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            else:
                parent[rootx] = rooty
                return True

        edges = sorted(zip(w, x, y))

        for w, x, y in edges:
            if union(x, y) and find(0) == find(n):  # early return without constructing MST
                return w

    # prim
    def getMinRiskValue2(self, n, m, x, y, w):
        # construct graph
        graph = collections.defaultdict(list)
        for i in range(m):
            graph[x[i]].append((y[i], w[i]))
            graph[y[i]].append((x[i], w[i]))

        # Prim's algorithm with min heap
        mst = collections.defaultdict(list)
        mini_heap = [(w, 0, y) for y, w in graph[0]]  # 从0位置出发构造，（weight， 0， end）
        max_risk = 0

        while n not in mst:
            w, s, e = heapq.heappop(mini_heap)  # weight start end 当前弹出来的就是权重最小的
            if e not in mst:
                mst[s].append((e, w))
                mst[e].append((s, w))
                max_risk = max(max_risk, w)
                for ee, ew in graph[e]:  # 以e为起点，ee为重点，权重为ew的边
                    if ee not in mst:
                        heapq.heappush(mini_heap, (ew, e, ee))

        return max_risk


n = int(input())
m = int(input())

x = []
for char in input().strip(''):
    if str(0) <= char <= str(9):
        x.append(int(char))
y = []
for char in input().strip(''):
    if str(0) <= char <= str(9):
        y.append(int(char))

w = []
for char in input().strip(''):
    if str(0) <= char <= str(9):
        w.append(int(char))

solution = Solution()
print(solution.getMinRiskValue2(n, m, x, y, w))
