from collections import deque




def bfs(G, start):
visited = []
queue = deque([start])


while queue:
node = queue.popleft()
if node not in visited:
visited.append(node)
queue.extend(G.neighbors(node))
return visited




def dfs(G, start):
visited = []
stack = [start]


while stack:
node = stack.pop()
if node not in visited:
visited.append(node)
stack.extend(G.neighbors(node))
return visited