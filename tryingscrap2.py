def websitescrapper(ur):    
    import os
    from selenium import webdriver

    # Set the PATH environment variable to include the directory where chromedriver is located
    chromedriver_path = 'C:\\Users\\utkar\\Downloads\\chromedriver.exe'
    os.environ['PATH'] += os.pathsep + chromedriver_path

    # Instantiate the Chrome WebDriver
    driver = webdriver.Chrome()

    # Rest of your code...


    # Navigate to the webpage
    # url = "https://www.nutritionix.com/food/paneer-butter-masala"
    url = ur
    driver.get(url)

    # Wait for the page to fully load (adjust the sleep time as needed)
    import time
    time.sleep(10)

    # Get the page source (which now includes the dynamically generated content)
    html_content = driver.page_source

    # Close the browser
    driver.quit()

    # Print the HTML content
    # print(html_content)

    from bs4 import BeautifulSoup

    html_code = html_content

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_code, 'html.parser')

    # Find the main content within the body tag
    body_content = soup.find('body')

    # Get the clean HTML code of the body content
    clean_html = body_content.prettify()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(clean_html, 'html.parser')

    # print(clean_html)

    # Find the <div> tag with the specified id
    div_tag = soup.find('div', class_='label-container')

    # Get the clean HTML code of the <div> tag
    div_html = div_tag.prettify()
    # print(type(div_html))
    # import html
    # div_html=html.unescape(div_html)
    # print(type(div_html))
    # Print the clean HTML code of the <div> tag
    return div_html

