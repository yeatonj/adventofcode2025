if __name__ == "__main__":
    f = 'data_test.txt'
    f = 'data.txt'
    input_data = open(f)

    data = {}

    row = 0
    for l in input_data:
        l = l.strip()
        col = 0
        for c in l:
            data[(row, col)] = c
            col += 1
        row += 1

    flow = {}
    for c in range(col):
        if (data[(0,c)] == 'S'):
            flow[(1, c)] = '|'
        else:
            flow[(1, c)] = data[(0,c)]
    
    splits = 0
    for r in range(2, row):
        for c in range(col):
            if (flow[(r - 1, c)] == '|'):
                if (data[(r,c)] == '^'):
                    splits += 1
                    flow[(r, c - 1)] = '|'
                    flow[(r, c + 1)] = '|'
                    if (r, c) in flow:
                        continue
                    else:
                        if (r, c) in flow:
                            continue
                        flow[(r, c)] = data[(r, c)]
                else:
                    if (r, c) in flow:
                        continue
                    flow[(r, c)] = '|'
            else:
                if (r, c) in flow:
                    continue
                flow[(r, c)] = data[(r,c)]
    print(splits)

    # pt 2, bfs this
    for i in range(col):
        if flow[(1,i)] == '|':
            start = (1,i)
            break

    paths_dic = {}
    def dfs(cur, flow, memo_dic):
        if (cur in memo_dic):
            return memo_dic[cur]
        elif (cur[0] + 1, cur[1]) not in flow:
            memo_dic[cur] = 1
            return 1
        # Check below
        elif flow[(cur[0] + 1, cur[1])] == '|':
            memo_dic[cur] = dfs((cur[0] + 1, cur[1]), flow, memo_dic)
            return memo_dic[cur]
        else:
            # check left
            left = dfs((cur[0] + 1, cur[1] - 1), flow, memo_dic)
            # check right
            right = dfs((cur[0] + 1, cur[1] + 1), flow, memo_dic)
            memo_dic[cur] = left + right
            return left + right
    
    print(dfs(start, flow, paths_dic))





    # for r in range(1, row):
    #     for c in range(col):
    #         print(flow[(r,c)], end='')
    #     print()
        