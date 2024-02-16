from typing import List
# nums=list[int]
class shudu_solution:
    def __init__(self, map: list[list[int]]) -> None:
        self.map = map
        self.m = len(map)
        self.n = len(map[0])
    
    def print_map(self) -> None:
        """打印数独"""
        for i in range(self.m):
            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in range(self.n):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.map[i][j], end=" ")
            print()
    
    def find_empty(self) -> tuple[int, int]:
        for i in range(self.m):
            for j in range(self.n):
                if self.map[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, num: int, pos: tuple[int, int]) -> bool:
        """判断是否合法"""
        # Check row
        for i in range(self.n):
            if self.map[pos[0]][i] == num and pos[1] != i:
                return False
        
        # Check column
        for i in range(self.m):
            if self.map[i][pos[1]] == num and pos[0] != i:
                return False
        
        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.map[i][j] == num and (i, j) != pos:
                    return False
        
        return True
    
    def solve(self) -> bool:
        """解数独"""
        find = self.find_empty()
        if find is None:
            return True
        else:
            row, col = find
        
        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.map[row][col] = i
                if self.solve():
                    return True
                self.map[row][col] = 0
        
        return False

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

xiaohe = shudu_solution(sudoku_board)
print("The map before solved:\n------------------------")
xiaohe.print_map()
if xiaohe.solve():
    print("The map after solved:\n----------------------")
    xiaohe.print_map()
else:
    print("No solution exists for the provided sudoku board.")