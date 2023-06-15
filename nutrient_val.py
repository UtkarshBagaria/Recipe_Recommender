from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tryingscrap2
import string

# Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the webpage
driver.get("https://www.nutritionix.com/")  # Replace with the URL of your desired webpage
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'ui-select-toggle')]")))
element.click()
search_query = "paneer butter masala"
search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
search_input.send_keys(search_query)
import time
time.sleep(1)
search_input.send_keys(Keys.ENTER)
import time
time.sleep(10)
current_url = driver.current_url
driver.get(driver.current_url) 

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.item-link'))
)

h4_element = element.find_element(By.TAG_NAME, 'h4')
h4_value = h4_element.text
# print(h4_value)
# Click on the <a> element
element.click()

time.sleep(10)
# print(driver.current_url)
current_url = driver.current_url
driver.quit()
nutrient=tryingscrap2.websitescrapper(current_url)
# nutrients=[]
# for i in range(0,len(nutrient)):
#     nutrients.append(nutrient[i].get_text())
nutrient=nutrient.split('<span itemprop="servingSize">',1)[1]
# write nutrient to a file
# f1=open("nutrient.txt","w")
# f1.write(nutrient)
# f1.close()
# Split the string into a list of words
words = nutrient.split()
nutrients={}
# Get the first word
serving_size = words[0]
serving_size+='g'
# serving_size
nutrient=nutrient.split('<div class="nf-item-name block">',1)[1]
words = nutrient.split('\n')
name=words[1].strip()
nutrients['name']=name
nutrients['serving_size']=serving_size
# name
nutrient = nutrient.split('<span class="nf-pr" itemprop="calories">',1)[1]
words = nutrient.split('\n')
calories=words[1].strip()
nutrients['calories']=calories
# calories
nutrient = nutrient.split('<span class="" itemprop="fatContent">',1)[1]
words = nutrient.split('\n')
tfat=words[1].strip()+'g'
nutrients['total_fat']=tfat
# tfat
nutrient = nutrient.split('<span class="" itemprop="saturatedFatContent">',1)[1]
words = nutrient.split('\n')
sfat=words[1].strip()+'g'
nutrients['saturated_fat']=sfat
# sfat
nutrient = nutrient.split('<span class="" itemprop="transFatContent">',1)[1]
words = nutrient.split('\n')
trfat=words[1].strip()+'g'
nutrients['trans_fat']=trfat
# trfat
nutrient = nutrient.split('<span class="" itemprop="">',1)[1]
words = nutrient.split('\n')
polyfat=words[1].strip()+'g'
nutrients['polyunsaturated_fat']=polyfat
# polyfat
nutrient = nutrient.split('<span class="" itemprop="">',1)[1]
words = nutrient.split('\n')
monofat=words[1].strip()+'g'
nutrients['monounsaturated_fat']=monofat
# monofat
nutrient = nutrient.split('<span class="" itemprop="cholesterolContent">',1)[1]
words = nutrient.split('\n')
chol=words[1].strip()+'mg'
nutrients['cholesterol']=chol
# chol
nutrient = nutrient.split('<span class="" itemprop="sodiumContent">',1)[1]
words = nutrient.split('\n')
sod=words[1].strip()+'mg'
nutrients['sodium']=sod
# sod
nutrient = nutrient.split('<span class="" itemprop="carbohydrateContent">',1)[1]
words = nutrient.split('\n')
carb=words[1].strip()+'g'
nutrients['carbohydrate']=carb
# carb
nutrient = nutrient.split('<span class="" itemprop="fiberContent">',1)[1]
words = nutrient.split('\n')
fib=words[1].strip()+'g'
nutrients['fiber']=fib
# fib
nutrient = nutrient.split('<span class="" itemprop="sugarContent">',1)[1]
words = nutrient.split('\n')
sug=words[1].strip()+'g'
nutrients['sugar']=sug
# sug
nutrient = nutrient.split('<span class="" itemprop="proteinContent">',1)[1]
words = nutrient.split('\n')
pro=words[1].strip()+'g'
nutrients['protein']=pro
# pro
nutrient = nutrient.split('<span class="" itemprop="vitaminDContent">',1)[1]
words = nutrient.split('\n')
vitd=words[1].strip()+'mcg'
nutrients['vitamin_d']=vitd
# vitd
nutrient = nutrient.split('<span class="" itemprop="calciumContent">',1)[1]
words = nutrient.split('\n')
cal=words[1].strip()+'mg'
nutrients['calcium']=cal
# cal
nutrient = nutrient.split('<span class="" itemprop="ironContent">',1)[1]
words = nutrient.split('\n')
ir=words[1].strip()+'mg'
nutrients['iron']=ir
# ir
nutrient = nutrient.split('<span class="" itemprop="potassiumContent">',1)[1]
words = nutrient.split('\n')
pot=words[1].strip()+'mg'
nutrients['potassium']=pot
# pot
nutrient = nutrient.split('<span class="" itemprop="caffeineContent">',1)[1]
words = nutrient.split('\n')
caf=words[1].strip()
nutrients['caffeine']=caf
# caf 
print(nutrients)
# print(nutrient)
# driver.implicitly_wait(10)  # Wait for 10 seconds (adjust as needed)

# driver.quit()
