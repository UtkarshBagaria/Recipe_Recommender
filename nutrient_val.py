def get_nutrient_dic(q):    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import tryingscrap2
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException

    # Launch the browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the webpage
    driver.get("https://www.nutritionix.com/")  # Replace with the URL of your desired webpage
    wait = WebDriverWait(driver, 5)
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'ui-select-toggle')]")))
        element.click()
        search_query = q 
        search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
        search_input.send_keys(search_query)
        import time
        time.sleep(1)
        search_input.send_keys(Keys.ENTER)
    except:
        return None
    import time
    time.sleep(5)
    current_url = driver.current_url
    driver.get(driver.current_url) 
    try:
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.item-link'))
        )

        h4_element = element.find_element(By.TAG_NAME, 'h4')
        h4_value = h4_element.text
        # print(h4_value)
        # Click on the <a> element
        element.click()

        time.sleep(5)
    except:
        return None
    # print(driver.current_url)
    current_url = driver.current_url
    driver.quit()
    nutrient=tryingscrap2.websitescrapper(current_url)
    if nutrient==None:
        return None
    # nutrients=[]
    # for i in range(0,len(nutrient)):
    #     nutrients.append(nutrient[i].get_text())
    nutrients={}
    if('<span itemprop="servingSize">' in nutrient):
        nutrient=nutrient.split('<span itemprop="servingSize">',1)[1]
        words = nutrient.split()
        serving_size = words[0]
        serving_size+='g'
        nutrients['serving_size']=serving_size
    # serving_size
    if('<div class="nf-item-name block">' in nutrient):
        nutrient=nutrient.split('<div class="nf-item-name block">',1)[1]
        words = nutrient.split('\n')
        name=words[1].strip()
        nutrients['name']=name
    # name
    if('<span class="nf-pr" itemprop="calories">' in nutrient):
        nutrient = nutrient.split('<span class="nf-pr" itemprop="calories">',1)[1]
        words = nutrient.split('\n')
        calories=words[1].strip()
        nutrients['calories']=calories
    # calories
    if('<span class="" itemprop="fatContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="fatContent">',1)[1]
        words = nutrient.split('\n')
        tfat=words[1].strip()+'g'
        nutrients['total_fat']=tfat
    # tfat
    if('<span class="" itemprop="saturatedFatContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="saturatedFatContent">',1)[1]
        words = nutrient.split('\n')
        sfat=words[1].strip()+'g'
        nutrients['saturated_fat']=sfat
    # sfat
    if('<span class="" itemprop="transFatContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="transFatContent">',1)[1]
        words = nutrient.split('\n')
        trfat=words[1].strip()+'g'
        nutrients['trans_fat']=trfat
    # trfat
    if('<span class="" itemprop="">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="">',1)[1]
        words = nutrient.split('\n')
        polyfat=words[1].strip()+'g'
        nutrients['polyunsaturated_fat']=polyfat
    # polyfat
    if('<span class="" itemprop="">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="">',1)[1]
        words = nutrient.split('\n')
        monofat=words[1].strip()+'g'
        nutrients['monounsaturated_fat']=monofat
    # monofat
    if('<span class="" itemprop="cholesterolContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="cholesterolContent">',1)[1]
        words = nutrient.split('\n')
        chol=words[1].strip()+'mg'
        nutrients['cholesterol']=chol
    # chol
    if('<span class="" itemprop="sodiumContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="sodiumContent">',1)[1]
        words = nutrient.split('\n')
        sod=words[1].strip()+'mg'
        nutrients['sodium']=sod
    # sod
    if('<span class="" itemprop="carbohydrateContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="carbohydrateContent">',1)[1]
        words = nutrient.split('\n')
        carb=words[1].strip()+'g'
        nutrients['carbohydrate']=carb
    # carb
    if('<span class="" itemprop="fiberContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="fiberContent">',1)[1]
        words = nutrient.split('\n')
        fib=words[1].strip()+'g'
        nutrients['fiber']=fib
    # fib
    if('<span class="" itemprop="sugarContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="sugarContent">',1)[1]
        words = nutrient.split('\n')
        sug=words[1].strip()+'g'
        nutrients['sugar']=sug
    # sug
    if('<span class="" itemprop="proteinContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="proteinContent">',1)[1]
        words = nutrient.split('\n')
        pro=words[1].strip()+'g'
        nutrients['protein']=pro
    # pro
    if('<span class="" itemprop="vitaminDContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="vitaminDContent">',1)[1]
        words = nutrient.split('\n')
        vitd=words[1].strip()+'mcg'
        nutrients['vitamin_d']=vitd
    # vitd
    if('<span class="" itemprop="calciumContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="calciumContent">',1)[1]
        words = nutrient.split('\n')
        cal=words[1].strip()+'mg'
        nutrients['calcium']=cal
    # cal
    if('<span class="" itemprop="ironContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="ironContent">',1)[1]
        words = nutrient.split('\n')
        ir=words[1].strip()+'mg'
        nutrients['iron']=ir
    # ir
    if('<span class="" itemprop="potassiumContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="potassiumContent">',1)[1]
        words = nutrient.split('\n')
        pot=words[1].strip()+'mg'
        nutrients['potassium']=pot
    # pot
    if('<span class="" itemprop="caffeineContent">' in nutrient):
        nutrient = nutrient.split('<span class="" itemprop="caffeineContent">',1)[1]
        words = nutrient.split('\n')
        caf=words[1].strip()
        nutrients['caffeine']=caf
    return(nutrients)
