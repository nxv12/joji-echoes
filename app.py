import os
import random
import tweepy
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def pick_lyric(path="lyrics.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and len(l.strip()) <= 270]
    return random.choice(lines)

def main():
    tweet = pick_lyric()
    if not tweet:
        print("No new lyrics to post.")
        return
    try:
        response = client.create_tweet(text=tweet)
        print(f"Tweeted: {tweet}\nTweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

def pick_lyric(path="lyrics.txt", history="posted.txt"):
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
    with open(history, "a", encoding="utf-8") as h:
        h.write(chosen + "\n")
    return chosen

if __name__ == "__main__":
    main()

