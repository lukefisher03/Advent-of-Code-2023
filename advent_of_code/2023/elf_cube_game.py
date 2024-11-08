# Sample line of input:
#    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red


def parse_line(s: str) -> list[int]:
    s = s.strip()  # just to double check
    output = []
    rounds = []
    label, content = s.split(":")
    output.append(int(label[5:]))
    for round in content.split(";"):
        entries = round.split(",")
        vals = [0] * 3  # [red, green, blue]
        for entry in entries:
            n, color = entry.strip().split(" ")
            match color:
                case "red":
                    vals[0] = int(n)
                case "green":
                    vals[1] = int(n)
                case "blue":
                    vals[2] = int(n)
        rounds.append(vals)
    output.append(rounds)
    return output


def is_possible_game(game: list) -> int:
    """
    -1 means game is impossible
    """
    max_vals = [12, 13, 14]
    for round in game[1]:
        for val, max_val in zip(round, max_vals):
            if val > max_val:
                return -1
    return game[0]


def create_possible_game(game: list) -> int:
    """
    returns the multiplication of all 3 colors maximum values
    """
    # -1 won't change the absolute value so it doesn't matter if we multiply by it
    max_vals = [-1, -1, -1]
    for round in game[1]:
        for i, n in enumerate(round):
            # only change the number if it's greater than 0 so we don't mess up the total power
            if n > 0 and n > max_vals[i]:
                max_vals[i] = n

    return abs(max_vals[0] * max_vals[1] * max_vals[2])


if __name__ == "__main__":
    with open("input_day2.txt", "r") as f:
        line = f.readline().strip()
        total_id_count = 0
        total_power = 0
        while line:
            print(line)
            parsed_line = parse_line(line)
            is_possible_game_id = is_possible_game(parsed_line)
            possible_game_power = create_possible_game(parsed_line)
            total_id_count += is_possible_game_id if is_possible_game_id > -1 else 0
            total_power += possible_game_power
            line = f.readline().strip()
        print(total_id_count)
        print(total_power)
