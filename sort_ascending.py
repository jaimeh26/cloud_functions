# Create cloud function that sorts the list in ascending order [4434,1233,7987,4567,3123,4356,9808,1211,7888,9328]

def sort_list_ascending(request):
    # List of numbers
    numbers = [4434, 1233, 7987, 4567, 3123, 4356, 9808, 1211, 7888, 9328]

    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)

    return {'sorted_numbers': sorted_numbers}

# Trigger URL https://us-central1-certain-beach-391616.cloudfunctions.net/sort
