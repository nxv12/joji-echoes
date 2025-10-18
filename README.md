🎤 Joji Echoes — Lyric Bot for X (Twitter)
Joji Echoes is a minimalist Python bot that posts iconic one-line lyrics from Joji’s discography to X (formerly Twitter). Designed for fans, built for automation, and deployed via Heroku.

📦 Features:

- Posts one lyric at a time from a curated lyrics.txt file
- Uses X API v2 via Tweepy’s Client.create_tweet()
- Reads secrets from .env or Heroku config vars
- Deployable via Heroku with scheduled tweets
- Easy to customize, expand, and remix

Getting Started:

1. Clone the repo
git clone https://github.com/yourusername/joji-echoes.git
cd joji-echoes

2. Create your .env file
env
API_KEY=your_api_key
API_KEY_SECRET=your_api_key_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
BEARER_TOKEN=your_bearer_token

3. Install dependencies
python -m pip install -r requirements.txt

4. Run the bot
python app.py

🗂 Project Structure:

joji-echoes/
- app.py              # Main bot logic
- lyrics.txt          # One-line lyrics (one per song)
- requirements.txt    # Dependencies
- Procfile            # Heroku process declaration
- .env                # API keys (local use only)

☁️ Deploying to Heroku:

1. Create app
heroku create joji-echoes

2. Set config vars
heroku config:set API_KEY=... API_KEY_SECRET=... ACCESS_TOKEN=... ACCESS_TOKEN_SECRET=... BEARER_TOKEN=...

3. Push code
git add .
git commit -m "Initial commit"
git push heroku main

4. Add Heroku Scheduler
heroku addons:create scheduler:standard
heroku addons:open scheduler

Schedule: python app.py every 6 hours or daily

🎨 Customization Ideas:

- Add hashtags or emojis to tweets
- Prevent duplicate lyrics
- Rotate themes (e.g., sad Joji, romantic Joji)
- Add images or album art
- Integrate with other fan bots

🧠 Credits:

Curated and built by Naveed Naleem Inspired by Joji’s discography and the art of quiet resonance.
