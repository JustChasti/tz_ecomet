import codecs
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import driver
from decorators import default_decorator


def get_city_html(db_id, ow_id):
    url = f'https://openweathermap.org/city/{ow_id}'
    data = driver.get(url)
    element = WebDriverWait(driver=driver, timeout=10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'heading'))
    )

    file = codecs.open(f'temp/{db_id}.html', "w", "utf−8")
    data = driver.page_source
    file.write(data)
    driver.quit()


@default_decorator('Finding city with selenium error')
def find_city(name):
    url = f'https://openweathermap.org/find?q={name}'
    data = driver.get(url)
    element = WebDriverWait(driver=driver, timeout=10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tab-pane.active'))
    )
    time.sleep(1)
    element = WebDriverWait(driver=driver, timeout=10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tab-pane.active'))
    )
    file = codecs.open(f'temp/find_{name}.html', "w", "utf−8")
    data = element.get_attribute('innerHTML')
    file.write(data)
    file.close()
    driver.quit()
