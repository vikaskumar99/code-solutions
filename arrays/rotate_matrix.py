"""

https://leetcode.com/problems/rotate-image/
"""

def rotate(self, matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix)):
        # print("i", matrix[i], i, self.show(matrix))
        for j in range(i, len(matrix)):
            # print("j", j, "item", matrix[i], matrix[i][j], matrix[j][i])
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # print("transpose", matrix)

    for i in range(len(matrix)):
        matrix[i] = list(reversed(matrix[i]))


def show(self, matrix):
    string = ""
    for i in range(len(matrix)):
        string += "\n"
        for j in range(len(matrix)):
            string += f"{matrix[i][j]} "
    return string