import sys

import bs4
import requests

import json
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import TimeoutException

#from selenium.webdriver.chrome.webdriver import WebDriver


# https://www.pluralsight.com/guides/advanced-web-scraping-tactics-python-playbook
#def getDriver():
#    chrome_options = Options()
#    chrome_options.add_argument("--headless")
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows https://chromedriver.chromium.org/downloads
#    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options)
#    return driver
    
#def getPageContent(driver: WebDriver, url, element):
#    driver.get(url)
#    try:
#        WebDriverWait(driver, 5).until(lambda s: s.find_element_by_class_name(element).is_displayed())
#    except TimeoutException:
#        print(f'Element \'{element}\' not found on page')
#        return None
    
#    soup = bs4.BeautifulSoup(driver.page_source, 'html5lib') # or 'html.parser' for default python one
#    return soup

#def parseContent(soup: bs4.BeautifulSoup):
    # parse page content here
#    pass

if __name__ == '__main__':
    #resp = request.urlopen('https://www.itaka.pl/')
    #source = resp.read().decode('utf-8')
    
    
    main_page = requests.get('https://www.itaka.pl/')
    #main_page.encoding = 'cp1252'
    #main_page.encoding = main_page.apparent_encoding
    main_soup = bs4.BeautifulSoup(main_page.content, "html.parser", from_encoding='utf-8')
    script = main_soup.find("form", {"id": "search-form"})
    script = script.find_next("script").string.split('= ')[1].split("\n")
    script = (''.join(script[0:2])).rstrip(';')
    #print(script[-10:])
    with open('test.json', 'w', encoding='utf-8') as f:
        f.write(script)
    json_data = json.loads(script)
    
    
    #parser = Parser()
    #tree = parser.parse(script.text)
    #array_items = []
    #for node in nodevisitor.visit(tree):
    #    if isinstance(node, ast.VarDecl) and node.identifier.value == 'baseSIPLSData':
    #        for item in node.initializer.items:
    #            parsed_dict = {getattr(n.left, 'value', '')[1:-1]: getattr(n.right, 'value', '')[1:-1]
    #                for n in nodevisitor.visit(item)
    #                if isinstance(n, slimit.ast.Assign)}
    #        array_items.append(parsed_dict)
    #print(array_items)
    
    #js_parser = Parser()
    #tree = js_parser.parse(script.text)
    #for node in nodevisitor.visit(tree):
        #if isinstance(node, ast.VarDecl) and node.identifier.value == 'baseSIPLSData':
            #print(node.value)
    
    
    #with open(sys.argv[1], 'r') as f:
        #driver = getDriver()
    #    urls = f.readlines()
    #    for url in urls:
            # parse URL
            #parsed_url = urllib.parse.urlparse(url)
            # hotel name
            #print(parsed_url.path.split('/')[-1]) # temporary print
            # parameters
            #params = urllib.parse.parse_qs(parsed_url.query)
            #for param in params:
            #    print(f'{param} = {params[param][-1]}') # temporary print
            
            # parse content
            #soup = getPageContent(driver, url, 'galeria') # class found on sample r.pl page
            #parseContent(soup)
            
    #        page = requests.get(url)
    #        soup = bs4.BeautifulSoup(page.content, "html.parser")
            
            #with open('res.txt', 'w', encoding='utf-8') as f:
            #    f.write(soup.prettify())
        #driver.close()
        
            