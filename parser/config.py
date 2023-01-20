import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

docker = False

# selenium configuration

if docker:
    pass

else:
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(
        'D:/code/tz_ecomet/parser/drivers/chromedriver.exe',
        options=options
    )

# db configuration
if docker:
    base_user = os.getenv('BASE_USER')
    base_pass = os.getenv('BASE_PASSWORD')
    base_name = os.getenv('BASE_NAME')
    base_host = os.getenv('BASE_HOST')
    base_port = os.getenv('BASE_PORT')

else:
    base_user = 'postgres'
    base_pass = 'qm7hFSIW'
    base_name = 'ecometbase'
    base_host = 'localhost'
    base_port = '5432'

# basic configuration
delay = 10

if docker:
    my_host = '0.0.0.0'
else:
    my_host = '127.0.0.1'

test_mode = True
