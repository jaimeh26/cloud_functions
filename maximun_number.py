# Create a Cloud Function that finds the maximum number in a list(the list can be initialized inside the cloud function) this is the list-->[4434,1233,7987,4567,3123,4356,9808,1211,7888,9328]

def find_max_number(request):
    # List of numbers
    numbers = [4434, 1233, 7987, 4567, 3123, 4356, 9808, 1211, 7888, 9328]

    # Find maximum number
    max_number = max(numbers)

    return {'max_number': max_number}

# Trigger URL https://us-central1-certain-beach-391616.cloudfunctions.net/maximum_number
