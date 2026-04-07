import math

def target_to_num(asci_target):
    tar = 0
    for i in range(len(asci_target)):
        if asci_target[i] == '#':
            tar += 2**i
    return tar

def button_list_to_bitwise_list(asci_button_list):
    buttons = asci_button_list.split(' ')
    bitwise_buttons = []
    for i in range(len(buttons)):
        button = buttons[i][1:-1].split(',')
        button = [int(x) for x in button]
        bitwise_buttons.append(asci_button_to_bitwise(button))
    return bitwise_buttons

def asci_button_to_bitwise(asci_button):
    button = 0
    for digit in asci_button:
        button += 2**digit
    return button

def find_min_pushes(target, buttons):
    shortest_presses = {}
    shortest_presses[0] = 0
    temp_queue = [0]
    current_presses = 0
    while (True):
        bfs_queue = temp_queue
        temp_queue = []
        for poss_target in bfs_queue:
            for button in buttons:
                pushed = poss_target ^ button
                if (pushed == target):
                    return current_presses + 1
                # otherwise, check if in dic
                if (pushed not in shortest_presses):
                    shortest_presses[pushed] = current_presses + 1
                    temp_queue.append(pushed)
        current_presses += 1



if __name__ == "__main__":
    f = 'data_test.txt'
    f = 'data.txt'
    input_data = open(f)

    machines = []

    for l in input_data:
        l = l.strip()
        cur_char = 0 
        while (l[cur_char] != ']'):
            cur_char += 1
        target = target_to_num(l[1:cur_char].strip())
        cur_char += 2
        button_start = cur_char
        while (l[cur_char] != '{'):
            cur_char += 1
        buttons = button_list_to_bitwise_list(l[button_start:cur_char].strip())
        joltage = l[cur_char + 1:-1].strip()
        joltage = [int(x) for x in joltage.split(',')]
        machines.append([target, buttons, joltage])

    # Now, we need to figure out an xor order of buttons with 0 that gets us to the target
    presses = 0
    for machine in machines:
        presses += find_min_pushes(machine[0], machine[1])

    print(presses)


    # Part 2 strategy:
    # To achieve a specific combo of lit lights, we push each button at most 1 time
    # We also know that a joltage has a specific combo of lights corresponding to it
    # Thus, each joltage is some combo of pushes, plus a whole bunch of pushes that result
    # in no lights (flipping them back and forth)
    # So, we find the 'odd' presses to get the combo in the joltage that get it to evens
    # Then divide by two any evens that are left
    # recurse until all are at zero
    # eg, {3, 5, 4, 7} is the pattern '##.#'
    # take current joltage, find odds and convert to binary ({1, 1, 0, 1})
    # -> {2, 2, 4, 6} -> {1, 1, 2, 3} -> {0, 0, 2, 2} -> {0, 0, 1, 1} -> {0, 0, 0, 0}

    # print(machines)

    def find_combos(target, buttons, memo_dic):
        if (target in memo_dic):
            return  memo_dic[target]
        # Build power series of all combos of buttons
        combos = []
        for i in range(2**len(buttons)):
            combo = []
            temp = 0
            for j in range(len(buttons)):
                if ((i >> j) & 1):
                    combo.append(j)
                    temp ^= buttons[j]
            # keep combo if it hits the target
            if (temp == target):
                combos.append(combo)
        memo_dic[target] = combos
        return combos

    def joltage_presses_recursive(buttons, joltages, joltage_dic, combo_dic):
        if (tuple(joltages) in joltage_dic):
            return joltage_dic[tuple(joltages)]
        # base case, return 0 if all joltages are 0 or inf if negative
        non_zero_joltage = False
        for joltage in joltages:
            if joltage > 0:
                non_zero_joltage = True
        if (not non_zero_joltage):
            joltage_dic[tuple(joltages)] = 0
            return 0
        
        # Find all combos to get us to a blank slate
        target = 0
        for i in range(len(joltages)):
            if (joltages[i] % 2 == 1):
                target += 2**i
        combos = find_combos(target, buttons, combo_dic)

        # Set our minimum presses to be infinite
        min_presses = math.inf
        
        # For each combo, find the new joltage and feed back in to the recursion
        for combo in combos:
            new_joltages = [jolt for jolt in joltages]

            negative = False
            for button_num in combo:
                button = buttons[button_num]
                # button is bitwise rep of button, need to subtract bits from each
                for i in range(len(new_joltages)):
                    if (button >> i & 1):
                        new_joltages[i] -= 1
                    # and floor divide by 2
                    if (new_joltages[i] < 0):
                        negative = True
            for i in range(len(new_joltages)):
                new_joltages[i] //= 2
            press_count = len(combo)
            if (negative):
                # don't feed back into recursion
                continue
            # calculate the presses for the new joltages plus old
            total_presses = (2 * joltage_presses_recursive(buttons, new_joltages, joltage_dic, combo_dic)) + press_count
            if (total_presses < min_presses):
                min_presses = total_presses
        joltage_dic[tuple(joltages)] = min_presses
        return min_presses
    
    min_presses = []
    for machine in machines:
        ans = joltage_presses_recursive(machine[1], machine[2], {}, {})
        min_presses.append(ans)
    print(sum(min_presses))