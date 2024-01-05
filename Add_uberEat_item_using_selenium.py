import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.get("https://restaurant.uber.com/")
# driver.maximize_window()
print(driver.title)
sleep(3)


with open("add_gum.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lin in csv_reader:
        prdcuts_name = lin[1]
        prdcuts_price = float(lin[2])
        print(prdcuts_name)

        click_add = driver.find_element("xpath", '//*[@id="overviewSidePanelDiv"]/div/div[1]/header/div/div/div[2]/button')
        click_add.click()
        sleep(2)
        click_add_item = driver.find_element("xpath", '/html/body/div/div/div[2]/div[2]/div/div/div/ul/li[2]')
        click_add_item.click()
        sleep(2)
        item_name = driver.find_element("xpath", '//*[@id="about"]/div[1]/div/div[2]/div/div/input').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

        sleep(1)
        item_name1 = driver.find_element("xpath", '//*[@id="about"]/div[1]/div/div[2]/div/div/input')
        item_name1.send_keys(f"{prdcuts_name}")
        sleep(0.5)

        item_price = driver.find_element("xpath", '//*[@id="pricing"]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/input')
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
        sleep(1)
        item_price.send_keys(prdcuts_price)
        sleep(0.5)
        try:
            sleep(1)
            update = driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/button[2]').click()
        except:
            pass
        sleep(1)
        save = driver.find_element("xpath", '//*[@id="overviewSidePanelDiv"]/div/div[1]/header/div/div/button[2]').click()
        sleep(1)
        try:
            leave = driver.find_element("xpath", '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/button[2]').click()
            sleep(2)
        except:
            pass
