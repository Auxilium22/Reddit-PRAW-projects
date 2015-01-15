import praw
from config_bot import *

user_agent =  ('PM Reader & Responder 0.1 - by Auxilium11')
r = praw.Reddit(user_agent=user_agent)

# Logging in
r.login(REDDIT_USERNAME, REDDIT_PASS)

# Making variable to check if we have mail, default is false.
mail = "false"
 
for msg in r.get_unread(limit=None):
    mail = "true"
    textfilename = msg.id
 
if mail is "false":
    raise Exception('No Mail')
    
# If there is a mail, it writes the content to a new text file with the message id as name, easy to recall it! 
with open(textfilename +".txt", "w") as f:
    for msg in r.get_unread(limit=None):
        msg2 = msg.body
        f.write(msg2)
        print msg.id
        msg.mark_as_read()