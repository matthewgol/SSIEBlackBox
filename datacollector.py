from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

##first we start by creating an array that we are going to use for the title of the pandas dataframe 
titlecol = []

for i in range (0,400):
    if i < 200:
        if i%20 < 10:
            titlecol.append("Q2-pos"+str(i))
        else:
            titlecol.append("Q1-pos"+str(i))
    else:
        if i%20 < 10:
            titlecol.append("Q3-pos"+str(i))
        else:
            titlecol.append("Q4-pos"+str(i))


##defininig the semi-global variables
stateN=[]


# Initialize the webdriver
service = Service(executable_path=r'C:\Users\matth\Programming\Packages\chromedriver-win64\chromedriver.exe')  # Update the path
driver = webdriver.Chrome(service=service)
driver.get(r'https://casci.binghamton.edu/academics/ssie501/blackbox/BlackBox.php?reset=1&cycles_input=1')

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all('td')


for td in tds:
    #print(td.get('class')[0])
    stateN.append(td.get('class')[0])
print(stateN)

blackboxstate = pd.DataFrame([stateN], columns=titlecol)

#print(blackboxstate)

button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next n Step')]")
button.click()
time.sleep(1.5)

for i in range(0,1000):
    stateNplus1=[]
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tds = soup.find_all('td')
    for td in tds:
        stateNplus1.append(td.get('class')[0])
    print(f"The row length of the first one is {len(blackboxstate.columns)}")
    print(f"The row length of the second one is {len(stateNplus1)}")
    print(stateNplus1)
    blackboxstate.loc[len(blackboxstate)] = stateNplus1
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next n Step')]")
    button.click()
    time.sleep(1.0)

path=r'C:\Users\matth\PhD\Fall 2024\SSIE 501-SSE 440\Programming\ScrapingOutput\\'
blackboxstate.to_csv(path+'blackbox.csv')  

#while sateN does not have 10-19, 20-29, 30-39, xxxx 100-109 != gru
#iterate 
#get new values
#wirte to csv 
#we will always write the value to state N  

input("Press Enter to close the browser...")