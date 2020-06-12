from collections import deque

class Grid:
  def __init__(self):
    self.R = 4
    self.C = 4
    self.m = [
      ['S', '.', '#', '.'],
      ['#', '.', '.', '.'],
      ['#', '#', '.', '.'],
      ['.', '.', 'E', '.']
    ]

    self.sr, self.sc = 0, 0 #row and column values    
    self.rq = deque()
    self.cq = deque()

    # variables used to track the number of steps taken
    self.move_count = 0
    self.nodes_left_in_layer = 1
    self.nodes_in_next_layer = 0

    self.reached_end = False

    self.visited = [[False for i in range(self.R)] for j in range(self.C)]

    #north, south, east, west direction vectors
    self.dr = [-1, +1, 0, 0]
    self.dc = [0, 0, +1, -1]

  def explore_neighbours(self, r, c):
    for i in range(4):
      rr = r + self.dr[i]
      cc = c + self.dc[i]    

      # skip out of bounds locations
      if rr < 0 or cc < 0: continue
      if rr >= self.R or cc >= self.C: continue

      # skip visited locations or blocked cells
      if self.visited[rr][cc]: continue
      if self.m[rr][cc] == '#': continue

      self.rq.append(rr)
      self.cq.append(cc)
      self.visited[rr][cc] = True
      self.nodes_in_next_layer += 1

  def solve(self):
    self.rq.append(self.sr)
    self.cq.append(self.sc)
    self.visited[self.sr][self.sc] = True

    while len(self.rq) > 0: # or len(cq) > 0
      r = self.rq.popleft()
      c = self.cq.popleft()
      if self.m[r][c] == 'E':
        self.reached_end = True        
        break

      self.explore_neighbours(r, c)
      self.nodes_left_in_layer -= 1
      if self.nodes_left_in_layer == 0:
        self.nodes_left_in_layer = self.nodes_in_next_layer
        self.nodes_in_next_layer = 0
        self.move_count += 1
    if self.reached_end:
      return self.move_count
    return -1


grid = Grid()
result = grid.solve()
print(result)
print(grid.visited)