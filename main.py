from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Create Tweepy client (v2)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)


website = "https://www.goal.com/en-gh"
path = "C:\\Users\\ALINCO TECH-28\\Documents\\chromedriver-win64\\chromedriver.exe"



options = Options()
options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--log-level=3")  # Suppress most ChromeDriver logs
# options.add_argument("--headless")  # Uncomment if you want headless

service = Service(path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)






h3 = driver.find_element(by="xpath", value="//h3").text
print(h3)
tweet = f"📰 Top News: {h3}"
response = client.create_tweet(text=tweet)
print("Tweet posted! ID:", response.data["id"])


driver.quit()