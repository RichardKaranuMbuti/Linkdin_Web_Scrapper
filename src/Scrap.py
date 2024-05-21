from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

job_title = 'Python Developer'
location = 'Nairobi County, Kenya'

base_url = f"https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}&position=1&pageNum=0"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(base_url)
    # Waiting for the page to load- Later consider WebDriverWait for better performance
    time.sleep(30)

    # Get the entire page source
    page_source = driver.page_source
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Find all job cards
    job_cards = soup.find_all('div', class_='base-search-card__info')
    
    # Create a CSV file to write the job details
    with open('job_listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Job Title', 'Company Name', 'Location', 'Posting Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Iterate over job cards and write each job details to the CSV file
        for job_card in job_cards:
            job_title_tag = job_card.find('h3', class_='base-search-card__title')
            job_title = job_title_tag.get_text(strip=True) if job_title_tag else 'N/A'
            
            company_name_tag = job_card.find('h4', class_='base-search-card__subtitle')
            company_name = company_name_tag.get_text(strip=True) if company_name_tag else 'N/A'
            
            job_location_tag = job_card.find('span', class_='job-search-card__location')
            job_location = job_location_tag.get_text(strip=True) if job_location_tag else 'N/A'
            
            job_posting_date_tag = job_card.find('time', class_='job-search-card__listdate')
            job_posting_date = job_posting_date_tag.get_text(strip=True) if job_posting_date_tag else 'N/A'
            
            # Write the job details to the CSV file
            writer.writerow({'Job Title': job_title, 'Company Name': company_name, 'Location': job_location, 'Posting Date': job_posting_date})
    
    print("Job details have been written to 'job_listings.csv' successfully!")
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
