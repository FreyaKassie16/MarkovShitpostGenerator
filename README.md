# MarkovShitpostGenerator

Generate delightfully random and occasionally nonsensical sentences using Markov Chains. This Python project leverages Markov Chain models to construct sentences based on input text, with a touch of "shitposting" for added humor and randomness.

## Features

- **Markov Chain Sentence Generation:** Construct sentences based on input text using a Markov Chain model.
- **Shitposting Element:** Introduce a dash of randomness and humor with occasional insertion of "shitpost" words.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/FreyaKassie16/MarkovShitpostGenerator.git
   cd MarkovShitpostGenerator
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run the Generator:**
   ```bash
   python main.py
4. **Customize**
   - Modify the **'example_text'** variable in **'main.py'** to use your own input text.
   - Adjust parameters in the **'generate_sentence'** function to control the length and randomness of generated sentences

## Example

```python
# Example usage:
example_text = "The quick brown fox jumps over the lazy dog. The lazy dog barks loudly."
markov_chain = build_markov_chain(example_text)
generated_sentence = generate_sentence(markov_chain, length=8)
print(generated_sentence)
```

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.
