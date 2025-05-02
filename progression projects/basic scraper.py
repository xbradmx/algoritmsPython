import requests
from bs4 import BeautifulSoup

url = str(input("Enter your url here:"))

response = requests.get(url)
response.raise_for_status()  ##for bad requests 

soup = BeautifulSoup(response.content, "html.parser") 

#attempting to just get phone number and email

refs = soup.find_all("a")

for reference in refs:
  print(reference.get('href'))


