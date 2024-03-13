# Create a cloud function that finds the longest word out of the following list : ["abracadabra","pineapple","food","Daisy","mcit","Montrealcollegeinformationandtechnology"]

def find_longest_word(request):
    # List of words
    words = ["abracadabra", "pineapple", "food", "Daisy", "mcit", "Montrealcollegeinformationandtechnology"]

    # Find the longest word
    longest_word = max(words, key=len)

    return {'longest_word': longest_word}

# Trigger URL https://us-central1-certain-beach-391616.cloudfunctions.net/longest_word
