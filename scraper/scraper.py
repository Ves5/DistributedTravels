import urllib.parse
import sys

import bs4

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.webdriver import WebDriver


# https://www.pluralsight.com/guides/advanced-web-scraping-tactics-python-playbook
def getDriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows https://chromedriver.chromium.org/downloads
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options)
    return driver
    
def getPageContent(driver: WebDriver, url, element):
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(lambda s: s.find_element_by_class_name(element).is_displayed())
    except TimeoutException:
        print(f'Element \'{element}\' not found on page')
        return None
    
    soup = bs4.BeautifulSoup(driver.page_source, 'html5lib') # or 'html.parser' for default python one
    return soup

def parseContent(soup: bs4.BeautifulSoup):
    # parse page content here
    pass

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        driver = getDriver()
        urls = f.readlines()
        for url in urls:
            # parse URL
            parsed_url = urllib.parse.urlparse(url)
            # hotel name
            print(parsed_url.path.split('/')[-1]) # temporary print
            # parameters
            params = urllib.parse.parse_qs(parsed_url.query)
            for param in params:
                print(f'{param} = {params[param][-1]}') # temporary print
            
            # parse content
            soup = getPageContent(driver, url, 'galeria') # class found on sample r.pl page
            parseContent(soup)
            
            #page = requests.get(url)
            #soup = bs4.BeautifulSoup(page.content, "html5lib")
            
            #print(soup.prettify())
        driver.close()
        
            