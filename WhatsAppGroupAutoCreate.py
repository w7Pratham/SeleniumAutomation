
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def p():
	print('Done with Step--')

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	for i in range(0,1):
		time.sleep(10)
		try:
			createGroup()
		except NoSuchElementException:
			pass
		finally:
			print('Login Checked')

def createGroup():
    time.sleep(20)
    print('Attempting to create group')
    chat = driver.find_element(By.XPATH, "//span[@data-testid='menu']")
    chat.click()
    p()
    time.sleep(5)
    newGroup = driver.find_element(By.XPATH, "//li[@class='jScby Iaqxu FCS6Q'][@data-testid='mi-new-group menu-item']")
    newGroup.click()
    p()
    time.sleep(5)
    select = driver.find_element(By.CLASS_NAME,'_8nE1Y')
    select.click()
    p()
    time.sleep(5)
    arrow = driver.find_element(By.CSS_SELECTOR, '[data-testid="arrow-forward"]')
    arrow.click()
    p()
    time.sleep(5)
    new_text = 'TEST'
    p_element = driver.find_element(By.CSS_SELECTOR,'p.selectable-text.copyable-text.iq0m558w.g0rxnol2')

    # js_code = f'''
    #     var newSpan = document.createElement('span');
    #     newSpan.className = 'selectable-text copyable-text';
    #     newSpan.setAttribute('data-lexical-text', 'true');
    #     newSpan.textContent = '{new_text}';
        
    #     var targetParagraph = arguments[0];
    #     targetParagraph.innerHTML = '';
    #     targetParagraph.appendChild(newSpan);
    # '''

    p_element.send_keys('TEST')

    p()
    time.sleep(5)
    tick = driver.find_element(By.CSS_SELECTOR, 'span[data-testid="checkmark-medium"]')
    tick.click()



if __name__ == "__main__":
	whatsapp_login()
	print("Process complete successfully")
