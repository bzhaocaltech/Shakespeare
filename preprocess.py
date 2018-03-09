import copy
import pickle

# We will experiment with several different ways of preprocessing the data
file = open("data/shakespeare.txt", 'r')
raw_data = file.read().split('\n')

# Seperate poem into lines
line_data = []
for line in raw_data:
    line_split = line.split()
    # Discard lines that are just spaces
    if len(line_split) <= 1:
        pass
    # Discard lines
    elif line_split[2] == '':
        pass
    else:
        line_data.append(line_split)

# To be used later
punct_line_data = copy.deepcopy(line_data)

# Ignore punctuation completely
for line in line_data:
    for word_position, word in enumerate(line):
        if word[-1] == ',' or word[-1] == ':' or word[-1] == '.' or word[-1] == '?' \
        or word[-1] == '!' or word[-1] == ")" or word[-1] == ';':
            line[word_position] = word[:-1]
        if word[-1] == '\'' and not (word != 'th\'' or word != 't\''):
            line[word_position] = word[:-1]
        if word[0] == '(':
            line[word_position] = word[1:]
        if word[0] == '\'' and not (word != '\'gainst' or word != "\'greeing" or
        word != '\'scraped' or word != '\'tis' or word != '\'twixt'):
            line[word_position] = word[1:]

pickle.dump(line_data, open("data/line_data.p", 'wb'))

# Seperate the poem into stanzas
stanza_data = []
stanza_lengths = [4, 4, 4, 2]
current_stanza_num = 0
line_counter = 0
while line_counter < len(line_data):
    if current_stanza_num == 4:
        current_stanza_num = 0
    stanza_length = stanza_lengths[current_stanza_num]
    current_stanza = []
    # Sonnet 99 has 15 instead of 14 lines
    if line_data[line_counter][0] == "One" and line_data[line_counter][1] == "blushing":
        stanza_length = 5
    for i in range(stanza_length):
        current_stanza += line_data[line_counter]

        line_counter += 1
    stanza_data.append(current_stanza)
    current_stanza_num += 1

pickle.dump(stanza_data, open("data/stanza_data.p", 'wb'))

# Don't seperate poems. Each poem is a sequence
poem_data = []
line_counter = 0
while line_counter < len(line_data):
    current_poem = []
    # Sonnet 99 has 15 lines
    if len(poem_data) == 98:
        for i in range(15):
            current_poem += line_data[line_counter]
            line_counter += 1
    # Sonnet 126 has 12 lines
    if len(poem_data) == 125:
        for i in range(12):
            current_poem += line_data[line_counter]
            line_counter += 1
    else:
        for i in range(14):
            current_poem += line_data[line_counter]
            line_counter += 1

    poem_data.append(current_poem)

pickle.dump(poem_data, open("data/poem_data.p", 'wb'))

# Poem data but with punctuation and \n characters!
poem_data = []
line_counter = 0
while line_counter < len(punct_line_data):
    current_poem = []
    # Sonnet 99 has 15 lines
    if len(poem_data) == 98:
        for i in range(15):
            current_poem += punct_line_data[line_counter] + ['\n']
            line_counter += 1
    # Sonnet 126 has 12 lines
    if len(poem_data) == 125:
        for i in range(12):
            current_poem += punct_line_data[line_counter] + ['\n']
            line_counter += 1
    else:
        for i in range(14):
            current_poem += punct_line_data[line_counter] + ['\n']
            line_counter += 1

    poem_data.append(current_poem)

# Create a sequence of letters. Seperate by poem
letter_data = []
for poem in poem_data:
    curr_poem = []
    for word in poem:
        for letter in word.lower() + ' ':
            # Just make everything lower case
            curr_poem.append(letter)
    letter_data.append(curr_poem)

pickle.dump(letter_data, open("data/letter_data.p", "wb"))

file.close()
