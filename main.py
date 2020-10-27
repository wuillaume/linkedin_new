'''
Created on Jul 19, 2020

@author: wuil
'''

from selenium import webdriver
from selenium.common.exceptions import (WebDriverException,
                                        NoSuchElementException)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webbus import WebBus
import time
from common import login_into_linkedinwithpass


def start():
    
    email = input("Type your linkedin email and press enter: ")
    password = input("Type your linkedin password and press enter: ")
    
    with WebBus('chrome') as bus:
        driver = bus.driver
        login_into_linkedinwithpass(driver, email,password)
        time.sleep(10)
        driver.get('https://www.linkedin.com/search/results/people/?keywords=&network=%5B%22S%22%5D&origin=FACETED_SEARCH&title=RH')
        
        p=0
        while(p<10):
            p+=1
            searchResult = driver.find_element_by_css_selector('div.search-results-page')
            searchEntities = searchResult.find_elements_by_css_selector('li.reusable-search__result-container')
            for entity in searchEntities:
    #             print(entity.get_attribute('innerHTML'))
                try:
                    entityHeader = entity.find_element_by_tag_name('a')
                    link = entityHeader.get_attribute('href')
                    print(link)
                    textEntity = entity.text
                    
                    firstName = textEntity.split(' ')[0]
                    print(firstName)
                    buttonConnect = entity.find_element_by_tag_name('button')
                    time.sleep(5)
                    buttonConnect.click()
                    time.sleep(10)
                    invitation = driver.find_element_by_css_selector('div.send-invite')
                    
                    noteButton = invitation.find_elements_by_tag_name('button')[1] 
                    noteButton.click()
                    time.sleep(10)
                    
                    invitation = driver.find_element_by_css_selector('div.send-invite')
        #             print(invitation.get_attribute('innerHTML'))
                    textarea = invitation.find_element_by_tag_name('textarea')
                    textarea.clear()
                    inputtext = 'Bonjour '+firstName+',\nje vous contacte pour une recherche sur les diverses pratiques RH aidant les employés à se rencontrer -- chose rendue difficile par le Covid.\nAuriez-vous 15 min pour en discuter cette semaine?\nJe serai ravi de partager mes infos également.\nExcellente fin de journée,\nWuillaume'
                    
        
                    for part in inputtext.split('\n'):
                        textarea.send_keys(part)
                        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                    time.sleep(10)
                    
                    invitation = driver.find_element_by_css_selector('div.send-invite')
                    noteButton = invitation.find_elements_by_tag_name('button')[2] 
                    noteButton.click()
                    time.sleep(50)
                except:
                    pass
            nextButton = driver.find_element_by_css_selector('button.artdeco-pagination__button--next')
            nextButton.click()
            time.sleep(10)
            
            

            
            
       

if __name__ == "__main__":
    start()