import pickle

# import our syllables dictionary
syllable_dict = pickle.load(open("data/syllable_dict.p", "rb"))

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

# Create the stress/unstressed dictionary
stress_dict = {}
stanza_lengths = [4, 4, 4, 2]
stanza_num = 0
line_in_stanza = 0
for line_num, line in enumerate(line_data):
    line_syl_count = 0        
    # Move onto the next stanza
    if line_in_stanza == stanza_lengths[stanza_num]:
        stanza_num += 1
        if stanza_num == 4:
            stanza_num = 0
        line_in_stanza = 0
    
    for word in line:
        word = word.lower()
        
        # for those weird cases
        if word == '\'this' or word == '\'thou' or word == 'none\'' or word == '\'had' or word == 'love\'' or word == '\'thus' or word == 'lords\'' or word == '\'truth' or word == '\'now' or word == 'eyes\'' or word == 'beds\'' or word == 'oaths\'':
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == 'excuse\'' or word == 'gracious' or word == 'seasons\'' or word == 'princes\'' or word == 'buried' or word == 'lovers\'' or word == 'others\'' or word == 'garments\'' or word == 'summers\'' or word == 'tyrants\'':
            line_syl_count += 2
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u', 's']
            else:
                stress_dict[word] = ['s', 'u']
            continue
        elif word == 'interest' or word == 'flattery' or word == 'intermixed\'' or word == 'mistress\'':
            line_syl_count += 3
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u', 's', 'u']
            else:
                stress_dict[word] = ['s', 'u', 's']
            continue     
        elif word == 'perpetual': 
            line_syl_count += 4
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u', 's', 'u', 's']
            else:
                stress_dict[word] = ['s', 'u', 's', 'u']
            continue     
        elif word == 'friend.\'':
            word = 'friend'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == 'doctor-like)':
            word = 'doctor-like'
            line_syl_count += 3
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u', 's', 'u']
            else:
                stress_dict[word] = ['s', 'u', 's']
            continue 
        elif word == 'perhaps)':
            word = 'perhaps'
            line_syl_count += 2
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u', 's']
            else:
                stress_dict[word] = ['s', 'u']
            continue
        elif word == 'love)':
            word = 'love'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == 'best,\'':
            word = 'best'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == '\'will\'' or word == '\'will.\'':
            word = 'will'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == '\'i':
            word = 'i'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == 'hate\'':
            word = 'hate'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == '\'not':
            word = 'hate'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        elif word == 'you\'':
            word = 'you'
            line_syl_count += 1
            if line_syl_count %2 == 0:
                stress_dict[word] = ['u']
            else:
                stress_dict[word] = ['s']
            continue
        
        num_syl = int(syllable_dict[word][-1])
        line_syl_count += num_syl
        
        if line_syl_count % 2 == 0:
            if num_syl == 1:
                stress_dict[word] = ['u']
            elif num_syl == 2:
                stress_dict[word] = ['u', 's']
            elif num_syl == 3:
                stress_dict[word] = ['u', 's', 'u']
            elif num_syl == 4:
                stress_dict[word] = ['u', 's', 'u', 's']
            # 5 is the max number of syllables
            elif num_syl == 5:
                stress_dict[word] = ['u', 's', 'u', 's', 'u'] 
                
                
        else:
            if num_syl == 1:
                stress_dict[word] = ['s']
            elif num_syl == 2:
                stress_dict[word] = ['s', 'u']
            elif num_syl == 3:
                stress_dict[word] = ['s', 'u', 's']
            elif num_syl == 4:
                stress_dict[word] = ['s', 'u', 's', 'u']
            # 5 is the max number of syllables
            elif num_syl == 5:
                stress_dict[word] = ['s', 'u', 's', 'u', 's'] 
        
       

pickle.dump(stress_dict, open("data/stress_dict.p", 'wb'))

file.close()
