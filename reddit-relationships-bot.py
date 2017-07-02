import os
import praw
from settings import SETTINGS

reddit = praw.Reddit(client_id=SETTINGS['REDDIT_CLIENT_ID'],
                     client_secret=SETTINGS['REDDIT_CLIENT_SECRET'],
                     user_agent=SETTINGS['REDDIT_USER_AGENT'])

subreddit = reddit.subreddit('relationships')

cliches = [
    {
        "advice": "Break up",
        "spellings": ["divorce", "break up", "leave him", "leave her"],
        "comments": [],
    },
    {
        "advice": "Get your ducks in a row",
        "spellings": ["ducks in a row"],
        "comments": [],
    },
    {
        "advice": "Don't JADE",
        "spellings": ["jade"],
        "comments": [],
    },
    {
        "advice": "Grey rock",
        "spellings": ["grey rock", "grey-rock", "gray rock", "gray-rock"],
        "comments": [],
    },
    {
        "advice": "Consult a lawyer",
        "spellings": ["lawyer"],
        "comments": [],
    },
    {
        "advice": "Go no-contact",
        "spellings": ["no contact", "no-contact"],
        "comments": [],
    },
    {
        "advice": "Love languages",
        "spellings": ["love language"],
        "comments": [],
    },
    {
        "advice": "Low-contact",
        "spellings": ["low contact", "low-contact"],
        "comments": [],
    },
    {
        "advice": "\"No\" is a complete sentence",
        "spellings": ["no is a complete sentence", "\"no\" is a complete sentence"],
        "comments": [],
    },
    {
        "advice": "Red flag",
        "spellings": ["red flag"],
        "comments": [],
    },
    {
        "advice": "Get therapy / counselling",
        "spellings": ["therapy", "counselling"],
        "comments": [],
    },
    {
        "advice": "Hit the gym",
        "spellings": ["hit the gym", "go the the gym", "going to the gym"],
        "comments": [],
    },
]


def display_information():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Analysing %d submissions for cliches" % (SETTINGS["SUBMISSIONS_TO_ANALYSE"])
    print "Analysed %d comments from %s submissions\n" % (comments_analysed, submissions_analysed + 1)
    for cliche in cliches:
        print "%s: %s" % (cliche['advice'], len(cliche['comments']))


def analyse_comment(comment):
    for cliche in cliches:
        for spelling in cliche['spellings']:
            if hasattr(comment, 'body') and spelling in comment.body.lower():
                cliche['comments'].append(comment.id)


submissions = subreddit.hot(limit=SETTINGS["SUBMISSIONS_TO_ANALYSE"])
submissions_analysed = 0
comments_analysed = 0

for submission in submissions:
    for comment in submission.comments.list():
        analyse_comment(comment)
        comments_analysed += 1
        display_information()

    submissions_analysed += 1

print "\nComplete."
