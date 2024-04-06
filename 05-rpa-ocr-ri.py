import cv2
import pytesseract
from playwright.sync_api import sync_playwright
import time
import re
import pandas as pd

# It's better to have Tessract in your PATH
# But alternatively, you can hardcode the path here
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\emily\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

with sync_playwright() as p:

  # set up
  browser = p.firefox.launch()
  context = browser.new_context(accept_downloads = True)
  page = context.new_page()

  # take screenshot of dashboard
  page.goto('https://app.powerbigov.us/view?r=eyJrIjoiMGEwN2E0MzUtOTA0OC00ZDA3LThjMTItZDZhYTBjYjU5ZjhjIiwidCI6IjJkMGYxZGI2LWRkNTktNDc3Mi04NjVmLTE5MTQxNzVkMDdjMiJ9')
  page.wait_for_load_state(state = 'networkidle')
  time.sleep(30)
  page.screenshot(path = 'data/ri.png')
  
  # cleanup
  page.close()
  context.close()
  browser.close()

# extract text from screenshot
img = cv2.imread('data/ri.png')
text = pytesseract.image_to_string(img)
n_tot = re.search('Total Voters to Date\n\n(\d+)', text.replace(',','')).group(1)
n_mail = re.search('BOE\n\n(\d+)', text.replace(',','')).group(1)

# write output
df = pd.DataFrame([[n_tot, n_mail]], columns = ['n_tot','n_mail'])
df.to_csv('data/ri.csv', index = False)