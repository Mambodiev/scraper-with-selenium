from selenium import webdriver
from lxml import html
from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(ChromeDriverManager().install())

s = Service('/tmp/chromedriver')
driver = webdriver.Chrome(service=s)

for page_nb in range(1,2):
    driver.get('https://www.aliexpress.com/w/wholesale-bike.html?SearchText=bike&catId=0&dida=y&initiative_id=AS_20230127125001&spm=a2g0o.home.1000002.0&trafficChannel=main&g=y&page={}'.format(page_nb))
    sleep(1)
    tree = html.fromstring(driver.page_source)

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(1)

    for product_tree in tree.xpath("//a[@class='manhattan--container--1lP57Ag cards--gallery--2o6yJVt']"):
        try:
            title = product_tree.xpath(".//h1[@class='manhattan--titleText--WccSjUS']/text()")
        except:
            title = None
        try:
            price = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='manhattan--price-sale--1CCSZfK']")))
        except:
            price = None

        try:
            review = product_tree.xpath(".//span[@class='manhattan--evaluation--3cSMntr']/text()") 
        except:
            review = None
        try:    
            nb_sold = product_tree.xpath('.//span[@class="manhattan--trade--2PeJIEB"]/text()')
        except:
            nb_sold = None

            
        print(title, price.text, review, nb_sold) 


    print("\n\n\n\n\n")