import pickle

file = open("data/Syllable_dictionary.txt", "r")
raw_data = file.read().split('\n')

syllable_dict = {}
for word in raw_data:
    if word != '':
        temp = word.split(' ')
        syllable_dict[temp[0]] = temp[1:]

pickle.dump(syllable_dict, open("data/syllable_dict.p", "wb"))

file.close()
