txt = "good morning, I'm a very good boy".split()
freq = {}
max_count = 0
for word in txt:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
    if freq[word] > max_count:
        max_count = freq[word]

for word in freq:
    if freq[word] == max_count:
        print(f'{word} : {freq[word]}')

