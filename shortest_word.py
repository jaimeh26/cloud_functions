# Create a cloud function that finds the shortest word out of the following list :["abracadabra","pineapple","food","Daisy","mcit","Montrealcollegeinformationandtechnology"]

def find_shortest_word(request):
    # List of words
    words = ["abracadabra", "pineapple", "food", "Daisy", "mcit", "Montrealcollegeinformationandtechnology"]

    # Find the shortest word
    shortest_word = min(words, key=len)

    return {'shortest_word': shortest_word}

# Trigger URL https://us-central1-certain-beach-391616.cloudfunctions.net/shortest_word
