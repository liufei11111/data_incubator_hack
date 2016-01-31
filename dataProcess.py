import matplotlib
matplotlib.use('Agg')
import json
import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages('/vagrant/multipage.pdf')

# tweets_data_path = '/vagrant/twitter_data.txt'
tweets_data_path = '/vagrant/twitter_large_data.txt'
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
## For language
tweets_by_lang = tweets['lang'].value_counts()
# create fig
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')

fig.patch.set_alpha(0.5)
ax = fig.add_subplot(111)
ax.patch.set_alpha(0.5)
ax.set_xlabel('volts', alpha=0.5)

tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
# save 
# fig = plt.figure()

plt.savefig(pp, format='pdf')

## For country
tweets_by_country = tweets['country'].value_counts()
# create fig
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')

fig.patch.set_alpha(0.5)
ax = fig.add_subplot(111)
ax.patch.set_alpha(0.5)
ax.set_xlabel('volts', alpha=0.5)

tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
# save 
# fig = plt.figure()

plt.savefig(pp, format='pdf')

pp.close()





