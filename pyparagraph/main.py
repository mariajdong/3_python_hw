#import modules
import os
import re

#specify paragraph paths
p1path = "resources/paragraph_1.txt"
p2path = "resources/paragraph_2.txt"

#define fxn to use w/ both txt files
def paragraph_analysis (txt_path, output_path):
    
    #define variable to hold paragraph contents
    paragraph = ""

    #write contents of paragraph to a single line string variable
    with open (txt_path) as txt_file:
        paragraph = txt_file.read().replace("\n\n", " ")

    #split paragraph to list of words, count length
    word_list = paragraph.split (" ")
    word_count = len (word_list)

    #calculate average word length
    word_length = []

    for word in word_list:
        word_length.append (len(word))
    
    avg_word_length = sum (word_length) / len (word_length)

    #split paragraph to list of sentences, count length
    sentence_list = re.split("(?<=[.!?]) +", paragraph)
    sentence_count = len (sentence_list)
    
    #calculate average sentence length
    sentence_length = []

    for sentence in sentence_list:
        sentence_words = sentence.split (" ")
        sentence_length.append (len (sentence_words))
    
    avg_sentence_length = sum (sentence_length) / len (sentence_length)

    #define output for terminal and new txt file
    output = f"""paragraph analysis
-----------------------------
approximate word count: {word_count}
approximate sentence count: {sentence_count}
average letter count: {round (avg_word_length, 1)}
average sentence length: {round (avg_sentence_length, 1)}"""

    #print accordingly
    print (output)
    with open (output_path, 'w') as analysis:
        analysis.write (output)

output_path1 = "analysis/p1_analysis.txt"
output_path2 = "analysis/p2_analysis.txt"

paragraph_analysis (p1path, output_path1)
paragraph_analysis (p2path, output_path2)