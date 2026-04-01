if __name__ == "__main__":
    # f = 'data_test.txt'
    f = 'data.txt'
    input_data = open(f)

    volts = []

    # Part 1
    for bank in input_data:
        bank = bank.strip()
        max = bank[0]
        max_ind = 0
        # iteration 1
        for ind in range(len(bank) - 1):
            if (bank[ind] > max):
                max = bank[ind]
                max_ind = ind
        max_2 = bank[max_ind + 1]
        max_ind_2 = max_ind + 1
        for ind in range(max_ind + 1, len(bank)):
            if (bank[ind] > max_2):
                max_2 = bank[ind]
                max_ind_2 = ind
        volts.append(int(max + max_2))

    print(sum(volts))
    input_data.close()

    # Part 2

    input_data = open(f)

    volts = []
    for bank in input_data:
        bank = bank.strip()
        max_ind = -1
        cur_num = ''
        for i in range(12):
            # find the largest number with at least 12 - (i + 1) digits behind it
            max_ind = max_ind + 1
            max = bank[max_ind]
            for ind in range(max_ind, len(bank) - (12 - (i + 1))):
                if (bank[ind] > max):
                    max = bank[ind]
                    max_ind = ind
            cur_num += max
        volts.append(int(cur_num))
    print(sum(volts))

        
