class PaperGrid:
    def __init__(self, lines):
        self.grid = [list(line) for line in lines]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def neighbors(self, r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    yield self.grid[rr][cc]

    def is_accessible(self, r, c):
        return self.grid[r][c] == '@' and sum(n == '@' for n in self.neighbors(r, c)) < 4
    
    def remove_paper(self, r, c):
        if self.is_accessible(r, c):
            self.grid[r][c] = 'x'

    def count_accessible(self):
        return sum(
            self.is_accessible(r, c)
            for r in range(self.rows)
            for c in range(self.cols)
        )