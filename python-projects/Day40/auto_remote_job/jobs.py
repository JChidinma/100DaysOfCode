import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv(override=True)

REMOTEOK_API_URL = "https://remoteok.com/api"
keywords = ['senior software engineer', 'senior data engineer', 'senior machine learning engineer',
            'senior machine learning operations engineer', 'senior MLOps Engineer', 'DevOps']
# contract_keywords = ['contract', 'freelance', 'contractor', 'full time']


class JobFeed:
    # def __init__(self, api_url, keywords, contract_keywords):

    def __init__(self, api_url, keywords):

        self.api_url = api_url
        self.keywords = [keyword.lower() for keyword in keywords]
        # [keyword.lower() for keyword in contract_keywords]

    def get_remote_jobs(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            jobs = response.json()
            return jobs
        else:
            print("Failed to retrieve data")
            return []

    def filter_jobs(self, jobs):
        remote_jobs = []

        for job in jobs:
            if job.get('position') and job.get('tags'):
                position = job['position'].lower()
                tags = [tag.lower() for tag in job['tags']]
                location = job['location'].lower()
                for keyword in self.keywords:
                    if keyword in position and 'Canada' in location or 'United States' in location:
                        remote_jobs.append(job)
                        break
                    break

        print(remote_jobs)


if __name__ == "__main__":
    job_feed = JobFeed(REMOTEOK_API_URL, keywords)

    jobs = job_feed.get_remote_jobs()

    filtered_jobs = job_feed.filter_jobs(jobs)
    pprint(filtered_jobs)

    # for job in jobs:
    #     if job.get('position') and job.get('tag'):
    #         position = job['position'].lower()
    #         tags = [tag.lower() for tag in job['tags']]

    #         for keyword in self.keywords:
    #             if keyword in position and 'contract' in tags:
    #                 for contract in self.contract_keywords:
    #                     if contract in position or contract in tags:
    #                         remote_jobs.append(job)
    #                         break
    #                 break

    # print(remote_jobs)

# date, company, position, tags: [], description, salary_min, salary_max, location (city, city, Country), url, apply_url
# class NewsFeed:
#     base_url = os.environ['NEWS_API_URL']
#     api_key = os.environ['NEWS_API_KEY']

#     def __init__(self, interest, from_date, to_date, language):
#         self.interest = interest
#         self.from_date = from_date
#         self.to_date = to_date
#         self.language = language

#     def get(self):
#         url = self._build_url()
#         response = requests.get(url)
#         content = response.json()
#         articles = content['articles']

#         email_body = ''
#         for article in articles:
#             email_body = email_body + \
#                 article['title'] + "\n" + article['url'] + "\n\n"
#         return email_body

#     def _get_articles(self, url):
#         url = self._build_url()
#         response = requests.get(url)
#         content = response.json()
#         articles = content['articles']
#         return articles

#     def _build_url(self):
#         url = f"{self.base_url}q={self.interest}&from={self.from_date}&to={self.to_date}&{self.language}&apiKey={self.api_key}"
#         return url


# if __name__ == "__main__":
#     news_feed = NewsFeed(interest='nasa',
#                          from_date='2024-09-11', to_date='2024-09-15', language='en')
#     print(news_feed.get())
