word_dic = {'pig':'animal', 'dollar':'currency', 'Tokyo': "Japan's capital",
            'computer':'tool', 'git':'software'}

print("pig: " + word_dic["pig"])
print("dollar: " + word_dic["dollar"])
print("Tokyo: " + word_dic["Tokyo"])
print("computer: " + word_dic["computer"])
print("git: " + word_dic["git"])

word_dic['list'] = 'built-in method'
word_dic['set'] = 'bulit-in method'
word_dic['if'] = 'built-in statement'
word_dic['for'] = 'built-in statement'
word_dic['dic'] = 'dictionary'

for word in word_dic.keys():
    print(word + ": " + word_dic[word])

for word in word_dic:
    print(word + ": " + word_dic[word])
