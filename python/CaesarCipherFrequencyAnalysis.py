import matplotlib.pyplot

# These are the letters we're interested in when dealing with frequency analysis
# WHITE SPACE IS THE MOST FREQUENT "LETTER" IN THE ENGLISH ALPHABET !!!
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# We count the occurences of the given characters
def frequency_analysis(text):
    text = text.upper()

    # we use a dictionary to store the letter-frequency pair
    letter_frequencies = {}

    # initialize the dictionary (of course with 0 frequencies)
    for letter in LETTERS:
        letter_frequencies[letter] = 0

    # Consider the text we want to analyse
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    matplotlib.pyplot.bar(frequencies.keys(), frequencies.values())
    matplotlib.pyplot.show()


if __name__ == "__name__":
    plain_text = "Shannon defined the quantity of information produced by a source for example, the quantity in a message by a formula similar to the equation that defines thermodynamic entropy in physics"
    freq = frequency_analysis(plain_text)
    plot_distribution(freq)
