# Newscrape
Newscrape is a Python script that automatically scrapes the latest headline from Goal.com Ghana and posts it to Twitter. Powered by Selenium and Tweepy, it runs headlessly and can be scheduled to tweet updates at intervals—ideal for football fans, content creators, or social media managers looking to automate news sharing.

🚀 Features

🔎 Scrapes latest football headline from Goal.com Ghana

🐦 Posts headline as a tweet with a news emoji

🛡️ Secure API key storage with environment variables

🕒 Run as a scheduled task (e.g., using cron or Task Scheduler)

## 🛠️ Tech Stack
- [Python](https://www.python.org/) 3.10+
  
- [Tweepy](https://docs.tweepy.org/) – Twitter API wrapper
  
- [Selenium](https://www.selenium.dev/documentation/) – Web automation tool
  
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api) – For posting tweets
  
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Manage environment variables

⚙️ Setup

🔑 How to Get Twitter API Keys

1. Go to [developer.x.com](https://developer.x.com/en) and log in with your Twitter account.

   ![Developer Portal](images/portal.png)

3. Click “Projects & Apps” in the top menu.

4. Create a New Project:

- Click “+ Create Project”

- Give your project a name and brief description (e.g., "Football Bot", "Posts headlines to Twitter")

4. Create an App within the Project:

- After creating the project, you'll be prompted to create an App

- Name your App (e.g., goal-news-bot)

- Choose the type of access (usually “Read and Write”)

- Agree to the terms and finish

5. Get Your Keys:

- Inside your App settings, go to "Keys and Tokens"

  ![App Settings](images/Setting.png)

- Generate the following credentials:

 - API Key

 - API Key Secret

 - Access Token

 - Access Token Secret

 - Bearer Token

6. Secure Your Keys in .env:

API_KEY=your_api_key

API_SECRET=your_api_secret

ACCESS_TOKEN=your_access_token

ACCESS_TOKEN_SECRET=your_access_token_secret

BEARER_TOKEN=your_bearer_token

🔧 Download ChromeDriver and Set Path

1. Go to chromedriver.chromium.org

2. Download the version that matches your Chrome browser

3. Extract the file and copy the path to chromedriver.exe

4. In your script, update this line:
   
   path = "C:\\path\\to\\chromedriver.exe"

how to run it
bash : python main.py
