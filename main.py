

#웹 실행
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#요소를 찾기
from selenium.webdriver.common.by import By

#창 크기 조절
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#추가 기능
import time

#경로 확인
import os


# f = open("C:\com\program\Python\door\personal_info.txt", "r")
try:
    path1 = os.getcwd() + "\personal_info.txt"
    f = open(path1, "r")

    info_data = f.read()
    f.close()

    s_id = info_data.split("\n")[0]
    s_pw = info_data.split("\n")[1]

    print(s_id,s_pw)
    options = Options()

    # driver = webdriver.Chrome("C:\\com\program\Python\door\chromedriver.exe")

    path2 = os.getcwd() + "\chromedriver.exe"
    driver = webdriver.Chrome(path2)
    
    driver.maximize_window()
    
    driver.get("https://door.deu.ac.kr/sso/login.aspx")
    driver.implicitly_wait(60)
    login = driver.find_element(By.XPATH,"/html/body/form/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/input")

    login.send_keys(s_id)

    pw = driver.find_element(By.CLASS_NAME,"i_text")
    pw.send_keys(s_pw,Keys.RETURN)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH,'//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a').click()
    driver.implicitly_wait(60)

    # driver.find_element(By.CSS_SELECTOR,"td.tAlignL pad_10 font_wei_n").click()
    print('\n\n\n\n\n\nif you want to stop, press ctrl + c or input "stop"\n:\n\n')
    a = input()
    
    while 1:
        a = input('\n\nif you want to stop, press ctrl + c or input "stop"\n:')
        if a == "stop":
            driver.close()
            # break
        if a == "re" or a == "main":
            driver.get("http://door.deu.ac.kr/MyPage")

except KeyboardInterrupt:
    driver.close()