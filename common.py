'''
Created on Oct 27, 2020

@author: wuil
'''

import time
import keyring
import os

def send_keys_withjs(driver,field,value):
        driver.execute_script("arguments[0].setAttribute('value', '" + value +"')", field)


def login_into_linkedinwithpass(driver, username,password):
    print('login')
    LINKEDIN_URL = 'https://www.linkedin.com'
    driver.get(LINKEDIN_URL)
        
#         raw_input("Press Enter to continue...")
    time.sleep(1)
    
#     input('did it load the page')
#     """
#     Just login to linkedin if it is not already loggedin
#     """
    userfield = driver.find_element_by_id('session_key')
    passfield = driver.find_element_by_id('session_password')

    submit_form = driver.find_element_by_class_name('sign-in-form')


    print('1')
    # If we have login page we get these fields
    # I know it's a hack but it works
    
    try:
        if userfield and passfield:
            print('2')
#             userfield.send_keys(username)
#             send_keys_workaround(userfield, username)
            send_keys_withjs(driver,userfield, username)
            print('3')
#             passfield.send_keys(password)
#             send_keys_workaround(passfield, password)
            send_keys_withjs(driver,passfield, password)
            print('4')
            submit_form.submit()
#             try:
#                 driver.find_element_by_css_selector('div.flow-challenge')
#                 raw_input("Captcha")
#             except NoSuchElementException:
#                 pass
#             click.echo("Logging in")
    except:
        pass
    