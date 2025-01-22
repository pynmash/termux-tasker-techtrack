import requests
from bs4 import BeautifulSoup

URL = "https://www.civil-service-careers.gov.uk/professions/working-in-digital-data-and-technology/techtrack"
phrase = "Register here to find out when applications open for the second cohort of Software Developer in early 2025."


def phrase_exists(links, phrase):
    for link in links:
        if phrase in link:
            return True
    return False


response = requests.get(url=URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")

links = [link for link in soup.find_all("a")]

result = phrase_exists(links, phrase)

if result:
    print(f'Still says "{phrase}"')
else:
    print("The text changed! Applications might be open")
