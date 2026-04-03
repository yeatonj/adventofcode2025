import math

def dist(a, b):
    return (((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2))**0.5

if __name__ == "__main__":
    f = 'data_test.txt'
    ITERATIONS = 10
    f = 'data.txt'
    ITERATIONS = 2000
    input_data = open(f)

    # Create the distance matrix
    coords = []
    distances = []
    
    for line in input_data:
        line = line.strip().split(',')
        line = list(map(lambda x : int(x), line))
        coords.append(line)


    distances = []
    for i in range(len(coords)):
        temp = []
        for j in range(len(coords)):
            if j <= i:
                temp.append(math.inf)
            else:
                temp.append(dist(coords[i], coords[j]))
        distances.append(temp)

    set_counter = 0
    circuits = {}

    # for iter in range(ITERATIONS): # for part 1
    done = False
    while (not done): # for part 2
        # Find min index
        cur_min = math.inf
        min_ind = [0,0]
        for i in range(len(coords)):
            for j in range(len(coords)):
                if distances[i][j] < cur_min:
                    cur_min = distances[i][j]
                    min_ind = [i, j]
        
        # Assign to a set
        # Case 1, neither in set
        i = min_ind[0]
        j = min_ind[1]
        if (i not in circuits and j not in circuits):
            # Create a new circuit
            circuits[i] = set_counter
            circuits[j] = set_counter
            # iterate set counter
            set_counter += 1
        # Case 2, i not in set but j in set
        elif (i not in circuits and j in circuits):
            circuits[i] = circuits[j]
        # Case 3, j not in set but i in set
        elif (i in circuits and j not in circuits):
            circuits[j] = circuits[i]
        # Case 4, both in different sets
        elif (circuits[i] != circuits[j]):
            # assign all in j's to i's circuit
            consolidated_circuit = circuits[i]
            to_remove = circuits[j]
            for c in circuits:
                if circuits[c] == to_remove:
                    circuits[c] = consolidated_circuit
        # remove dist from dists
        distances[i][j] = math.inf
        # Check number of circuits
        circuit_sets = {}
        if (len(circuits) >= len(coords)):
            done = True
            for c in circuits:
                if circuits[c] not in circuit_sets:
                    circuit_sets[circuits[c]] = True
                if len(circuit_sets) > 1:
                    done = False
                    break

    print(coords[i][0] * coords[j][0])

    # Part 1
    # totals = {}
    # for c in circuits:
    #     if circuits[c] not in totals:
    #         totals[circuits[c]] = 1
    #     else:
    #         totals[circuits[c]] += 1
    
    # sizes = []
    # for t in totals:
    #     sizes.append(totals[t])
    # sizes.sort(reverse=True)
    # product = 1
    # for k in range(0,3):
    #     product *= sizes[k]
    # print(product)
        

            
    # # Print them?
    # for i in range(len(coords)):
    #     print(distances[i])