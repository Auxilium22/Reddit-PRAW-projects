import praw
from config_bot import *

user_agent =  ('PM Reader & Responder 0.1 - by Auxilium11')
r = praw.Reddit(user_agent=user_agent)

# Logging in
r.login(REDDIT_USERNAME, REDDIT_PASS)

with open("pm.txt", "w") as f:
    for msg in r.get_unread(limit=None):
        msg2 = str(msg)
        f.write(msg2)
        msg.mark_as_read()
