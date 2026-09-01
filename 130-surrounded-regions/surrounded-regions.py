class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Rows, Cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def capture():
            q = deque()
            for r in range(Rows):
                for c in range(Cols):
                    if (r == 0 or r == Rows-1 or c == 0 or c == Cols - 1) and board[r][c] == "O":
                        q.append((r,c))

            while q:
                r,c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < Rows and 0 <= nc < Cols and board[nr][nc] == "O":
                            q.append((nr, nc))
        
        capture()
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
