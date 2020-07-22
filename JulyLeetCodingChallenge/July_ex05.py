#(5) Word Search

result = ''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global result
        result = False
        check = [[0] * len(board[0]) for _ in range(len(board))]

        def dfs(x, y, idx, check, tmp, board, word):
            global result
            if result:
                return
            if tmp == word:
                result = True
                return
            N = len(board)
            M = len(board[N - 1])
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for a in range(4):
                tx, ty = x + d[a][0], y + d[a][1]
                if tx >= 0 and tx < N and ty >= 0 and ty < M:
                    if board[tx][ty] == word[len(tmp)] and not check[tx][ty]:
                        check[tx][ty] = 1
                        dfs(tx, ty, idx + 1, check, tmp + board[tx][ty], board, word)
                        check[tx][ty] = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    check[i][j] = 1
                    dfs(i, j, 0, check, board[i][j], board, word)
                    check[i][j] = 0
        return result

