def check_adjacent(schema: list[list[int]], row: int, col: int) -> bool:
    # check if we're in the top or bottom row

    top_row = schema[row - 1][col - 1 : col + 2] if row != 0 else ""
    bottom_row = schema[row + 1][col - 1 : col + 2] if row < len(schema) - 1 else ""
    left_right = []

    if col > 0:
        left_right.append(schema[row][col - 1])
    if col < len(schema[row]) - 1:
        left_right.append(schema[row][col + 1])
    for c in "".join([top_row, bottom_row, "".join(left_right)]):
        if not c.isalnum() and c != ".":
            # print(f"found a symbol: {c}")
            return True
    return False


def decode_schematic(schema: list[list[int]]) -> int:
    # Essentially we need to check every single element and all the elements surrounding it.
    # If a number has a symbol surrounding it, then we can add its value to the total sum

    schema_sum = 0

    for i in range(len(schema)):
        chars = []
        valid_number = False
        for right in range(len(schema[i])):
            if schema[i][right].isnumeric():
                chars.append(schema[i][right])
                valid_position = check_adjacent(schema, i, right)
                if not valid_number:
                    valid_number = valid_position
            else:
                if chars and valid_number:
                    print(int("".join(chars)))
                    schema_sum += int("".join(chars))
                chars = []
                valid_number = False
        if chars and valid_number:
            # print('END NUMBER:', "".join(chars))
            print("".join(chars))
            schema_sum += int("".join(chars))

    return schema_sum
    # check_adjacent(schema, i, j)


if __name__ == "__main__":
    with open("input_day3.txt", "r") as f:
        contents = [l.strip() for l in f]
        print('TOTAL SUM:', decode_schematic(contents))
