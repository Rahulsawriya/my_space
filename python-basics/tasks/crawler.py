import csv
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8","Accept-Encoding": "gzip, deflate, br"}
site = 'https://www.mouser.in'
response = requests.get("https://www.mouser.in/Electronic-Components/", headers=headers)
if response:
    #print('Success!')
    soup = BeautifulSoup(response.text, "html.parser")
    plist = soup.find("div", {"id": "tblSplitCategories"})
    for item in plist.find_all("div", {"class": "light-grey-panel"}):
    	#print(item.find()
    	item_href = item.find("div", {"class": "panel-heading"}).find('a').attrs['href']
    	item_href = site + str(item_href)
    	item_value = str(item.find("div", {"class": "panel-heading"}).find('a').find('h2').text)
    	print(item_value)
    	print(item_href)
    	print("^^"*50)
    	for sub_item in item.find_all("div", {"class": "sub-category-section"}):
    		sub_item_value = str(sub_item.find("div", {"class": "sub-category-title"}).find('h3').text)
    		sub_item_href = str(sub_item.find("div", {"class": "sub-category-title"}).find('a').attrs['href'])
    		sub_item_href = site + sub_item_href
    		print(sub_item_href)
    		print(sub_item_value)
    		#print(sub_item)
    		print("@@"*50)
    		for sub_item1 in sub_item.find_all('ul'):
    			for sub_item2 in sub_item1.find_all('li'):
    				sub_item2_href = str(sub_item2.find('a').attrs['href'])
    				sub_item2_href = site + sub_item2_href
    				sub_item2_value = str(sub_item2.find('a').find(text=True, recursive=False))
    				print(sub_item2_href)
    				print(sub_item2_value)
    				print("00))))))")
    			#print("&&"*50)
    		#print('%'*50)"""
    	if item.find('div', {"class": "top-category-list"}):
    		main_list = item.find('div', {"class": "top-category-list"})
    		#print(main_list)
    		for main_sub in main_list.find_all('ul'):
    			for main_sub1 in main_sub.find_all('li'):
    				main_sub1_href = str(main_sub1.find('a').attrs['href'])
    				main_sub1_href = site + main_sub1_href
    				main_sub1_value = str(main_sub1.find('a').find(text=True, recursive=False))
    				print(main_sub1_value)
	    			print(main_sub1_href)
	    			print("##"*50)
    	#print)
    	"""for main_sub in main_list.find('ul'):
    		print(main_sub)
    		print("$$"*50)"""
    	print("-----------------@@@"*30)
else:
    print('An error has occurred.')