# Web-Scraping-Linkedin-Job-Page-with-Selenium-Python
In this project, we will be using Selenium which will help us to navigate between pages, fill out forms (such as login credentials), click links, etc. Briefly, besides the data scraping part, Selenium is going to be used to automate the following steps mentioned below to manage some actions until we access the pages where we will scrape the data. We will scrape the job offers and scrape their information.
<br>
<br>
The whole process would look like
- Navigate to the Linkedin login page.
- Look for the cookies pop-up and click it. Allow cookies
- Fill in the E-Mail Address and Password fields, then click Login.
- Select Jobs from the area above.
- Look for job openings. India's Data Scientist
- Scroll down to the bottom of the page to collect the link to each presented Job offer.
- When you reach the end of the page, proceed to the next page while continuing to collect links.
- After you've gathered all of the links, go to each one.
- To expand the job description content, click the "See More" option.
- Scrape the desired information
## Prerequisites
- Selenium Module
- Pandas Module
- Time Module
- Download chrome driver as per your chrome version
## File Contents
- Main.py -> Entire code for web scraping job offers in Linkedin with Selenium
- Cred.txt -> Contains credentials
- Job_desc.txt -> Contains Job Description
- linkedin.csv -> Contains Scraped Dataset
- DFD.png -> Data Flow of project
## Future Ideas
- Text dataset preprocessing
- ML model to predict fake job listings

