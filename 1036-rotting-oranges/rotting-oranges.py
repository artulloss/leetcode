class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = set()
        fresh = set()

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 2:
                    rotten.add((x,y))
                elif cell == 1:
                    fresh.add((x, y))

        # def display(x, y):
        #     print("=============")
        #     for rx, row in enumerate(grid):
        #         for cy, cell in enumerate(row):
        #             if rx == x and cy == y:
        #                 print("[" + str(cell) + "]", end="")
        #             else:
        #                 print(" " + str(cell) + " ", end="")
        #         print()

        def neighbors(x, y):
            adjs = [
                (x + 1, y), # Left
                (x - 1, y), # Right
                (x, y + 1), # Top
                (x, y - 1)  # Bottom
            ]
            adjs = [(x, y) for x, y in adjs if isValid(x,y) and grid[x][y] == 1]
            return adjs

        def isValid(x, y):
            return x < len(grid) and y < len(grid[x]) and x >= 0 and y >= 0


        minutes = 0

        # Execute bfs
        q = deque([
            ((rx, ry), 0) for rx, ry in rotten
        ])
        while len(q):
            (cx, cy), dist = q.popleft()
            if grid[cx][cy] == 1:
                minutes = max(minutes, dist)
            # display(cx, cy)
            grid[cx][cy] = 2
            for nx, ny in neighbors(cx, cy):
                if not grid[nx][ny] == 2:
                    q.append(((nx,ny), dist + 1))
                    grid[cx][cy] = 2


        for x, y in fresh:
            if grid[x][y] == 1:
                return -1

        return minutes
                

