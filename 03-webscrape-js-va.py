from playwright.sync_api import sync_playwright
import datetime
import re
import pandas as pd

def retrieve_county(county, page):

  # navigate to county-specific page
  url_stub = county.lower()
  url = f'https://www.vpap.org/elections/early-voting/2023-november-general-election/locality-{url_stub}-county-va/'
  page.goto(url)
  
  # iterate over days on bar chart
  county_records = []

  for n in range(1,75):

    print(n)
  
    # extract values from chart tooltip
    selector = f'#timeline g.popovers rect:nth-of-type({n})'
    try:
      date = page.get_attribute(selector, 'data-original-title')
      vals = page.get_attribute(selector, 'data-content')
    except Exception:
      break

    if vals is None:
      break

    # process data into tabular structure
    template_string = 'Voted In Person: (\d+)<br />Voted by Mail: (\d+)<br />Total: (\d+)' 
    vals_method = re.search(template_string, vals.replace(',',''))
    date_parse = datetime.datetime.strptime(date + ' 2022', '%b %d %Y').strftime('%Y-%m-%d')
    record = [county, 
              date_parse, 
              vals_method.group(1), 
              vals_method.group(2)]
    county_records.append(record)

  return county_records

with sync_playwright() as p:

  # set up
  browser = p.firefox.launch()
  context = browser.new_context(accept_downloads = True)
  page = context.new_page()
  
  # iterate over counties
  records = []
  county = ['Accomack', 'Albemarle', 'Alexandria']
  for c in county:
    records += retrieve_county(c, page)
  
  # save resulting data
  col_names = ['county', 'date', 'n_mail', 'n_poll']
  df = pd.DataFrame(records, columns = col_names)
  df.to_csv('data/va.csv', index = False)

  # cleanup
  page.close()
  context.close()
  browser.close()