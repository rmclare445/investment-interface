from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import keys as key

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
cost_basis = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'total.nr.right'))
)
total_gains = cost_basis.text

# Retrieve individual performance
driver.get('https://personal.vanguard.com/us/TPView#634664130132126')
vug_ar = driver.find_element_by_css_selector('#BHForm2\:accountID\:1\:_id243tbody0 > tr:nth-child(3) > td:nth-child(7) > span:nth-child(1)')
vht_ar = driver.find_element_by_css_selector('#BHForm2\:accountID\:1\:_id243tbody0 > tr:nth-child(4) > td:nth-child(7) > span:nth-child(1)')
vpu_ar = driver.find_element_by_css_selector('#BHForm2\:accountID\:1\:_id243tbody0 > tr:nth-child(5) > td:nth-child(7) > span:nth-child(1)')


print(total_gains)
for i in (vug_ar, vht_ar, vpu_ar):
    print(i.text)