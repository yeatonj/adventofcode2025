import math

if __name__ == "__main__":
    f = 'data_test.txt'
    f = 'data.txt'
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


    # Traverse perimeters, if we cross them in our rectangle then not acceptable
    # Need to create an 'inside' and 'outside' perimeter

    # Start at one corner and build from there, then pick the other corner and do the same

    # (0, 0) at top left
    # option 1: _|  ((r - 0.1, c - 0.1) and (r + 0.1, c + 0.1))
    # option 2: -i  ((r + 0.1, c - 0.1) and (r - 0.1, c + 0.1))
    # option 3: |_  ((r + 0.1, c - 0.1) and (r - 0.1, c + 0.1))
    # option 4: i-  ((r - 0.1, c - 0.1) and (r + 0.1, c + 0.1))
    

    # returns the coords of the two outside/inside
    def find_offset_corner_coords(pt1, pt2, pt3):
        # Ensure that we're going 'left to right'
        if (pt1[1] > pt3[1]):
            (pt1, pt3) = (pt3, pt1)
        # Case 1: horizontal first line (row pt1 == row pt2)
        if (pt1[0] == pt2[0]):
            # Case 1a: second line up
            if (pt2[0] > pt3[0]):
                return [(pt2[0] - 0.1, pt2[1] - 0.1), (pt2[0] + 0.1, pt2[1] + 0.1)]
            # Case 1b: second line down
            else:
                return [(pt2[0] + 0.1, pt2[1] - 0.1), (pt2[0] - 0.1, pt2[1] + 0.1)]
        # Case 2: vertical first line (col pt1 == col pt2)
        else:
            # Case 2a: first line up
            if (pt1[0] < pt2[0]):
                return [(pt2[0] + 0.1, pt2[1] - 0.1), (pt2[0] - 0.1, pt2[1] + 0.1)]
            # Case 2b: first line down
            else:
                return [(pt2[0] - 0.1, pt2[1] - 0.1), (pt2[0] + 0.1, pt2[1] + 0.1)]
            
    def calc_perimeter(perim_coords):
        cur_perim = 0
        seg_lengths = []
        for i in range(len(perim_coords)):
            cur = perim_coords[i]
            next = perim_coords[(i + 1) % len(perim_coords)]
            cur_perim += abs(next[0] - cur[0] + next[1] - cur[1])
            seg_lengths.append(abs(next[0] - cur[0] + next[1] - cur[1]))
        return cur_perim
            
    
    # Find the initial two possiblities for corners, pick one to traverse first
    starts = find_offset_corner_coords(coords[-1], coords[0], coords[1])

    perimeter_coords = [[], []]
    perimeters = []
    for i in range(len(starts)):
        # set current coordinate to starting coordinate
        cur_coord = starts[i]
        perimeter_coords[i].append(cur_coord)
        for j in range(1, len(coords)):
            possible_nexts = find_offset_corner_coords(coords[j - 1], coords[j], coords[(j + 1) % len(coords)])
            # One of the coordinates should match, take that one as the 'current' coordinate and add it
            for possible_next in possible_nexts:
                if (math.isclose(cur_coord[0], possible_next[0]) or math.isclose(cur_coord[1], possible_next[1])):
                    cur_coord = possible_next
                    perimeter_coords[i].append(cur_coord)
        # Calculate perimeter
        perimeters.append(calc_perimeter(perimeter_coords[i]))
    # keep higher of the two
    if (perimeters[0] < perimeters[1]):
        outer_perimeter = perimeter_coords[1]
    else:
        outer_perimeter = perimeter_coords[0]

    # we can't 'cross' the perimeter.
    def segments_intersect(rec_1_coord, rec_2_coord, perim_1_coord, perim_2_coord):
        # true if intersect, else false
        x1 = rec_1_coord[1]
        x2 = rec_2_coord[1]
        x3 = perim_1_coord[1]
        x4 = perim_2_coord[1]
        y1 = rec_1_coord[0]
        y2 = rec_2_coord[0]
        y3 = perim_1_coord[0]
        y4 = perim_2_coord[0]

        den = (x1 - x2) * (y3 - y4) - ((y1 - y2) * (x3 - x4))
        if (math.isclose(den, 0)):
            return False

        t_num = (x1 - x3) * (y3 - y4) - ((y1 - y3) * (x3 - x4))

        u_num = -1 * ((x1 - x2) * (y1 - y3) - ((y1 - y2) * (x1 - x3)))
        t = t_num / den
        u = u_num / den
        if ((t <= 1) and (u <= 1) and (t >= 0) and (u >= 0)):
            return True
        return False


    max = 0
    for i in range(len(coords) - 1):
        for j in range(i, len(coords)):
            area = calc_area(coords[i], coords[j])
            if (area > max):
                # Need to check for intersections
                # Find the four lines that make it up
                segments = [[coords[i],[coords[i][0], coords[j][1]]],
                            [coords[i],[coords[j][0], coords[i][1]]],
                            [[coords[i][0], coords[j][1]],coords[j]],
                            [[coords[j][0], coords[i][1]],coords[j]]]
                intersects = False
                for segment in segments:
                    # Check intersection with all of the pairs of perimeter segments
                    for k in range(len(outer_perimeter)):
                        if (segments_intersect(segment[0], segment[1], outer_perimeter[k], outer_perimeter[(k + 1) % len(outer_perimeter)])):
                            # print(segment[0], segment[1], outer_perimeter[k], outer_perimeter[(k + 1) % len(outer_perimeter)])
                            intersects = True
                            break
                    if (intersects):
                        break
                if (not intersects):
                    max = area
    print(max)
