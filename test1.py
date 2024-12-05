from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d"+'_'+"%H:%M:%S"))


# service = Service(executable_path=r'C:\Users\matth\Programming\Packages\chromedriver-win64\chromedriver.exe')  # Update the path
# driver = webdriver.Chrome(service=service)
# driver.get(r'https://casci.binghamton.edu/academics/ssie501/blackbox/BlackBox.php?reset=1&cycles_input=1')




# time.sleep(5)

# service = Service(executable_path=r'C:\Users\matth\Programming\Packages\chromedriver-win64\chromedriver.exe')  # Update the path
# driver = webdriver.Chrome(service=service)
# driver.get(r'https://casci.binghamton.edu/academics/ssie501/blackbox/BlackBox.php?reset=1&cycles_input=1')

# input("Press Enter to close the browser...")

