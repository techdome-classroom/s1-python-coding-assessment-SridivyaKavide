class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            # Base case: If out of bounds, already visited, or water
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] == 'W':
                return
            # Mark the cell as visited
            visited[r][c] = True
            # Explore all four possible directions (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    # Start a new DFS traversal for a new island
                    dfs(r, c)
                    island_count += 1

        return island_count
