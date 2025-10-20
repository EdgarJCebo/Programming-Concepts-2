#Using the code in Section 7.4, write a program that will allow me to enter a paragraph, including sentences which begin
#with numbers. Display each individual sentence and the count of sentences in the paragraph.
#You should have at least two functions, but you could have more.

import re

def split_sentences(paragraph):

#This splits the paragraph into individual sentences using regex.

#This pattern splits on punctuation followed by whitespace and either a capital letter or a digit
    pattern = r'(?<=[.!?])\s+(?=[A-Z0-9])'
    sentences = re.split(pattern, paragraph.strip())
    return sentences

def display_results(sentences):

#This displays each sentence and the total count for it.
    print("\n--- Sentences Found ---")
    for idx, sentence in enumerate(sentences, 1):
        print(f"{idx}. {sentence.strip()}")
    print(f"\nTotal number of sentences: {len(sentences)}")

def main():

#Main function to get user input and process it.
    paragraph = input("Please enter a paragraph (sentences can begin with numbers): \n")
    sentences = split_sentences(paragraph)
    display_results(sentences)

if __name__ == "__main__":
    main()
