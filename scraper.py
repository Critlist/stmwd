import requests
from bs4 import BeautifulSoup

url = 'URL_OF_THE_PAGE'  # Replace with the actual URL
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

# Example: Extracting a table
table = soup.find('table', {'class': 'GroupBox1'})
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        print(cell.get_text(strip=True))
        
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get('URL_OF_THE_PAGE')  # Replace with the actual URL

# Example: Fill a form and submit
form = driver.find_element(By.NAME, 'HeaderForm')
submit_button = form.find_element(By.NAME, 'submit')
submit_button.click()

# Wait for the next page to load and extract data
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'GroupBox1'))
)

# Extract table data
table = driver.find_element(By.CLASS_NAME, 'GroupBox1')
rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    for cell in cells:
        print(cell.text)

# Close the browser
driver.quit()