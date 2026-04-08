if __name__ == "__main__":
    f = 'data_test.txt'
    f = 'data.txt'
    input_data = open(f)

    connections = {}

    for line in input_data:
        line = line.strip()
        line = line.split(': ')
        links = line[1].split(' ')

        connections[line[0]] = []

        for link in links:
            connections[line[0]].append(link)


    def dfs_count(current, visited, nodes, goal, memo_dic):
        if (current in memo_dic):
            return memo_dic[current]
        # If we are goal, return 1
        if (current == goal):
            return 1
        # add ourselves to visited
        visited[current] = True
        # visit adjacent nodes
        total_visited = 0
        if (current not in nodes):
            return 0
        for adj_node in nodes[current]:
            if adj_node in visited:
                continue
            else:
                total_visited += dfs_count(adj_node, visited, nodes, goal, memo_dic)
        visited.pop(current)
        memo_dic[current] = total_visited
        return total_visited
    
    print(dfs_count('you', {}, connections, 'out', {}))

    fft_first = dfs_count('svr', {}, connections, 'fft', {}) * dfs_count('fft', {}, connections, 'dac', {}) * dfs_count('dac', {}, connections, 'out', {})
    
    dac_first = dfs_count('svr', {}, connections, 'dac', {}) * dfs_count('dac', {}, connections, 'fft', {}) * dfs_count('fft', {}, connections, 'out', {})

    print(fft_first + dac_first)