"""
In EventBrite, go to MyEvent>EventReports.
Be sure to select Survey Answers and Company in the configured Columns
Make sure there are no commas in the tweet!
"""
import csv
import tweepy


auth = tweepy.OAuthHandler('','')
auth.set_access_token('','')

api = tweepy.API(auth)

public_tweets = api.home_timeline()

def convert_evnt_brt_to_twts(event_brite_csv):
    """Read tweets from the EventBrite csv and write to EventBriteTweets.csv

    Format for internal csv files is row = tweet,True/False
    True/False denotes if the tweet has been tweeted or not already
    """
    with open(event_brite_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        twt_col = reader.next().index(
            'Tweet (to be tweeted by @ucbstarupfair)')
        tweets = []
        for row in reader:
            tweets.append(row[twt_col])
        tweets = [[x,'False'] for x in tweets if x != '']
    with open('EventBriteTweets.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(tweets)


def get_all_tweets(csvfile):
    """Gets tweets from the given file and returns a list of dicts

    [{tweet='', already_tweeted=True/False}]
    """
    tweet_dict = []
    with open(csvfile, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            tweet_dict.append(
                {'tweet': str(row[0]), 'already_tweeted': str_to_bool(row[1])})
    return tweet_dict


def str_to_bool(string):
    """Convert 'True' to True and 'False' to False"""
    if type(string) == bool:
        return string
    return string in ("True")


def write_all_tweets_csv(tweet_lst, csvfile):
    """Writes tweet_lst to csvfile in the following format:

    tweet,True/False
    """
    with open(csvfile, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for tweet in tweet_lst:
            writer.writerows([[tweet['tweet'], tweet['already_tweeted']]])


def update_status(status):
    """Updates live Twitter status with the string status"""
    api.update_status(status)


def get_next_tweet(tweet_lst):
    """Gets the next tweet that has not been tweeted yet"""
    for dic in tweet_lst:
        if not dic['already_tweeted']:
            return dic

def update_tweet_with_already_tweeted(tweet_lst, tweet_dict):
    """Updates tweet_lst that tweet_dict has already been tweeted

    and returns an updated tweet_lst"""
    tweet_str = tweet_dict['tweet']
    update = False
    updated_tweet_lst = []
    for tweet_dict in tweet_lst:
        if tweet_dict['tweet'] == tweet_str:
            new_tweet_dict = {'tweet': tweet_str, 'already_tweeted':True}
            updated_tweet_lst.append(new_tweet_dict)
            updated = True
        else:
            updated_tweet_lst.append(tweet_dict)
    if not updated:
        raise LookupError("Couldn't find tweet: {0}".format(tweet_str))
    return updated_tweet_lst

convert_evnt_brt_to_twts('temp.csv')
all_tweets = get_all_tweets('tweets.csv')
next_tweet_dict = get_next_tweet(all_tweets)
update_status(next_tweet_dict['tweet'])
updated_all_tweets = update_tweet_with_already_tweeted(all_tweets, next_tweet_dict)
write_all_tweets_csv(updated_all_tweets, 'tweets.csv')
