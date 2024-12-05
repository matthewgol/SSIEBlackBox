from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

##first we start by creating an array that we are going to use for the title of the pandas dataframe 
titlecol = []

for i in range (0,400):
    if i < 100:
            titlecol.append("Q1-pos"+str(i))
    elif i < 200:
            titlecol.append("Q2-pos"+str(i))
    elif i < 300:
            titlecol.append("Q3-pos"+str(i))
    elif i < 400:
            titlecol.append("Q4-pos"+str(i))


##defininig the semi-global variables
stateN = []
q1,q2,q3,q4=[],[],[],[]

# Initialize the webdriver
service = Service(executable_path=r'C:\Users\matth\Programming\Packages\chromedriver-win64\chromedriver.exe')  # Update the path
driver = webdriver.Chrome(service=service)
driver.get(r'https://casci.binghamton.edu/academics/ssie501/blackbox/BlackBox.php?reset=1&cycles_input=1')

#scrape the web page for 'tds' -> this is how the cells are denoted on the black box
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
tds = soup.find_all('td')


##under this partitioning mechanism, we have the graph broken down into quadrants
for count, color in enumerate(tds):
    if count < 200:
        if count%20 < 10:
            q2.append(color.get('class')[0])
        else:
            q1.append(color.get('class')[0])
    else:
        if count%20 < 10:
            q3.append(color.get('class')[0])
        else:
            q4.append(color.get('class')[0])

#adds the stats together so that they are in order
stateN = q1+q2+q3+q4
#appends to the dataframe
blackboxstate = pd.DataFrame([stateN], columns=titlecol)

#we can step through as many times as we like 
for i in range(0,15):
    #gets the Next Step Button
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next n Step')]")
    button.click()
    time.sleep(1.5)
    stateNplus1=[]
    q1,q2,q3,q4=[],[],[],[]
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tds = soup.find_all('td')
    for count, color in enumerate(tds):
        if count < 200:
            if count%20 < 10:
                q2.append(color.get('class')[0])
            else:
                q1.append(color.get('class')[0])
        else:
            if count%20 < 10:
                q3.append(color.get('class')[0])
            else:
                q4.append(color.get('class')[0])
    stateNplus1 = q1+q2+q3+q4
    #print(f"The row length of the first one is {len(blackboxstate.columns)}")
    #print(f"The row length of the second one is {len(stateNplus1)}")
    #print(stateNplus1)
    blackboxstate.loc[len(blackboxstate)] = stateNplus1
    #button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next n Step')]")

path=r'C:\Users\matth\PhD\Fall 2024\SSIE 501-SSE 440\Programming\ScrapingOutput\\'
blackboxstate.to_csv(path+'blackbox.csv')  


input("Press Enter to close the browser...")