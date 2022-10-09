import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

words = []
with open("textfile.txt", "r") as f:
    for line in f:
        words.extend(line.split())

counts = Counter(words)
top5 = counts.most_common(5)
word_map =  {key:value for key, value in top5}

words = word_map.keys()
freq = word_map.values()

plt.bar(words, freq)
plt.title('Frequency chart')
plt.xlabel('Words')
plt.ylabel('Frequenct')
plt.show()