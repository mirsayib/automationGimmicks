from selenium import webdriver

browser = webdriver.Firefox()

browser.get(
    'https://login.yahoo.com/')

createAccountBtn = browser.find_element_by_css_selector('#createacc')
createAccountBtn.click()

firstNameField = browser.find_element_by_css_selector('#usernamereg-firstName')
firstNameField.send_keys('Mir')

LastNameField = browser.find_element_by_css_selector('#usernamereg-lastName')
LastNameField.send_keys('Sayib')

emailField = browser.find_element_by_css_selector('#usernamereg-yid')
emailField.send_keys('mirsayib1999')

passField = browser.find_element_by_css_selector('#usernamereg-password')
passField.send_keys('adibpo008')

mobileField = browser.find_element_by_css_selector('#usernamereg-phone')
mobileField.send_keys('7889326611')

try:
    dobMonth = browser.find_element_by_css_selector('#usernamereg-month')
    dobMonth.send_keys('March')
except:
    browser.get('https://www.google.com')

dobDay = browser.find_element_by_css_selector('#usernamereg-day')
dobDay.send_keys('4')

dobYear = browser.find_element_by_css_selector('#usernamereg-year')
dobYear.send_keys('1998')

continuekey = browser.find_element_by_css_selector('#reg-submit-button')
continuekey.click()



#sending special Keys

# Attributes Meanings
# Keys.DOWN, Keys.UP, Keys.LEFT,
# Keys.RIGHT
# The keyboard arrow keys
# Keys.ENTER, Keys.RETURN The enter and return keys
# Keys.HOME, Keys.END, Keys.PAGE_DOWN,
# Keys.PAGE_UP
# The home, end, pagedown, and pageup keys
# Keys.ESCAPE, Keys.BACK_SPACE,
# Keys.DELETE
# The esc, backspace, and delete keys
# Keys.F1, Keys.F2, ..., Keys.F12 The F1 to F12 keys at the top of the keyboard
# Keys.TAB The tab key
