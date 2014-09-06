StartupFairTweeting
===================

Automatic tweeting for the UCB EECS Startup Fair, because let's face it - we are just too lazy.
This module tweets from a given csv file or emails a notification saying it's out of tweets.


Usage
-----
1. Get tweets from EventBrite. Go to the event page > Manage > Event Reports (Under Analyze).
    1. Click 'Show Columns' and make sure 'Survey Answers' is selected
    2. Click 'Update Report'
    3. Export to CSV
    4. Save the file as 'temp.csv'
    5. Put this file in the same directory as `tweeper.py`
2. Run `convert_evnt_brt_to_twts('temp.csv')`
    1. This extracts the tweets and writes to `EventBriteTweets.csv`
3. Copy `temp.csv` to `tweets.csv`
    1. Here's where you want to add custom tweets and edit the tweets that exist
    2. Be sure to follow the format of `Some Tweet Text,False`
    3. Note that tweets should not have commas in them
    4. Lines ending in False will be queued to tweet while lines ending with True won't be tweeted or have already been tweeted
4. Uncomment the last 5 lines (main and name)
    1. Make sure to comment out the `convert_evnt_brt_to_twts()` line
5. Set up a crontab to have this run in intervals (Weekly at first, then daily)
