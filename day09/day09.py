if __name__ == "__main__":
    f = 'data_test.txt'
    # f = 'data.txt'
    input_data = open(f)

    coords = []

    for l in input_data:
        l = l.strip()
        l = [int(x) for x in l.split(',')]
        coords.append(l)

    def calc_area(c1, c2):
        length = abs(c2[1] - c1[1]) + 1
        width = abs(c2[0] - c1[0]) + 1
        return length * width
    
    max = 0
    for i in range(len(coords) - 1):
        for j in range(i, len(coords)):
            area = calc_area(coords[i], coords[j])
            if (area > max):
                max = area

    print(max)


    # Traverse perimeters, if there are any tiles that aren't green/red in them then not OK
    # ASsume corners
    
    perimeter_tiles = {}

    def add_to_perimeter(p_tiles, start, end):
        if (start[0] == end[0]):
            # on same row
            if (end[1] > start[1]):
                for i in range(start[1], end[1] + 1):
                    p_tiles[(start[0], i)] = True
            else:
                for i in range(end[1], start[1] + 1):
                    p_tiles[(start[0], i)] = True
        else:
            # on same column
            if (end[0] > start[0]):
                for i in range(start[0], end[0] + 1):
                    p_tiles[(i, start[1])] = True
            else:
                for i in range(end[0], start[0] + 1):
                    p_tiles[(i, start[1])] = True

    # map of green tiles
    for i in range(len(coords)):
        add_to_perimeter(perimeter_tiles, coords[i], coords[(i + 1) % len(coords)])
        print(perimeter_tiles)

    # we can't 'cross' the perimeter. 

    # Find first 

    max = 0
    for i in range(len(coords) - 1):
        for j in range(i, len(coords)):
            area = calc_area(coords[i], coords[j])
            if (area > max):
                # Check perimeter
                max = area