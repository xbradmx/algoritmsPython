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

  refs = soup.find_all("a")



  #storage arrays for already found info
  is_num = []
  is_email = []

  #loop for searching all 'a' and 'hrefs
  for reference in refs:
    #print(reference.get('href'))
    href = str(reference.get('href'))
    for searcher_email in href:

  #finds emails
      if '@'  in searcher_email:
        email = href.strip()
        char_location = href.index(':')
        email = href[char_location + 1:]

  #gives email output
        if email not in is_email:
          print(f'this is an email: {email}')
          is_email.append(email)

  #finds phone numbers 
      elif any(str(digit) in href for digit in range(10)) and "javascript" not in href:
        number = href.strip()
        char_location = href.index(':')
        number = href[char_location + 1:]
        #print(f'potential phone number:{number}')


  #ensures that its not an arbitrary number 
        if (len(number) == 11 or len(number) == 10) and number not in is_num:
          print(f'this is a phone number: {number}')
          is_num.append(number)
        else:
          continue






  




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




