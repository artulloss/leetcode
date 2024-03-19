class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def bfs(coordAndDist):
            coord, dist = coordAndDist
            q = deque([(coord, dist)])
            while len(q):
                coord, dist = q.popleft()
                # printMaze(coord)
                # print(dist)
                markSeen(coord)

                if isExit(coord):
                    return dist

                for adj in neighbors(coord):
                    markSeen(adj)
                    q.append((adj, dist + 1))
            return -1


        def neighbors(coord):
            x, y = coord
            adjs = [
                (x - 1, y), # Left
                (x + 1, y), # Right
                (x, y - 1), # Bottom
                (x, y + 1)  # Top
            ]
            return [ # Only valid neighbors
                coord for coord in adjs if validCoord(coord) and not isSeen(coord) and not isWall(coord) 
            ]

        def validCoord(coord):
            x, y = coord
            return x >= 0 and y >= 0 and x < len(maze) and y < len(maze[x])

        def isWall(coord):
            x, y = coord
            return maze[x][y] == "+"

        def printMaze(coord):
            print("---------------")
            for x, xlist in enumerate(maze):
                for y, ylist in enumerate(maze[x]):
                    if coord[0] == x and coord[1] == y:
                        print("[" + maze[x][y] + "]", end='')
                    else:
                        print(" " + maze[x][y] + " ", end='')
                print()

        def isBorder(coord):
            x, y = coord
            return x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[x]) - 1

        def isExit(coord):
            return (entrance[0], entrance[1]) != coord and isBorder(coord) and not isWall(coord)

        def markSeen(coord):
            x, y = coord
            maze[x][y] = "0"

        def isSeen(coord):
            x, y = coord
            return maze[x][y] == "0"

        start = (entrance[0], entrance[1])
        return bfs((start, 0))