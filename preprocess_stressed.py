import pickle
import random

# import our syllables dictionary
syllable_dict = pickle.load(open("data/syllable_dict.p", "rb"))
line_data = pickle.load(open("data/line_data.p", "rb"))

# Create the stress/unstressed dictionary
stress_dict = {}
for line_num, line in enumerate(line_data):
    is_done = False
    tries = 0
    while not is_done:
        tries += 1
        # Current number of syllables in line
        line_syl_count = 0
        # To hold possible combination of syllables
        temp_dict = {}
        for word_num, word in enumerate(line):
            word = word.lower()

            # So we keep randomly choosing a possible syllable length until we get
            # that the whole line has 10 syllables. A little sketchy but works
            # ok. Can't actually gurantee correctness but hopefully get something
            # close to it
            num_syl = random.choice(syllable_dict[word])
            # Only allow E if word is at end of the line
            while num_syl[0] == 'E' and word_num != len(line) - 1:
                num_syl = random.choice(syllable_dict[word])

            if num_syl[0] == 'E' and word_num == len(line) - 1:
                num_syl = int(num_syl[1])
            num_syl = int(num_syl)

            # Add to temp dict
            if line_syl_count % 2 == 0:
                if word == 'lover':
                    print("hi")
                temp_dict[word + str(num_syl)] = 'u'
            else:
                if word == 'lover':
                    print("hi")
                temp_dict[word + str(num_syl)] = 's'

            line_syl_count += num_syl

        if line_syl_count == 10:
            is_done = True
            # Add temp dict to the stress_dict
            for key, value in temp_dict.items():
                # Can be both unstressed and stressed
                if key in stress_dict and value != stress_dict[key]:
                    stress_dict[key] = "us"
                else:
                    stress_dict[key] = value

        # Can't pin down the syllables in this line
        if tries > 100:
            print(line)
            print(line_num)
            is_done = True

pickle.dump(stress_dict, open("data/stress_dict.p", 'wb'))
