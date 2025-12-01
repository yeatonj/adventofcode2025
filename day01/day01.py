if __name__ == "__main__":
    # input_data = open('data_test.txt')
    input_data = open('data.txt')

    cur_pos = 50
    zeros = 0
    extra = 0

    ## Part 1

    # for line in input_data:
    #     line_trunc = line.strip()
    #     direction = line_trunc[0]
    #     rotation = int(line_trunc[1:])
    #     if (direction == 'L'):
    #         cur_pos -= rotation
    #     else:
    #         cur_pos += rotation
    #     cur_pos %= 100

    #     if (cur_pos == 0):
    #         zeros += 1

    # print(zeros)

    ## Part 2

    for line in input_data:
        line_trunc = line.strip()
        direction = line_trunc[0]
        rotation = int(line_trunc[1:])
        if (rotation >= 100):
            extra = rotation // 100
            rotation %= 100
        if (direction == 'L'):
            if (cur_pos == 0):
                # To account for 'extra' rotation due to mod math
                extra -= 1
            cur_pos -= rotation
        else:
            cur_pos += rotation

        if (cur_pos > 100 or cur_pos < 0):
            extra += 1
        cur_pos %= 100

        zeros += extra
        extra = 0

        if (cur_pos == 0):
            zeros += 1
        

    # 24130 is too high
    print(zeros)
    


    input_data.close()