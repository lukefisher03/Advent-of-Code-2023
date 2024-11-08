# 1abc2 -> 12
# pqr3stu8vwx -> 38
# a1b2c3d4e5f -> 15
# treb7uchet -> 77 | if there's only one number, double it
# oermfi42303492902m sdokgmroigm93049230rm 03f923429k 30k

# use a left and right pointer
# increment both one at a time towards each other
# If the pointers either pass each other or they're both digits then return
# if they pass, then there's only one number. return this number doubled.
# otherwise they're both digits and we can return the numbers concatenated.


def decode(s: str) -> str:
    # two pointers!
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isdigit():
            left += 1
        if not s[right].isdigit():
            right -= 1

        if s[left].isdigit() and s[right].isdigit():
            return s[left] + s[right]
    return s[left] + s[left]


def replace_words_with_numbers(s: str) -> str:
    # sliding window!
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    i = 0
    new_s = []

    last_match_len = 0
    last_match_index = -1
    s = s.strip()
    while i < len(s):
        found_match = False
        for k, v in numbers.items():
            word = s[i : i + len(k)]
            if word == k:
                new_s.append(str(v))
                found_match = True
                last_match_len = len(k)
                last_match_index = i
                break
        if not found_match and i > last_match_index + last_match_len - 1:
            new_s.append(s[i])
        i += 1

    return "".join(new_s)


if __name__ == "__main__":
    total_with_replacement = 0
    with open("input_day1.txt", "r") as f:
        line = f.readline()
        while line:
            l = replace_words_with_numbers(line)
            decoded = int(decode(l))
            print(line.strip(), l, decoded)
            total_with_replacement += decoded
            line = f.readline()
        print("total:", total_with_replacement)
