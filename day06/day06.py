def do_math(operands, op):
    if op == '+':
        return sum(operands)
    else:
        prod = 1
        for num in operands:
            prod *= num
    return prod

if __name__ == "__main__":
    # f = 'data_test.txt'
    f = 'data.txt'
    input_data = open(f)

    nums = []
    ops = []

    for l in input_data:
        l = l.strip()
        l = l.split(' ')
        if '+' in l:
            l_new = [item for item in l if item != '']
            ops = l_new
        else:
            l_new = [int(item) for item in l if item != '']
            nums.append(l_new)

    total = 0
    for i in range(len(ops)):
        temp = []
        for j in range(len(nums)):
            temp.append(nums[j][i])
        total += do_math(temp, ops[i])
    print(total)

    # Pt 2

    data_pt2 = []
    input_data.close()
    input_data = open(f)
    for line in input_data:
        data_pt2.append(line[:-1])
    data_pt2 = data_pt2[:-1]

    transposed = []

    for i in range(len(data_pt2[0])):
        temp = ''
        for j in range(len(data_pt2)):
            temp += data_pt2[j][i]
        transposed.append(temp)

    
    transposed_nums = []
    temp = []
    for num in transposed:
        num = num.strip()
        if num == '':
            transposed_nums.append(temp)
            temp = []
            continue
        temp.append(int(num))
    transposed_nums.append(temp)

    total = 0
    for i in range(len(ops)):
        total += do_math(transposed_nums[i], ops[i])
    print(total)