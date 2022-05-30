from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_reponses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_reponses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)

# plt.ylabel("Programming languages")
plt.title("Most Popular Languages")
plt.xlabel("Number of people who use")

plt.tight_layout()

plt.show()