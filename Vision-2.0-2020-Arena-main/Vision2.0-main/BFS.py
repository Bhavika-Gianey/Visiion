
import numpy as np


class FindPath:
    parent = np.ones(81, dtype="uint8") * (-1)
    end = -1
    path = []

    def __init__(self, adj, val, start, s):
        self.adj = adj
        self.val = val
        self.start = start
        c=0
        for i in ('TY','SY','CY','TR','SR','CR'):
            c=c+1
            if (s==i):
                self.t=c
        self.path=[]
        self.perform_bfs()
        self.get_path()
        self.path.reverse()
        self.path.pop(0)
        if len(self.path)!=0:
            for i in (31,41,39,49):
                if self.path[len(self.path)-1] ==i:
                    self.path.append(40)

    def perform_bfs(self):
        visited = [False] * 81
        q = [self.start]

        # Set source as visited
        visited[self.start] = True

        while q:
            vis = q[0]

            # Print current node
            # print(vis, end=' ')
            q.pop(0)

            # For every adjacent vertex to
            # the current vertex
            for i in range(0, 81):
                if (self.adj[vis][i] == 1 and
                        (not visited[i])):
                    # Push the adjacent node
                    # in the queue
                    q.append(i)

                    # set
                    visited[i] = True
                    self.parent[i] = vis
                    if self.val[i] == self.t:
                        self.end = i
                        print("broke at", i)
                        return

    def get_path(self):
        k = self.end
        while 1:
            self.path.append(k)
            k=self.parent[k]
            if k==-1:
                break
            





