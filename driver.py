'''
'''

from selenium import webdriver
import keys as key

driver = webdriver.Firefox(executable_path=r'C:\Users\Ryan\Documents\GitHub\investment-interface\geckodriver.exe')
driver.get("https://investor.vanguard.com/my-account/log-on")
user_input = driver.find_element_by_id('username')
user_input.send_keys(key.username)
pass_input = driver.find_element_by_id('password')
pass_input.send_keys(key.password)

login = driver.find_element_by_css_selector('.vui-button')
login.click()

driver.get('https://personal.vanguard.com/us/XHTML/com/vanguard/costbasisnew/xhtml/CostBasisSummary.xhtml')
#cost_basis = driver.find_element_by_id('cbaPortfolioSummary:costBasisTabs_tabBoxItemLink0')
#cost_basis.click()

#cost_basis = driver.find_element_by_id('unrealizedTabForm:dataTableAccount_34169838_HoldingAccount_128tbody0')

driver.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/span/form/div[1]/span[2]/div/div/div[2]/div[1]/span/div[1]/span/div/div[1]/span/span[1]/table/tbody/tr[11]')

print(cost_basis.text)



#driver.get('https://personal.vanguard.com/us/TPView#634664130132126')
