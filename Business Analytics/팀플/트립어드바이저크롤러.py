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
import logging 
from datetime import datetime 
import time as time
from selenium.common.exceptions import UnexpectedAlertPresentException

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') # gui 없이 돌아갈 수 있게 도와줌 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
    

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

driver = webdriver.Chrome('/Users/jeong-wonlyeol/Desktop/BA team project/chromedriver', chrome_options = chrome_options)
def croller():
    
    dic = {"name" : [] , "price" : [] ,"review" : [] ,"evaluation": [] }
    df1 = pd.DataFrame(dic)
    
    
    
    
    driver.get("https://www.tripadvisor.co.kr/Search?q=%EA%B0%95%EB%82%A8&searchSessionId=122CB00603311342A466E023ABA185CB1604468554867ssid&searchNearby=false&sid=B3FDBEDC9A40F96E756B7C9424E761AC1604468589664&blockRedirect=true&ssrc=e&rf=4") 
    
    count = 2
    time.sleep(2)
    page = 1
    
    while True:
            
        # 가게 선택 div1                    /html/body/main/article/div[2]/div/div/section/div[3]/ul/li[1]/div[2]/figure/figcaption/div/a/h2

        print(count)
        
        
        try:
            
            driver.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div['+str(count)+']/div/div/div/div[2]/div[1]/div[1]/span').click()
            df1 = smallCrawller(df1)
        except Exception as e:
            logger.warning(e)
            pass
        
        
        
        
        count = count+1
            
        
        
        if count > 40:
            page = page+1 # 이 페이지로 가야함 
            count = 1
            
        
            print(str(count) + " \n\n\n 프린트 카운트!!!")   
            try:
                print("Page  == ",page)
                driver.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/div/a[2]')
                
                time.sleep(2)
            except Exception as e :
                logger.warning(e)
                break
            
                
                
            #3번째부터
            #//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/a[5]
            
            
            
        
        
    
    return df1

    
def smallCrawller(df1):
    
    driver.implicitly_wait(5)
    
    
    driver.switch_to.window(driver.window_handles[1])
    # 언어 영어 선택 
    try:
        
        driver.find_element_by_xpath('//*[@id="taplc_detail_filters_rr_resp_0"]/div/div[1]/div/div[2]/div[4]/div/div[2]/div[1]/div[3]/label/span[1]').click()
    except:
        pass
    
    
    time.sleep(1)
    
    
    price = ""
    
    name = driver.find_element_by_css_selector('div > div._1hkogt_o > h1').text
    
    try:
        
        price = driver.find_element_by_xpath('//*[@id="component_42"]/div/div[2]/span[3]/a[1]').text
    except NoSuchElementException : 
        print('여기임?')
        pass
    
    # 여기서부터 리뷰 
    page = 1
    while True:
        
        try:
            taLnk = driver.find_elements_by_css_selector('span.taLnk.ulBlueLinks')
            if (len(taLnk) != 0):
                time.sleep(1)
                taLnk[0].click()
                time.sleep(2)
            reviews = driver.find_elements_by_css_selector('p.partial_entry')
            ratings = [rating.get_attribute('class').split(' ')[1].split('_')[1] for rating in driver.find_elements_by_css_selector('div.ui_column.is-9  span.ui_bubble_rating')]
            counter = 1
            
            for review,rating in zip(reviews,ratings):
               
                print('\n')
                counter += 1
            
                dic2 = {"name" : [name] , "price" : [price] ,"review" : [review.text] ,"evaluation": [rating] }
                
                df2 =pd.DataFrame(dic2)        
                print(df2)
                df1 = pd.concat([df1,df2])
                df1.to_csv("/Users/jeong-wonlyeol/Desktop/Tripadvisor.csv",encoding='utf-8-sig')
                        


        except Exception as e:
            print("여긴가? 1 ")
            logger.warning('Error Caught!')
            logger.warning(e)
            break
            
        
        
        
                
        
        try:
            if page == 1:
                print(page ,'Page')
                driver.find_element_by_xpath('//*[@id="taplc_location_reviews_list_resp_rr_resp_0"]/div/div[13]/div/div/a[2]').click()
                page = page + 1
                time.sleep(1)
            
            else:
                page = page +1 
                print(page ,'Page')
                
                driver.find_element_by_xpath('//*[@id="taplc_location_reviews_list_resp_rr_resp_0"]/div/div[12]/div/div/a[2]').click()
                time.sleep(1)
            
            
        
        except Exception as e:
            print("여긴가? 2 ")
            
            print("\n\n\n\n")
            logger.warning(e)
            
            break
        
        
    
    
    
    
    
    
    driver.close()
    
    driver.switch_to.window(driver.window_handles[0])
    
    print('여기 실행 됨 ? ')
    
    return df1 

    

            
    



if __name__ == "__main__":
    a = croller()
    a.to_csv("/Users/jeong-wonlyeol/Desktop/Tripadvisor_final.csv",encoding='utf-8-sig')
    
