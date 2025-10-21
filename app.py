import os
import random
import tweepy
from dotenv import load_dotenv
import argparse 
import pytz
from datetime import datetime

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true', help='Run in test mode without logging')
args = parser.parse_args()

# Load environment variables
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Initialize Twitter client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Pick a lyric, optionally skip logging
def pick_lyric(path="lyrics.txt", history="posted.txt", log=True):
    with open(path, "r", encoding="utf-8") as f:
        lyrics = [l.strip() for l in f if l.strip()]
    posted = set()
    if os.path.exists(history):
        with open(history, "r", encoding="utf-8") as h:
            posted = set(h.read().splitlines())
    choices = [line for line in lyrics if line not in posted]
    if not choices:
        return None
    chosen = random.choice(choices)
    if log:
        with open(history, "a", encoding="utf-8") as h:
            h.write(chosen + "\n")
    return chosen

#Bot run logging
def log_run(status, tweet=None, error=None, logfile="logs.txt"):
    tz = pytz.timezone("Australia/Melbourne")
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a", encoding="utf-8") as f:
        if status == "success":
            f.write(f"[{now}] SUCCESS: {tweet}\n")
        else:
            f.write(f"[{now}] ERROR: {error}\n")

# Main bot logic
def main():
    tweet = pick_lyric(log=not args.test)
    if not tweet:
        print("No new lyrics to post.")
        log_run("error", error="No new lyrics to post.")
        return
    try:
        response = client.create_tweet(text=tweet)
        print(f"Tweeted: {tweet}\nTweet ID: {response.data['id']}") 
        log_run("success", tweet=tweet)
    except Exception as e:
        print(f"Error posting tweet: {e}")
        log_run("error", error=str(e))

if __name__ == "__main__":
    main()