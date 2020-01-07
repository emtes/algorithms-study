def binary_search(lst, item):
    # define initial high and low
    low = 0
    high = len(lst) - 1
    ### lemme see steps for fun/stress testing
    step = 0

    # loop while low and high aren't the same element
    while low <= high:
        ####
        step += 1
        ####
        # define a middle and guess by accessing list
        mid = (low + high) // 2
        guess = lst[mid]
        # did we guess correctly?
        if guess == item:
            print(step)
            return mid

        # are we too low?
        if guess < item:
            # then new low must be at least one above our guess, numbered by mid
            low = mid + 1
        # or are we too high?
        else:
            # then new high must be at least one below our guess
            high = mid - 1
    # if we came down to one number and it wasn't correct, item must not be in list
    return None

# Testing
sorted_list = list(range(75))

binary_search(sorted_list, 6)
binary_search(sorted_list, 12)
binary_search(sorted_list, 11)