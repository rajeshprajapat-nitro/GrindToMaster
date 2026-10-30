import heapq
from collections import defaultdict

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int 
        :rtype: int
        "

        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')

        # dist[node][cnt] = minimum cost
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0

        # (cost, node, consecutive_count)
        pq = [(0, 0, 1)]

        while pq:
            cost, u, cnt = heapq.heappop(pq)

            if cost != dist[u][cnt]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:

                if labels[u] == labels[v]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_cost

                    heapq.heappush(
                        pq, (new_cost, v, new_cnt)
                    )

        return -1
