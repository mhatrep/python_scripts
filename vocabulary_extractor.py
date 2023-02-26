import os
import re
import string
import nltk
from nltk.corpus import words

# set up the path for the input and output files
input_path = 'c:/Data/words/myfile.txt'
output_path = 'c:/Data/words/output.txt'

# define the set of stop words
stop_words = set(nltk.corpus.stopwords.words('english'))

# define a regex pattern to match words
word_pattern = re.compile(r'\b\w+\b')

# define a regex pattern to match hyphenated words
hyphenated_word_pattern = re.compile(r'\b\w+(?:-\w+)+\b')

# load the set of English words from the NLTK corpus
english_words = set(words.words())

# create an empty set to store unique English vocabulary
unique_vocabulary = set()

# open the input file in utf-8 encoding
with open(input_path, 'r', encoding='utf-8') as input_file:
    # read the contents of the file
    contents = input_file.read()
    # find all words and hyphenated words in the contents
    all_words = word_pattern.findall(contents)
    hyphenated_words = hyphenated_word_pattern.findall(contents)
    # combine the lists of words and hyphenated words
    all_words += hyphenated_words
    # iterate over the words
    for word in all_words:
        # convert the word to lowercase
        word = word.lower()
        # exclude words that contain non-alphabetic characters or are stop words or numbers
        if not word.isalpha() or word in stop_words or word.isnumeric():
            continue
        # exclude words that are not American English dictionary words
        if word not in english_words:
            continue
        # add the word to the set of unique vocabulary
        unique_vocabulary.add(word)

# sort the unique vocabulary by descending length
sorted_vocabulary = sorted(unique_vocabulary, key=len, reverse=True)

# open the output file in utf-8 encoding and append the sorted vocabulary
with open(output_path, 'a', encoding='utf-8') as output_file:
    for word in sorted_vocabulary:
        # only include words with length greater than or equal to 3
        if len(word) >= 3:
            # write the word to the output file on a new line
            output_file.write(word + '\n')
