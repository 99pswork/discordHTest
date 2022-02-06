from selenium import webdriver
import undetected_chromedriver as uc
import requests
import time

site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
pageurl = 'https://discord.com/register'

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get(pageurl)
print("SLEEP")
time.sleep(60)
print("WAKE")
api_key = "a87ea21189afab895a352b4da421416d"

form = {"method": "hcaptcha",
        "googlekey": site_key,
        "key": api_key, 
        "pageurl": pageurl, 
        "json": 1}

response = requests.post('http://2captcha.com/in.php', data=form)
request_id = response.json()['request']
print(request_id)


url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

status = 0
while not status:
    res = requests.get(url)
    print(res.json()['request'])
    if res.json()['status']==0:
        time.sleep(3)
    else:
        requ = res.json()['request']
        js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
        js2 = f'document.getElementById("h-captcha-response").innerHTML="{requ}";'
        driver.execute_script(js)
        driver.execute_script(js2)
        driver.find_element_by_id("recaptcha-demo-submit").submit()
        status = 1
