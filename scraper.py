from bs4 import BeautifulSoup
import requests


def scrape_info_tamu(url):
    scraped_data = []
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table')
    rows = table.find_all('td')
    for row in rows:
        scraped_data.append({
                "final_exam_time":final_exam_time, "regular_class_time":regular_class_time
            })
        scraped_data.append(row.text)

    return scraped_data

def scrape_school_data(url, university_id):
    scraping_functions = {
        1 : scrape_info_tamu
        # add more universities
    }
    
    # call the scraping function specific to the university id passed in
    scrape_function = scraping_functions.get(university_id)
    if scrape_function:
        scraped_data = scrape_function(url)
    else:
        print("Can't find the university id")
        scraped_data = None

    return scraped_data