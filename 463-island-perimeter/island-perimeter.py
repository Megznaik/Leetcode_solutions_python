class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit =set()

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0):
                return 1
            if (r,c) in visit:
                return 0

            visit.add((r,c))
            perim = dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return perim

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r,c)
                    perim += 1
        return 0
