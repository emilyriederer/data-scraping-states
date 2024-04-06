from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://mvic.sos.state.mi.us/votehistory/Index?type=C&electionDate=11-8-2022"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find("div", id = "tab-target-voterTurnout")

data = []
rows = table.find_all("div", recursive = False)

# iterate over rows excluding first (header) and last (total)
for r in range(1, len(rows) - 1): 

  row = rows[r]
  vals = [d.get_text() for d in row.find_all("div", recursive = False)]
  vals[1] = int(vals[1].replace(',',''))
  data.append(vals)
  
# save resulting data
df = pd.DataFrame(data, columns = ['county','n_votes'])
df.to_csv('data/mi.csv', index = False)
