from bs4 import BeautifulSoup
from selenium import webdriver
from optparse import OptionParser
import time

print("""


   _____ _      _      _                      
  / ____| |    (_)    | |                     
 | |    | |     _  ___| | ___ __ ___   ___    
 | |    | |    | |/ __| |/ / '_ ` _ \ / _ \   
 | |____| |____| | (__|   <| | | | | |  __/   
  \_____|______|_|\___|_|\_\_|_|_| |_|\___|__ 
         | |           \ \   / /       (_)/ _|
         | |__  _   _   \ \_/ /   _ ___ _| |_ 
         | '_ \| | | |   \   / | | / __| |  _|
         | |_) | |_| |    | || |_| \__ \ | |  
         |_.__/ \__, |    |_| \__,_|___/_|_|  
                 __/ |                        
                |___/                          
                  
""")

print("Program başlayır...")
 
time.sleep(4)

def elements(url):
    clickable_elements = []
    # Selenium kitabxanasi ile web sehifeni yukleyirik
    driver = webdriver.Chrome() 
    driver.get(url)
    
        
    # HTML elementlerini parse ede bilmek ucun BeautifulSoup kitabxanasindan istifade et
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Klikleye bileceyim elementleri ver
    clickable_elements.extend(soup.find_all('a'))
    clickable_elements.extend(soup.find_all('button'))
    

    driver.quit()
    
    return clickable_elements

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="web saytın url-i")
    (options, args) = parser.parse_args()

    if not options.url:
        parser.error('Bu aləti işə sala bilmək üçün url-i qeyd etməlisiniz.')

    clickable_elements = elements(options.url)
    print("Səhifədə tapılan kiləyə biləcəyin elementlər:")
    for element in clickable_elements:
        print(element)
