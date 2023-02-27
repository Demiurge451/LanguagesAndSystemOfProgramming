from collections import deque
from typing import Any
import re


def matrix_without_single_value_vector(arr: [[]]) -> [[]]:
    rows = init_dict_of_dicts(len(arr))
    columns = init_dict_of_dicts(len(arr[0]))

    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            cur = arr[i][j]

            if cur in rows[i]:
                rows[i][cur] += 1
            else:
                rows[i][cur] = 1

            if cur in columns[j]:
                columns[j][cur] += 1
            else:
                columns[j][cur] = 1

    del_single_value_vector(rows, columns)
    res = []
    for row in rows:
        cur = []
        for col in columns:
            cur.append(arr[row][col])
        res.append(cur)

    return res


def del_single_value_vector(rows: dict[int, dict[Any, Any]], columns: dict[int, dict[Any, Any]]):
    first_iteration = True
    del_rows_value = deque()
    del_col_value = deque()
    while first_iteration or (len(del_col_value) != 0 or len(del_rows_value) != 0):
        if first_iteration:
            for key in list(rows.keys()):
                if len(rows[key]) <= 1:
                    del_rows_value.append(next(iter(rows[key])))
                    del rows[key]

            for key in list(columns.keys()):
                if len(columns[key]) <= 1:
                    del_col_value.append(next(iter(columns[key])))
                    del columns[key]
            first_iteration = False
        else:
            del_column_or_row(rows, del_col_value, del_col_value)
            del_column_or_row(columns, del_rows_value, del_rows_value)


def del_column_or_row(vector: dict[int, dict[Any, Any]], del_value_cur: deque, del_value_next: deque):
    while len(del_value_cur) != 0:
        cur = del_value_cur.popleft()
        for key in list(vector.keys()):
            vector[key][cur] -= 1
            if vector[key][cur] == 0:
                del vector[key][cur]
            if len(vector[key]) <= 1:
                del_value_next.append(next(iter(vector[key])))
                del vector[key]


def new_matrix(arr: [[]], delete_rows: deque, delete_columns: deque) -> [[]]:
    set_of_delete_rows = set(delete_rows)
    set_of_delete_columns = set(delete_columns)

    matrix = []
    for i in range(0, len(arr)):
        if i in set_of_delete_rows:
            continue
        row = []
        for j in range(0, len(arr[0])):
            if j in set_of_delete_columns:
                continue
            row.append(arr[i][j])
        matrix.append(row)

    return matrix


def init_dict_of_dicts(size: int) -> dict[int, dict[Any, Any]]:
    dictionary = {}
    for i in range(0, size):
        dictionary[i] = {}

    return dictionary


def read_from_file() -> [[]]:
    with open("test1.txt", "r") as f:
        pattern = re.compile('\d+')
        matrix = []
        for s in f.readlines():
            match = re.findall(pattern, s)
            matrix.append(match)

    matrix = [[int(numeric_string) for numeric_string in row] for row in matrix]
    return matrix


def write_to_file(matrix: [[]]):
    with open("output.txt", "w") as f:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                f.write(str(matrix[i][j]))
                f.write(" ")
            f.write("\n")


def main():
    matrix = read_from_file()
    write_to_file(matrix_without_single_value_vector(matrix))

main()
