from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
from datetime import date as d
url = "http://pelotkashop.ru"

browser = webdriver.PhantomJS()


def open_web_site():

	browser.get(url)
	html = browser.page_source
	soup = BeautifulSoup(html)
	
	sidebar = soup.find('div', {'id': 'sidebar'})
	items = sidebar.findAll('div', {'class': 'recently_aricle'})

	today = d.today().strftime("%Y %m %d")
	
	with open('sexshop-{}.csv'.format(today), 'w', newline='') as csvfile:

		fieldnames = ['url', 'imgage url', 'date', 'text', 'price']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

		for item in items:
			img = item.find('img')
			if img:
				print('IMG: ' + str(img.get('src')))
				img = img.get('src')

			date = item.find('p', {'class': 'recently_date'})
			if date:
				print('DATE: ' + str(date.text))
				date = date.text

			href = item.findAll('a')
			if href:
				print('HREF: ' + str(href[-1].get('href')))
				href = href[-1].get('href')

			text = item.findAll('a')
			if text:
				print('TEXT: ' + str(text[-1].text))
				text = text[-1].text

			price = item.find('p', {'class': 'recently_price'})
			if price:
				print('PRICE: ' + str(price.text))
				price = price.text

			print('________________________________________________________')
			
			writer.writerow({
				'url': url + href,
				'imgage url': url + img,
				'date': date,
				'text': text,
				'price': price
				})

def main():
	open_web_site()
	browser.quit()


if __name__ == '__main__':
	main()