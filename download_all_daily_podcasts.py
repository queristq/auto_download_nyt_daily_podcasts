from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import requests
from pathlib import Path
import os
import datetime

# parameters that you want to change
# foldername = r'D:\dev' # write the foldername that you want to save the pod cast files. I save this one 
foldername = r'write the folder name here to save the files, e.g., D:\dev' # write the foldername that you want to save the pod cast files. I save this one 
max_download_number = 5

# Set up the Chrome driver with JavaScript enabled
options = Options()
options.add_argument("--enable-javascript")
service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# Load the page and wait for it to fully render
url = "https://www.nytimes.com/column/the-daily"
driver.get(url)
driver.implicitly_wait(10)

# Find all links on the page
links = []
elems = driver.find_elements(By.XPATH, "//a[@href]")
current_year = str(datetime.datetime.now().year)
for elem in elems:
    if current_year in elem.get_attribute("href"):
        links.append(elem.get_attribute("href"))
for l in links:
    print(l)
# Quit the driver
driver.quit()

current_downlaoded_podcast_count = 0
for url  in links:
    # Create a new Chrome driver instance
    driver = webdriver.Chrome()

    # Enable JavaScript in the driver
    driver.execute_script("return navigator.webdriver")

    # Load the webpage in the driver
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Search the HTML source code for URLs with the .mp3 extension
    mp3_urls = re.findall('https?://[^\s"]+\.mp3', driver.page_source)

    # Download the mp3 files and replace the filename with the podcast's date and title
    urls_for_mp3_files = url.split("/")
    podcast_title = urls_for_mp3_files[-1].split(".")[0]
    podcast_date = urls_for_mp3_files[3]+urls_for_mp3_files[4]+urls_for_mp3_files[5]
        
    # You can now use the path variable as a string
    filename = foldername + r'\D' + podcast_date + '-' + podcast_title + '.mp3'
    
    if os.path.exists(filename):
        print("same file exists: " + filename )
    else:
        for mp3_url in mp3_urls:
            response = requests.get(mp3_url)
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f"Downloaded {filename}")
            break      # the first one is the target mp3 file. So break. 

    # Close the driver
    driver.quit()
    
    # if we finish all the downloads, then let's exit.     
    current_downlaoded_podcast_count = current_downlaoded_podcast_count+1
    if current_downlaoded_podcast_count >= max_download_number:
        print("Exiting the program. Total " + str(current_downlaoded_podcast_count) + " files have been downloaded")
        break
