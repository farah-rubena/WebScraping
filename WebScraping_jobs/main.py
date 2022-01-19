#goal os to get all jobs that are posted a few days ago. So we will be scraping all jobs and then condition pur program to get the jobs thta have been posted only a few days ago

from bs4 import BeautifulSoup
import requests
import time


#filter basis skills using input
print("Put some skill you're not familiar with")
unfamiliar_skills = input('>')
print(f"Filtering out {unfamiliar_skills}")


def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    #print(html_text)

    #Create a beutifulsoup instance and then pass he html as the html_text variable
    soup = BeautifulSoup(html_text, "lxml")
    #print(soup)

    #get jobs using the tag and class name
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    #search for the specific element (company name) inside the job
    for index, job in enumerate(jobs):
        #in order tp get the jobs posted a few days ago start with published date

        # because this data is embeded in a span tag inside a span tag
        published_date = job.find('span', class_="sim-posted").span.text
        if "few" in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace("  ", "")
            skills = job.find('span', class_="srp-skills").text.replace("  ", "")
            #going inside multiple tags
            job_desc = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.xls', "w") as f:
                    f.write(f'{index} Company Name: {company_name.strip()}\n')
                    f.write(f'Keyskills: {skills.strip()}\n')
                    f.write(f'Job Description: {job_desc}\n')
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        #allows prog to wait certain number of mins
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait * 100)

