# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:35:55 2020

@author: User
"""

import pandas as pd 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
import urllib.request
import requests
from datetime import datetime 
import time as time
from selenium.common.exceptions import UnexpectedAlertPresentException

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') # gui 없이 돌아갈 수 있게 도와줌 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
    

driver = webdriver.Chrome('/Users/jeong-wonlyeol/Desktop/BA team project/chromedriver', chrome_options = chrome_options)
def croller():
    
    dic = {"name" : [] , "price" : [] ,"review" : [] ,"evaluation": [] }
    df1 = pd.DataFrame(dic)
    
    
    
    
    driver.get("https://www.mangoplate.com/search/%EA%B0%95%EB%82%A8%20") 
    
    count = 1     
    time.sleep(2)
    page = 1
    
    while True:
            
        # 가게 선택 div1                    /html/body/main/article/div[2]/div/div/section/div[3]/ul/li[1]/div[2]/figure/figcaption/div/a/h2
        try:
            print(count)
            driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[3]/ul/li['+str(count)+']/div[1]/figure/figcaption/div/a').click()
            print('두번쨰꺼 부터 됨 ')         
            
            df1 = smallCrawller(df1)
            
            driver.find_element_by_xpath('/html/body/main/article/div[2]/div/div/section/div[3]/ul/li['+str(count)+']/div[2]/figure/figcaption/div/a').click()
            
            df1 = smallCrawller(df1)
            count = count+1
            
        except :
            page = page+1
            count = 1
            print(str(count) + " \n\n\n 프린트 카운트!!!")   
                
            driver.find_element_by_xpath("/html/body/main/article/div[2]/div/div/section/div[4]/p/a["+str(page)+"]").click()
            time.sleep(3)
            
            
            
            
            
        
        
    
    return df1

    
def smallCrawller(df1):
    price = ""
    name = driver.find_element_by_xpath("/html/body/main/article/div[1]/div[1]/div/section[1]/header/div[1]/span/h1").text
    try:
        
        price = driver.find_element_by_xpath("/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[10]/td/ul/li[1]/span[2]").text
    except NoSuchElementException : 
    
        pass
    
    
    # 버튼누르기 (있는 리뷰 모두 )

    while True:
        try:
            
            driver.find_element_by_xpath("/html/body/main/article/div[1]/div[1]/div/section[3]/div[2]").click()
            
            time.sleep(2)
        except:
            break
            
    review_count = 1
    while True:
        
        
        try:
            
            review = driver.find_element_by_xpath('/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li['+str(review_count)+']/a/div[2]/div/p').text
            
            evaluation = driver.find_element_by_xpath("/html/body/main/article/div[1]/div[1]/div/section[3]/ul/li["+str(review_count)+"]/a/div[3]/span").text
        
            dic2 = {"name" : [name] , "price" : [price] ,"review" : [review] ,"evaluation": [evaluation] }
            
            df2 = pd.DataFrame(dic2)
            df1 = pd.concat([df1,df2])
            df1.to_csv("/Users/jeong-wonlyeol/Desktop/mangoplate.csv",encoding='utf-8-sig')
                        
            print(dic2)
            review_count = review_count + 1 
        except NoSuchElementException:
            print("smallCrawller")
            
            break
    
    
    driver.back()
    return df1 
    

            
    



if __name__ == "__main__":
    a = croller()
    a.to_csv("/Users/User/Desktop/mangoplate.csv",encoding='utf-8-sig')
    
