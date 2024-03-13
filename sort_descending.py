# Create cloud function that sorts the above list in descending order [4434,1233,7987,4567,3123,4356,9808,1211,7888,9328]

def sort_list_descending(request):
    # List of numbers
    numbers = [4434, 1233, 7987, 4567, 3123, 4356, 9808, 1211, 7888, 9328]

    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    return {'sorted_numbers': sorted_numbers}
