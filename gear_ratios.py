def decode_schematic(schema: list[list[int]]) -> int:
    # Essentially we need to check every single element and all the elements surrounding it.
    # If a number has a symbol surrounding it, then we can add its value to the total sum

    schema_sum = 0

    for i in range(2):
        for j in range(len(schema[i])):
            symbol_found = False
            # check if we're in the top or bottom row
            top_row = schema[i-1][j-1:j+2]
            bottom_row = schema[i+1][j-1:j+2]
            left_right = []

            if j > 0:
                left_right.append(schema[i][j-1])
            if j < len(schema[i]) - 1:
                left_right.append(schema[i][j+1])
            for c in "".join([top_row, bottom_row, "".join(left_right)]):
                if not c.isalnum() and c != ".":
                    print(c)

if __name__ == "__main__":
    with open("input_day3.txt", "r") as f:
        contents = [l.strip() for l in f]
        decode_schematic(contents)
