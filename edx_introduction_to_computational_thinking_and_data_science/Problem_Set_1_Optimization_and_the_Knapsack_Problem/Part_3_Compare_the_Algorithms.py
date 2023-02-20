def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    cows = load_cows("data_files/ps1_cow_data.txt")
    # default weight limits of 10
    limit = 10

    start = time.time()
    ## code to be timed
    number_brute = len(brute_force_cow_transport(cows, limit))
    end = time.time()
    duration_brute = end - start

    start = time.time()
    ## code to be timed
    number_greedy = len(greedy_cow_transport(cows, limit))
    end = time.time()
    duration_greedy = end - start

    print(f'Greedy {number_greedy} trips, {duration_greedy} \nBrute force {number_brute} trips, time {duration_brute}')
    print(f'greedy_cow_transport runs faster: {(duration_greedy - duration_brute) < 0},\nbrute_force_cow_transport returns better solution: {(number_brute - number_greedy) < 0}')

