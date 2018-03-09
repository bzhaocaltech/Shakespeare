import pickle

# This file doesn't have sonnet 99 or 126
file = open("data/shakespeare_edited.txt", 'r')
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

# Create the rhyme dictionary
rhyme_dict = {}
stanza_lengths = [4, 4, 4, 2]
stanza_num = 0
line_in_stanza = 0
for line_num, line in enumerate(line_data):
    # Move onto the next stanza
    if line_in_stanza == stanza_lengths[stanza_num]:
        stanza_num += 1
        if stanza_num == 4:
            stanza_num = 0
        line_in_stanza = 0
    # Find the last word of this stanza
    last_word = line[-1]
    if not last_word[-1].isalpha():
        last_word = last_word[:-1]
    # Find the corresponding rhyming word
    corresponding_word = -1
    if stanza_lengths[stanza_num] == 4 and line_in_stanza <= 1:
        corresponding_word = line_data[line_num + 2][-1]
    if stanza_lengths[stanza_num] == 4 and line_in_stanza >= 2:
        corresponding_word = line_data[line_num - 2][-1]
    if stanza_lengths[stanza_num] == 2 and line_in_stanza == 0:
        corresponding_word = line_data[line_num + 1][-1]
    if stanza_lengths[stanza_num] == 2 and line_in_stanza == 1:
        corresponding_word = line_data[line_num - 1][-1]
    if not corresponding_word[-1].isalpha():
        corresponding_word = corresponding_word[:-1]
    # Add to rhyming dict
    if last_word not in rhyme_dict:
        rhyme_dict[last_word] = [corresponding_word]
    elif corresponding_word not in rhyme_dict[last_word]:
        rhyme_dict[last_word].append(corresponding_word)
    # Move to the next line in the stanza
    line_in_stanza += 1

pickle.dump(rhyme_dict, open("data/rhyme_dict.p", 'wb'))

file.close()
