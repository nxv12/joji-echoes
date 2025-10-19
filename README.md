#  Joji Echoes Bot

A scheduled Twitter bot that posts one Joji lyric every day at 3AM AEST. Built with Python, GitHub Actions, and emotional resonance.

---

##  Features

-  Daily tweets via GitHub Actions  
-  Manual test mode for safe, non-logged runs  
-  Duplicate filtering via `posted.txt`  
-  Secrets managed securely with GitHub Actions  
-  Lyric curation from `lyrics.txt`

---

##  How It Works

- Selects a random lyric from `lyrics.txt`  
- Skips previously posted lyrics using `posted.txt`  
- Tweets via Twitter API using GitHub Secrets  
- Runs daily at 3AM AEST (`cron: '0 16 * * *'`)  
- Supports manual runs with `--test` flag

---

##  Files

| File         | Purpose                          |
|--------------|----------------------------------|
| `app.py`     | Main bot logic                   |
| `lyrics.txt` | Source of Joji lyrics            |
| `posted.txt` | Tracks posted lyrics             |
| `.env`       | Local secrets (excluded from repo)  
| `bot.yml`    | GitHub Actions workflow          |

---

##  Test Mode

Run the bot with `--test` to skip logging the lyric to `posted.txt`. Useful for manual bonus tweets or debugging.

---

##  Follow the bot

[@JojiEchoes on X](https://x.com/JojiEchoes)

---

##  Ideas for Expansion
  
- Dry-run preview mode  
- Lyric scraping from Genius  
- Bonus tweet scheduler  
- Quote-only mode for Joji replies
