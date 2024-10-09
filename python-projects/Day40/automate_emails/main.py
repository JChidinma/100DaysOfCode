import yagmail
import pandas as pd
import datetime
from dotenv import load_dotenv
from news import NewsFeed
load_dotenv(override=True)

df = pd.read_excel('people.xlsx')
gmail_user = os.environ['gmail_user']
gmail_password = os.environ['gmail_app_password']

for index, row in df.iterrows():
    # print(row)
    # print(row['name'])
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() -
                 datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    news_feed = NewsFeed(
        interest=row['interest'], from_date=yesterday, to_date=today, language='en')
    email = yagmail.SMTP(user=gmail_user,
                         password=gmail_password)
    email.send(
        to=row['email'],
        subject=f"Your {row['interest']} news report for today!",
        contents=f"Hi {row['name']},\nSee what's up about {row['interest']} today. \n\n{news_feed.get()} \n\nRegards,\nJoyce"
    )

