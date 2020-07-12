def saddle_points(matrix):
    if not is_valid_matrix(matrix):
        raise ValueError("Irregular matrix")

    saddles = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if is_max_column(row, column, matrix) and is_min_row(row, column, matrix):
                saddles.append({"row": row + 1, "column": column + 1})
    return saddles


def is_valid_matrix(matrix):
    return all([len(matrix[0]) == len(matrix[x]) for x in range(len(matrix))])


def is_max_column(row, column, matrix):
    return matrix[row][column] == max(matrix[row])


def is_min_row(row, column, matrix):
    return matrix[row][column] == min(matrix[row][column] for row in range(len(matrix)))
