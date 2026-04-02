if __name__ == "__main__":
    # f = 'data_test.txt'
    f = 'data.txt'
    input_data = open(f)

    ranges = []
    checks = []

    for line in input_data:
        line = line.strip()
        if '-' in line:
            line = line.split('-')
            ranges.append([int(line[0]), int(line[1])])
        elif line == '':
            continue
        else:
            checks.append(int(line))

    fresh = 0
    for check in checks:
        for r in ranges:
            if ((check >= r[0]) and (check <= r[1])):
                fresh += 1
                break
    print(fresh)

    # part 2
    ranges.sort()
    ranges_pt2 = [ranges[0]]
    
    for i in range(1, len(ranges)):
        # Case 1: bottom of both ranges are equal -> adjust range to keep range's high
        if (ranges[i][0] == ranges_pt2[-1][0]):
            ranges_pt2[-1][1] = ranges[i][1] if ranges[i][1] > ranges_pt2[-1][1] else ranges_pt2[-1][1]
        # Case 2: bottom of range is between the two -> adjust range to keep range's high
        elif ((ranges [i][0] > ranges_pt2[-1][0]) and (ranges[i][0] <= ranges_pt2[-1][1])):
            ranges_pt2[-1][1] = ranges[i][1] if ranges[i][1] > ranges_pt2[-1][1] else ranges_pt2[-1][1]
        # Case 3: bottom of range is outside the two -> append onto new ranges
        else:
            ranges_pt2.append(ranges[i])
    
    total = 0
    for r in ranges_pt2:
        total += (r[1] - r[0] + 1)
    print(total)
    