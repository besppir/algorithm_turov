import string

with open('LICENSE_PYTHON.txt') as f:
    text_init = f.read()

lowered_text = text_init.lower()
spaces = " " * len(string.punctuation)
clean_text = lowered_text.translate(str.maketrans(string.punctuation, spaces))
words = clean_text.split()

words_count = {}
for word in words:
    words_count[word] = words_count.get(word, 0) + 1 #вместо words_count[word] = words.count(word)

top_10 = sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:10]  #как отсортировать словарь

for word, count in top_10:
    print(f"{word}: {count}")