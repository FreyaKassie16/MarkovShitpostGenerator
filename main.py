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

# Example usage:
example_text = "The quick brown fox jumps over the lazy dog. The lazy dog barks loudly."
markov_chain = build_markov_chain(example_text)
generated_sentence = generate_sentence(markov_chain, length=8)
print(generated_sentence)
