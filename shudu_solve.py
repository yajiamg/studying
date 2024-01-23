def print_sudoku(board):#其实这一部分代码的核心就是在两层循环之中，在打印具体的数字之前，如果行是三的倍数，就打印一条横线，如果列是三的倍数，就打印一条竖线，这样就可以打印出数独的布局了。
    """打印数独布局的函数"""
    for i in range(len(board)):
        if i %3==0 and i!=0:
            print("---------------------")
        for k in range(len(board[0])):
            if k%3 == 0 and k!=0:
                print("|",end="")
            if k == 8:
                print(board[i][k])
            else:
                print(str(board[i][k])+" ",end="")
def find_empty(board):
    """找到数独板上空白位置的函数（用0表示）"""
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # 行, 列
    return None

def is_valid(board, num, pos):
    """检查放置的数字是否有效的函数"""
    # 检查行
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # 检查列
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # 检查3x3格子
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    """使用回溯算法解数独的函数"""
    find = find_empty(board)
    if not find:
        return True  # 如果没有空位，数独已解决
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # 回溯，重置格子

    return False  # 触发回溯

# 数独问题布局
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("原始数独布局:")
print_sudoku(sudoku_board)
print(print_sudoku.__doc__)
# if solve_sudoku(sudoku_board):
#     print("\n解决后的数独布局:")
#     print_sudoku(sudoku_board)
# else:
#     print("无解")