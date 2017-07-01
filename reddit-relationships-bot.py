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
        "spellings": ["grey rock", "grey-rock"],
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
]


def display_cliche_counts():
    for cliche in cliches:
        print "%s: %s" % (cliche['advice'], len(cliche['comments']))


def analyse_comment(comment):
    for cliche in cliches:
        for spelling in cliche['spellings']:
            if hasattr(comment, 'body') and spelling in comment.body.lower():
                cliche['comments'].append(comment.id)



print "Analysing for cliches..."
submissions = subreddit.hot(limit=10)
comments_analysed = 0

for submission in submissions:
    for comment in submission.comments.list():
        analyse_comment(comment)
        comments_analysed += 1

print "Analysed %d comments\n" % (comments_analysed)
display_cliche_counts()
