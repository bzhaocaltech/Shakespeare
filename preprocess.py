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

# To be used later (maybe?)
punct_line_data = copy.deepcopy(line_data)

# Ignore punctuation completely
for line in line_data:
    for word_position, word in enumerate(line):
        if ',' in word or ':' in word or '.' in word or '?' in word:
            line[word_position] = word[:-1]

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
    for i in range(stanza_length):
        current_stanza += line_data[line_counter]
        print(current_stanza)
        line_counter += 1
    stanza_data.append(current_stanza)
    current_stanza_num += 1

for stanza in stanza_data:
    print(stanza)

file.close()
