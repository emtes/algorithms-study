def binary_search(lst, item):
    # define initial high and low
    low = 0
    high = len(lst) - 1

    # loop while low and high aren't the same
    while low <= high:
        # define a middle and guess by accessing list
        mid = (low + high) // 2
        guess = lst[mid]
        # did we guess correctly?
        if guess == item:
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

print(binary_search(sorted_list, 6))
print(binary_search(sorted_list, 67))
print(binary_search(sorted_list, 52))