'''
Created on Jul 19, 2020

@author: wuil
'''

import click
from selenium import webdriver
from selenium.common.exceptions import (WebDriverException,
                                        NoSuchElementException)


class UnknownUserException(Exception):
    pass


class UnknownBrowserException(Exception):
    pass



class WebBus:
    """
    context manager to handle webdriver part
    """

    def __init__(self, browser):
        self.browser = browser
        self.driver = None

    def __enter__(self):
        # XXX: This is not so elegant
        # should be written in better way
        if self.browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser.lower() == 'chrome':
            
            options = webdriver.ChromeOptions() 
#             options.add_argument('--headless')
            self.driver = webdriver.Chrome(executable_path="resources/chromedriver",chrome_options=options)
        elif self.browser.lower() == 'phantomjs':
            self.driver = webdriver.PhantomJS()
        else:
            raise UnknownBrowserException("Unknown Browser")

        return self

    def __exit__(self, _type, value, traceback):
        if _type is OSError or _type is WebDriverException:
            click.echo("Please make sure you have this browser")
            return False
        if _type is UnknownBrowserException:
            click.echo("Please use either Firefox, PhantomJS or Chrome")
            return False

        self.driver.close()