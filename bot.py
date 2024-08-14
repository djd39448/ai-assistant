import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class Bot:
    def run(self):
        print('Bot is running...')
        self.create_account()

    def create_account(self):
        # Set up Selenium WebDriver with user data directory and headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--user-data-dir=/tmp/chrome-user-data')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get('https://make.com')
        time.sleep(2)  # Wait for the page to load
        print('Account creation attempted.')
        driver.quit()

if __name__ == '__main__':
    bot = Bot()
    bot.run()