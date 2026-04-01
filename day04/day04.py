def count_adj(r_coord, c_coord, map_dic):
    count = 0
    for r in range(r_coord - 1, r_coord + 2):
        for c in range(c_coord - 1, c_coord + 2):
            char = map_dic.get((r, c), '.')
            if (char == '@'):
                if (not (r == r_coord and c == c_coord)):
                    count += 1
    return count


if __name__ == "__main__":
    # f = 'data_test.txt'
    f = 'data.txt'
    input_data = open(f)

    warehouse = {}

    row = 0
    for line in input_data:
        line = line.strip()
        col = 0
        for c in line:
            warehouse[(row, col)] = c
            col += 1
        row += 1

    count = 0
    for c in range(col):
        for r in range(row):
            if ((warehouse[(r, c)] == '@') and (count_adj(r, c, warehouse) < 4)):
                count += 1
    print(count)

    # Part 2
    count = 0
    removed = 1
    while (removed > 0):
        temp_dic = {}
        removed = 0
        for c in range(col):
            for r in range(row):
                if ((warehouse[(r, c)] == '@') and (count_adj(r, c, warehouse) < 4)):
                    count += 1
                    removed += 1
                    temp_dic[(r,c)] = '.'
                else:
                    temp_dic[(r,c)] = warehouse[(r,c)]
        warehouse = temp_dic
        temp_dic = {}
    print(count)
