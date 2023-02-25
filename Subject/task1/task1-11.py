from sortedcontainers import SortedSet


def min_elements(input_arr: [], n: int) -> []:
    new_arr = []
    st = SortedSet()
    for x in input_arr:
        st.add(x)

    for i in range(0, n):
        new_arr.append(st.pop(0))

    return new_arr


def read_from_file() -> (int, []):
    with open("input.txt", "r") as f:
        n = int(f.readline())
        values = [int(i) for i in f.readline().split(" ")]

    return n, values


def write_to_file(output_arr: []):
    with open("output.txt", "w") as f:
        for x in output_arr:
            f.write(str(x))
            f.write(" ")


def main():
    tmp = read_from_file()
    n = tmp[0]
    arr = tmp[1]
    arr = min_elements(arr, n)
    write_to_file(arr)


main()
