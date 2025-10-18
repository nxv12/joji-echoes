import os
import random
import tweepy
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def pick_lyric(path="lyrics.txt"):
    with open(path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and len(l.strip()) <= 270]
    return random.choice(lines)

def main():
    tweet = pick_lyric()
    api.update_status(tweet)
    print(f"Tweeted: {tweet}")

if __name__ == "__main__":
    main()