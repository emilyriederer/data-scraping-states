from playwright.sync_api import sync_playwright
import datetime

def retrieve_date(date, page):

  # navigate to date-specific page 
  target_date = datetime.datetime.strptime(date, '%Y%m%d')
  target_date_str = target_date.strftime('%Y-%m-%d 00:00:00.0')
  target_file = 'tx-' + target_date.strftime('%Y%m%d') + '.csv'
  
  # pick election
  page.goto('https://earlyvoting.texas-election.com/Elections/getElectionDetails.do')
  page.select_option('#idElection', label = "2020 NOVEMBER 3RD GENERAL ELECTION")
  page.click('#electionsInfoForm button')
  page.wait_for_selector('#selectedDate')
  
  # pick day
  page.select_option('#selectedDate', value = target_date_str)
  page.click('#electionsInfoForm button:nth-child(2)')
  page.wait_for_selector('"Generate Statewide Report"')

  # download report  
  with page.expect_download() as download_info:
    page.click('"Generate Statewide Report"')
  download = download_info.value
  download.save_as(f'data/{target_file}')

with sync_playwright() as p:

  browser = p.firefox.launch()
  # want to see it in action? Switch to firefox.launch(headless=False, slow_mo=50)
  context = browser.new_context(accept_downloads = True)
  page = context.new_page()
  
  dates = ['20201020','20201021','20201022']
  for d in dates:
    retrieve_date(d, page)

  # cleanup
  page.close()
  context.close()
  browser.close()