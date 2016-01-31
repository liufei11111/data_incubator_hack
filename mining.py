import re
import matplotlib
matplotlib.use('Agg')
import json
import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages('/vagrant/minging.pdf')

# tweets_data_path = '/vagrant/twitter_data.txt'
tweets_data_path = '/vagrant/twitter_large_data.txt'
x_label_font = 6
size_of_fig = 100
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)

# print map(lambda tweet: tweet['text'], tweets_data)
print tweets_data[2]['text']
textArr = map(lambda tweet: tweet['text'], tweets_data)
langArr = map(lambda tweet: tweet['lang'], tweets_data)
countryArr = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets = pd.DataFrame({'text': textArr, 'country': countryArr, 'lang': langArr})

def word_in_text(words, text):
    words = map(lambda word: word.lower(), words)
    text = text.lower()
    match = False
    for aword in words:
    	match = match or re.search(aword, text)
    if match:
        return True
    return False
tweets['HillaryClinton'] = tweets['text'].apply(lambda tweet: word_in_text(['Hillary', 'Clinton'], tweet))
tweets['RockyDeLaFuente'] = tweets['text'].apply(lambda tweet: word_in_text(['Rocky' ,'Fuente'], tweet))
tweets['MartinOMalley'] = tweets['text'].apply(lambda tweet: word_in_text(['Martin','Malley'], tweet))
tweets['BernieSanders'] = tweets['text'].apply(lambda tweet: word_in_text(['Bernie','Sanders'], tweet))
tweets['DonaldTrumph'] = tweets['text'].apply(lambda tweet: word_in_text(['Donald','Trumph'], tweet))

# additional filter
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text(['president'], tweet))
print tweets['HillaryClinton'].value_counts()[True]
print tweets['RockyDeLaFuente'].value_counts()[True]
print tweets['MartinOMalley'].value_counts()[True]
print tweets['BernieSanders'].value_counts()[True]
print tweets['DonaldTrumph'].value_counts()[True]
print tweets['relevant'].value_counts()[True]
prg_langs = ['Hillary Clinton', 'Rocky De La Fuente', 'Martin O Malley','Bernie Sanders', 'Donald Trumph']
####
tweets_by_prg_lang = [tweets['HillaryClinton'].value_counts()[True], 
tweets['RockyDeLaFuente'].value_counts()[True], 
tweets['MartinOMalley'].value_counts()[True],
tweets['BernieSanders'].value_counts()[True],
tweets['DonaldTrumph'].value_counts()[True]
]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Hillary Clinton vs. Rocky De La Fuente vs. Martin O Malley vs Bernie Sanders vs Donald Trumph(Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
ax.tick_params(axis='x', labelsize=x_label_font)
fig.tight_layout()
plt.grid()
# plt.savefig(pp, format='pdf')
plt.savefig('raw_data_rank.png',format='png',dpi=size_of_fig)
####
# print tweets[tweets['relevant'] == True]
# print tweets[tweets['relevant'] == True]['RockyDeLaFuente'].value_counts()
def get_relevant_count(relevant_data_frame_value_counts):
	if len(relevant_data_frame_value_counts)<2:
		return 0
	else:
		return relevant_data_frame_value_counts[True]

tweets_by_prg_lang = [get_relevant_count(tweets[tweets['relevant'] == True]['HillaryClinton'].value_counts()), 
                      get_relevant_count(tweets[tweets['relevant'] == True]['RockyDeLaFuente'].value_counts()), 
                      get_relevant_count(tweets[tweets['relevant'] == True]['MartinOMalley'].value_counts()),
                      get_relevant_count(tweets[tweets['relevant'] == True]['BernieSanders'].value_counts()),
                      get_relevant_count(tweets[tweets['relevant'] == True]['DonaldTrumph'].value_counts())
                      ]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Hillary Clinton vs. Rocky De La Fuente vs. Martin O Malley vs Bernie Sanders vs Donald Trumph (Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
ax.tick_params(axis='x', labelsize=x_label_font)
fig.tight_layout()
plt.grid()
# plt.savefig(pp, format='pdf')
plt.savefig('relevant_data_rank.png',format='png',dpi=size_of_fig)
pp.close()
