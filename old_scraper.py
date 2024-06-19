from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def init_driver(webdriver_path):
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service = service)
    return driver

def navigate_to_website(driver, url):
    driver.get(url)

def close_driver(driver):
    driver.quit()

def scrape_info_tamu(driver):
    #texas a&m
    schedules = []
    rows = driver.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 1:
            final_exam_time = cells[0].get_attribute("innerText")
            regular_class_time = cells[1].get_attribute("innerText")
            schedules.append({
                "final_exam_time":final_exam_time, "regular_class_time":regular_class_time
            })
    return schedules


def scrape_school_data(url, university_id):
    # driver and navigate to website
    path_to_driver = "chromedriver.exe"
    driver = init_driver(path_to_driver)
    navigate_to_website(driver, url)

    scraping_functions = {
        1 : scrape_info_tamu
        # add more universities
    }
    
    # call the scraping function specific to the university id passed in
    scrape_function = scraping_functions.get(university_id)
    if scrape_function:
        scraped_data = scrape_function(driver)
    else:
        print("Can't find the university id")
        scraped_data = None
        
    close_driver(driver)
    return scraped_data
