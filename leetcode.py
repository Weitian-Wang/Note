class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # (i, j) (x, y)
        # check row i == x
        # check col j == y
        # main diag i - j == x - y
        # anti diag i + j == x + y
        # all valid placement
        sols = []
        # current solution
        placed = []
        
        def is_valid(i, j):
            for (x, y) in placed:
                if i == x or j == y or i - j == x - y or i + j == x + y:
                    return False
            return True

        def dfs(i):
            if i == n:
                sols.append(placed.copy())
                return
            for j in range(n):
                if is_valid(i, j):
                    placed.append((i, j))
                    dfs(i+1)
                    placed.pop()
        
        dfs(0)
        output = []
        for sol in sols:
            tmp = [['.']*n for _ in range(n)]
            for i, j in sol:
                tmp[i][j] = 'Q'
            output.append(["".join(row) for row in tmp])
        return output

def main():
    sol = Solution()
    print(sol.solveNQueens(4))

if __name__ == "__main__":
    main()