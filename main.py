from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

link = "https://www.flashscorekz.com/"
football_class = "event__match--twoLine"

custom_options = Options()
custom_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=custom_options)
driver.get(link)

driver_m = driver.find_elements(By.CLASS_NAME, football_class)
matches = []

for match in driver_m:
    match = match.text.splitlines()
    if match[4] < 2:
        matches.append(match)   


collumns = ['status', 'team 1', 'team 2', 'goals 1', 'goals 2']
df = pd.DataFrame(matches, columns=collumns)
excel_filename = "output_data.xlsx"
df.to_excel(excel_filename, index=False)
driver.quit()