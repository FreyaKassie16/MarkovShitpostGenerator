import random

def build_markov_chain(text):
    words = text.split()
    markov_chain = {}
    prev_word = None

    for word in words:
        if prev_word is None:
            prev_word = word
            continue

        if prev_word not in markov_chain:
            markov_chain[prev_word] = []

        markov_chain[prev_word].append(word)
        prev_word = word

    return markov_chain

def generate_sentence(markov_chain, length=10, randomness_factor=0.2):
    if not markov_chain:
        return "Markov chain is empty."

    sentence = []
    current_word = random.choice(list(markov_chain.keys()))

    for _ in range(length):
        sentence.append(current_word)

        if current_word in markov_chain:
            next_words = markov_chain[current_word]
            current_word = random.choice(next_words)
        else:
            break

        # Introduce randomness occasionally
        if random.random() < randomness_factor:
            sentence.append(get_random_word())

    return ' '.join(sentence)

def get_random_word():
    # Define your list of "shitpost" words here
    shitpost_words = ["banana", "noodle", "gibberish", "flibbertigibbet", "kerfuffle", "brouhaha", "malarkey"]
    return random.choice(shitpost_words)

def get_user_input():
    return input("Enter a sentence or text: ")

def read_external_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    # Allow user to input text dynamically
    example_text = get_user_input()

    # Alternatively, you can read from an external dataset
    # example_text = read_external_dataset('external_dataset.txt')

    markov_chain = build_markov_chain(example_text)
    generated_sentence = generate_sentence(markov_chain, length=15)   # Increase the length for more variety
    print("Generated Sentence:", generated_sentence)
