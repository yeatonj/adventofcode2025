def cust_compare(a, b):
    if (len(a) < len(b)):
        return -1
    elif (len(a) > len(b)):
        return 1
    elif (a < b):
        return -1
    elif (a == b):
        return 0
    return 1

def cust_increment(num_str):
    num = int(num_str)
    return str(num + 1)

if __name__ == "__main__":
    # input_data = open('data_test.txt')
    input_data = open('data.txt')

    ranges = input_data.readline()
    input_data.close()

    in_ranges = {}

    range_arr = ranges.split(',')

    for pt1_range in range_arr:
        endpoints = pt1_range.split('-')
        (low, high) = (endpoints[0], endpoints[1])

        # find start point
        if (len(low) % 2 == 1):
            cur_half = '1' + ('0' * (len(low) // 2))
        else:
            first_half = low[0:len(low) // 2]
            second_half = low[len(low) // 2:]
            if (cust_compare(first_half, second_half) < 0):
                cur_half = cust_increment(first_half)
            else:
                cur_half = first_half

        # Now, iterate through
        while (cust_compare(cur_half * 2, high) < 1):
            in_ranges[int(cur_half * 2)] = True
            cur_half = cust_increment(cur_half)

    sum = 0
    for num in in_ranges:
        sum += num
    print(sum)

    # Part 2

    in_ranges_2 = {}

    for pt2_range in range_arr:
        endpoints = pt2_range.split('-')
        (low, high) = (endpoints[0], endpoints[1])

        # start with one digit nums, then 2, then... up to length of number / 2

        # start point is 1 times number of digits 
        cur_check = '1'
        min_reps = len(low)
        # length of repeated string
        for check_len in range(1, len(high) // 2 + 1):
            ## possible number of repeats
            min_repeats = len(low) // check_len
            if (len(low) % check_len != 0):
                min_repeats += 1
            max_repeats = len(high) // check_len
            # Possible repeats to check
            if (min_repeats < 2):
                min_repeats += 1 # make sure we repeat at least once
            for num_repeats in range(min_repeats, max_repeats + 1):
                # Find start point
                cur_check = '1' + (check_len - 1) * '0'
                # Increment until above low number
                while (cust_compare(cur_check * num_repeats, low) < 0):
                    cur_check = cust_increment(cur_check)
                    # Break if too long
                    if (len(cur_check) > check_len):
                        break
                # Then, iterate through
                while (cust_compare(cur_check * num_repeats, high) < 1):
                    in_ranges_2[int(cur_check * num_repeats)] = True
                    cur_check = cust_increment(cur_check)
                    # Break if too long
                    if (len(cur_check) > check_len):
                        break

    # print(in_ranges_2)

    sum = 0
    for num in in_ranges_2:
        sum += num
    print(sum)

    # 31680314021 is too high



    


    