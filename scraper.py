import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json



# this is the landing page for the Buffalo C on the rrc website. I need to document the process of getting to this page and add every backend query that is made to get to this page.
# drillDownQueryAction.do?name=BUFFALO%2BC&fromPublicQuery=Y&univDocNo=497360370


url = 'URL_OF_THE_PAGE'  # Replace with the actual URL

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Example: Extracting a table
table = soup.find('table', {'class': 'GroupBox1'})
rows = table.find_all('tr')

for row in rows:
	cells = row.find_all('td')
	for cell in cells:
		print(cell.get_text(strip=True))

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

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

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

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

data = []
for row in rows:
	cells = row.find_elements(By.TAG_NAME, 'td')
	row_data = {}
	for i, cell in enumerate(cells):
		row_data[f'column_{i}'] = cell.text
	data.append(row_data)

# Convert the list of dictionaries to JSON
json_data = json.dumps(data, indent=4)

# Save the JSON to a file
with open('data.json', 'w') as json_file:
	json_file.write(json_data)

# Close the browser
driver.quit()
