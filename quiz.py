#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test
@File    ：quiz.py
@IDE     ：PyCharm
@Author  ：shiqinqin
@Date    ：2024/6/4 13:35
"""


def reverse_list(l: list):
    """
    TODO: 反转列表，不使用任何内置函数

    该函数应返回一个反转后的列表。
    输入l是一个可以包含任何类型数据的列表。
    """
    # 使用列表截取
    # return l[::-1]
    # 使用了 range 的情况下
    # return [l[i-1] for i in range(len(l), 0, -1)]
    # 不使用 range
    temp_l = [None] * len(l)
    index = len(l)
    for v in l:
        index -= 1
        temp_l[index] = v
    return temp_l


def solve_sudoku(matrix):
    """
    TODO: 编写一个程序来解决9x9的数独板。

    数独是史上最受欢迎的谜题游戏之一。数独的目标是在一个9×9的网格中填入数字，使得每一行、每一列和每一个3×3的小格子都包含1到9的所有数字。作为一个逻辑谜题，数独也是一项极好的大脑游戏。

    输入矩阵是一个9x9的矩阵。你需要编写一个程序来解决它。
    """
    # 设定结构为二元数组[[1,2,3,4,5,6,7,8,9], []...], 空的为None
    # 竖向列集合为
    column_list = [set() for _ in range(9)]
    # 九宫格集合为 grid_list
    grid_list = [set() for _ in range(9)]
    for i, j in enumerate(matrix):
        for x, y in enumerate(j):
            if y is not None:
                column_list[x].add(y)
                grid_index = get_grid_index(i, x)
                grid_list[grid_index].add(y)

    def guess_next(x, y):
        # 使用深度遍历
        flag = True
        # 获取下一个需要猜测的位置
        for i, j in enumerate(matrix[x:]):
            i += x
            if flag:
                flag = False
            else:
                y = 0
            for k, l in enumerate(j[y:]):

                k += y
                if l is None:
                    grid_index = get_grid_index(i, k)
                    for v in range(1, 10):  # 枚举猜测
                        if v in j or v in grid_list[grid_index] or v in column_list[k]:  # 合理性判断（列唯一，行唯一，宫格唯一）
                            continue
                        matrix[i][k] = v
                        grid_list[grid_index].add(v)
                        column_list[k].add(v)
                        if k == 8:
                            if i == 8:  # 猜测到最后一个返回成功
                                return True
                            result = guess_next(i + 1, 0)
                        else:

                            result = guess_next(i, k + 1)
                        if result is True:
                            return True
                        else:  # 清空猜测值
                            matrix[i][k] = None
                            grid_list[grid_index].remove(v)
                            column_list[k].remove(v)
                    else:
                        return False  # 猜测无法填充返回失败到上层


    guess_next(0, 0)  # 递归猜测
    return matrix


x_dict = {
    (0, 1, 2): {0, 1, 2},
    (3, 4, 5): {3, 4, 5},
    (6, 7, 8): {6, 7, 8}
}
y_dict = {
    (0, 1, 2): {0, 3, 6},
    (3, 4, 5): {1, 4, 7},
    (6, 7, 8): {2, 5, 8}
}


def get_grid_index(x, y):
    """
    获取九宫格位置
    0 1 2
    3 4 5
    6 7 8
    :param x:
    :param y:
    :return:
    """

    for i, j in x_dict.items():
        if x in i:
            for k, l in y_dict.items():
                if y in k:
                    return (j & l).pop()


if __name__ == '__main__':
    # print(reverse_list([1, 2, 3]))
    # print( solve_sudoku([[None]*9 for _ in range(9)]))
    # result = solve_sudoku([[None] * 9 for _ in range(9)])
    # for i in result:
    #     print(i)
    # input = [[None] * 9 for _ in range(9)]
    input = [
        [6, None, 5, None, None, None, None, None, None],
        [None, None, 8, None, None, 2, None, None, 6],
        [None, None, 9, None, None, 3, 5, 4, None],
        [None, 7, None, 3, None, None, None, None, None],
        [8, None, None, None, None, None, 7, None, None],
        [None, None, None, None, None, None, None, 9, 3],
        [3, None, 1, None, 8, 5, None, None, 9],
        [None, None, None, None, None, None, None, 6, None],
        [None, 2, 4, None, 1, 9, None, None, None]
    ]
    result = solve_sudoku(input)
    for i in result:
        print(i)