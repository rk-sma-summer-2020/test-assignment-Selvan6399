from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

consumer_key = 'Rw5gDHlkgRWiACkatfsAC0mMx'
consumer_secret = 'KRYsQaaRwHiCX6SC82vdU1F28tximdWPWZO9gYgAnYNcjQuOqh'
access_token = '1134099088775962624-3NqvSuFSgzXzmXoKsNLGfcmFHeIkhK'
access_secret = 'XX2d957VPIhFcH2PmlPM7xxVfjPItiA69xaCjtKIo2WUf'

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
    	fname = sys.argv[1]
    	try:
    		with open(fname, 'a') as f:
    			f.write(data)
    			return True
    	except BaseException as e:
    		print("Error in writing to file")
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = Stream(auth, l)
stream.filter(track=['RPSvMI'])
