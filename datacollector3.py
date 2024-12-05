#set the global variables and the imports 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime



def get_row(driver):
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
    print(stateNplus1)
    return stateNplus1

def initialize_black_box(driver):
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
    row = get_row(driver)
    blackboxstate = pd.DataFrame([row], columns=titlecol)
    #print(blackboxstate)
    return blackboxstate


def update_webpage(driver):
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next n Step')]")
    button.click()
    time.sleep(1.5)
    return driver

def run_black_box(driver, steps):
    blackboxstate = initialize_black_box(driver)
    for i in range(0,steps):
        driver = update_webpage(driver)
        new_row = get_row(driver)
        blackboxstate.loc[len(blackboxstate)] = new_row
    return blackboxstate



for run in range(0,5):
    service = Service(executable_path=r'C:\Users\matth\Programming\Packages\chromedriver-win64\chromedriver.exe')  # Update the path
    driver = webdriver.Chrome(service=service)
    driver.get(r'https://casci.binghamton.edu/academics/ssie501/blackbox/BlackBox.php?reset=1&cycles_input=1')
    time.sleep(5)
    path=r'C:\Users\matth\PhD\Fall 2024\SSIE 501-SSE 440\Programming\ScrapingOutput\\'
    blackbox_output = run_black_box(driver, steps=10)
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d"+'_'+"%H-%M-%S")
    blackbox_output.to_csv(path+'blackbox'+str(timestamp)+'.csv')  

#have the definitions to collect the data

#run a loop to collect the data and get the output


input("Press Enter to close the browser...")
