open_file = open(r"C:\Users\User\Desktop\sentence.txt", "r")
sentence_list = open_file.read()
line_list = []
word_list = []
word_set = []
before = []
line_list = sentence_list.split("\n")
for i in range(len(line_list)):
    word_list.append(line_list[i].split(" "))
for i in range(len(word_list)):
    for j in range(len(word_list[i])):
        word_list[i][j] = word_list[i][j].upper()
        word_set.append(word_list[i][j])
for i in range(len(word_set)):
    if "." in word_set[i]:
        word_set[i] = word_set[i][0:len(word_set[i])-1]
if "" in word_set:
    word_set.remove("")
word_set = set(word_set)
word_set = list(word_set)
print("포함된 단어의 개수:", len(word_set))
print("포함된 단어:", word_set)