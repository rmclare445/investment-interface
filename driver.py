from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import keys as key

# Total ETFs
nETF = 3
# Headless operation
hls = True

if hls:
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(executable_path=key.driverpath, options=options)
else:
    driver = webdriver.Firefox(executable_path=key.driverpath)
    
# Log in
driver.get("https://investor.vanguard.com/my-account/log-on")
user_input = driver.find_element_by_id('username')
user_input.send_keys(key.username)
pass_input = driver.find_element_by_id('password')
pass_input.send_keys(key.password)
login = driver.find_element_by_css_selector('.vui-button')
login.click()

# Retrieve total earnings
driver.get('https://personal.vanguard.com/us/XHTML/com/vanguard/costbasisnew/xhtml/CostBasisSummary.xhtml')
total_gains = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'total.nr.right'))).text

# Retrieve individual performance
driver.get('https://personal.vanguard.com/us/TPView#634664130132126')
etfs, pcts, count = [], [], 3
try:
    while count <= nETF+2:
        etfs.append( driver.find_element_by_css_selector(
        '#BHForm2\:accountID\:1\:_id243tbody0 > tr:nth-child(%s) > td:nth-child(1)'%count).text
        )
        pcts.append( driver.find_element_by_css_selector(
        '#BHForm2\:accountID\:1\:_id243tbody0 > tr:nth-child(%s) > td:nth-child(7) > span:nth-child(1)'%count).text
        )
        count+=1
finally:
    pass

print(total_gains)
for i in range(len(etfs)):
    print(etfs[i], pcts[i].split())