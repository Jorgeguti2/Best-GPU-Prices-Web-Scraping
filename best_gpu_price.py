from bs4 import BeautifulSoup
import requests
import re

gpu_Name = input("What GPU are you searching for?\n")

newegg_Url = f"https://www.newegg.com/p/pl?d={gpu_Name}&N=4131"

newegg_Page = requests.get(newegg_Url).text

doc = BeautifulSoup(newegg_Page, "html.parser")

page_Text = doc.find(class_="list-tool-pagination-text").strong.text
print(page_Text)
