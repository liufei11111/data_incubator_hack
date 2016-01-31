import sys
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "565143844-m5xnhqoUQBMlDBTStd6KCuaVOVFTMkjbS0kE0EGM"
access_token_secret = "62w18tNodXh3SB69yeR51KMzWWM7z9VdYbArDZEmlJf4e"
consumer_key = "jykW12B5ataHCOJPDGzppA1OD"
consumer_secret = "VN5CqJa9N7LVh0FTqaZg857PVPycP36MNNHZ5pAXiObuM9ptm1"

count = 10000
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        if count == 0:
            sys.exit(0)
        print data
        count = count -1
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Hillary', 'Clinton', 'Rocky' ,'Fuente', 'Martin','Malley', 'Bernie','Sanders', 'Donald','Trumph'])

