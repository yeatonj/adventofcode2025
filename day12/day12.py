if __name__ == "__main__":
    shape_in = open('shapes.txt')
    area_in = open('areas.txt')

    tile_counter = 0
    present_tile_counts = []
    for line in shape_in:
        if ':' in line:
            present_tile_counts.append(tile_counter)
            tile_counter = 0
        else:
            for c in line:
                if c == '#':
                    tile_counter += 1
    present_tile_counts.append(tile_counter)

    present_tile_counts = present_tile_counts[1:]

    present_areas = []
    for line in area_in:
        temp = []
        line = line.strip()
        line = line.split(': ')
        temp.append([int(x) for x in line[0].split('x')])
        temp.append([int(x) for x in line[1].split(' ')])
        present_areas.append(temp)

    good_areas = 0
    for present_area in present_areas:
        total_area = present_area[0][0] * present_area[0][1]
        total_present_area = 9 * sum(present_area[1])
        if total_present_area <= total_area:
            good_areas += 1
        else:
            min_present_area = 0
            for i in range(len(present_tile_counts)):
                min_present_area += present_tile_counts[i] * present_area[1][i]
            if min_present_area < total_area:
                print('Gonna need something more complex')
    print(good_areas)

    # 546 is wrong
