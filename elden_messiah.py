import config
import praw

reddit = praw.Reddit(username=config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent="elden ring updates")


# print(reddit.user.me())
post_sent = []
subreddit = reddit.subreddit("Eldenring")

search_words = ["trailer", "reveal", "[official]", "teaser"]

for submission in subreddit.hot(limit=10):
    post_title = submission.title.lower()
    search_met = any(word in post_title for word in search_words)
    if submission.id not in post_sent and search_met:
        msg = "Miyazaki gives us hope! {0}. \n{1}".format(post_title, submission.shortlink)
        reddit.redditor(config.username).message("Elden rings news", msg)
        post_sent.append(submission.id)


