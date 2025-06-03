import requests
from bs4 import BeautifulSoup
import time


def num_email_func():
  url = str(input("Enter your url here:"))
  print('\n')
  #url =str("https://marketgatelancaster.co.uk/stores/ ") # just for tests


  headers = {'User-Agent': 'Mozilla/5.0'}
  response = requests.get(url, headers=headers)
  time.sleep(1.5)
  
  response.raise_for_status()  ##for bad requests 

  soup = BeautifulSoup(response.content, "html.parser") 

  #attempting to just get phone number and email

  refs = soup.find_all("span")

  

  for x in refs:
    if True:
      print(x.get_text(strip=True))

while True:
  repeat_scraper = str(input('would you like to enter a website?(y/n): '))
  if repeat_scraper.lower() == 'y':
    print('\n')
    num_email_func()
    print('\n')
  elif repeat_scraper.lower() == 'n':
    print('\n')
    print('---Now Exiting program---')
    print('\n')
    break
  else:
    continue
