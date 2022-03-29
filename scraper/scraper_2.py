# pluralsight.py
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
import json

def write_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text+ '\n')

def write_to_json_file(filename, text):
    dictionary = {
        "destination": text
    }
    json_object = json.dumps(dictionary, indent=1)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json_object)

def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()

    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")

    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    parentPath = os.path.dirname(os.path.abspath(__file__))
    os.chdir(parentPath)
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options)
    return driver


def getCourses(driver, url):
    # Step 1: Go to pluralsight.com, category section with selected search keyword
    driver.get(url)

    # wait for the element to load
    try:
        WebDriverWait(driver, 5).until(lambda s: s.find_element_by_id("hotels-switcher-box"))
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None

    # Step 2: Create a parse tree of page sources after searching
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Step 3: Iterate over the search result and fetch the course
    for course_page in soup.select("optgroup"):
        #print(course_page)
        for course in course_page.select("option"):
            #print(course)
            print(course.text)
            write_to_file("destinations.txt", course.text)
            write_to_json_file("destinations.json", course.text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You need to specify single path argument")
        exit(1)

    url = sys.argv[1]

    # create the driver object.
    driver = configure_driver()
    getCourses(driver, url)

    # close the driver.
    driver.close()