import pandas as pd

words = []
with open('test.txt', 'r') as f:
    for line in f:
        words.extend(line.split())

for word in words:
    if '.jpg' in word:
        words.remove(word)

object = list(set(words))

count = []
for word in object:
    count.append(words.count(word))

d = {'object': object, 'count': count}
df = pd.DataFrame(data=d)
print(df)