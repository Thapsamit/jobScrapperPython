from cgitb import html
from bs4 import BeautifulSoup
import requests
import time




print("Enter Unfamiliar skill")
unfamiliarSkill = input()
print(f"Filtering unfamiliar skill {unfamiliarSkill}...")


def find_jobs(id):
    # get file response
    html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')

    # convert to text
    html_text = html_file.text

    # convert to soup 

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    # getting company names 

    for idx,j in enumerate(jobs):
        posted = j.find('span',class_='sim-posted').text
        if 'few' in posted:
            companies = j.find('h3',class_='joblist-comp-name')
            company_name = companies.text.replace(' ','') #replacig whitespaces
            skills = j.find('span',class_='srp-skills').text.replace(' ','')
            apply_link = j.header.h2.a['href'] #getting apply link in href attribute
            if unfamiliarSkill not in skills:
                with open(f'jobs/posts{id}.txt','a') as f:
                    f.write(f"Company Name : {company_name.strip()}\n")
                    f.write(f"Skills: {skills.strip()}\n")
                    f.write(f"Apply Link = {apply_link}\n")
                print(f'Jobs Saved with posts{id}.txt file...')

if __name__=="__main__":
    i = 1
    while i:
        find_jobs(i)
        timeLeft = 1
        print(f"Waiting for Time {timeLeft*10} seconds ...")
        time.sleep(timeLeft*10)
        i+=1
