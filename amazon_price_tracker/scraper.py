import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.in/ASUS-ZenBook-i7-1165G7-Graphics-UX425EA-BM701TS/dp/B08M4SWRR5/ref=pd_sbs_147_13?_encoding=UTF8&pd_rd_i=B08M4SWRR5&pd_rd_r=314ea757-0eb1-4e98-9e49-29d7bfdaf749&pd_rd_w=pCPnf&pd_rd_wg=xBnEB&pf_rd_p=758bfbc8-a8f2-4456-bf65-ae5d502eac06&pf_rd_r=271BAAF0ZD8ANXYENT9T&psc=1&refRID=271BAAF0ZD8ANXYENT9T'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}



def check_price(desired_price):
	page = requests.get(URL,headers = headers)
	soup = BeautifulSoup(page.content,'html.parser')

	# print(soup.prettify())

	title = soup.find(id = 'productTitle').get_text()
	price = soup.find(id = 'priceblock_ourprice').get_text()
	price = price.replace(',', '')
	converted_price =  float(price[2:8])

	# print(title.strip())
	# print(converted_price)

	if converted_price <= desired_price:
		send_mail()


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	server.login('adithyabhatpr@gmail.com','<password>')

	subject = 'Price of product has fallen'
	body = 'Check the amazon link: https://www.amazon.in/ASUS-ZenBook-i7-1165G7-Graphics-UX425EA-BM701TS/dp/B08M4SWRR5/ref=pd_sbs_147_13?_encoding=UTF8&pd_rd_i=B08M4SWRR5&pd_rd_r=314ea757-0eb1-4e98-9e49-29d7bfdaf749&pd_rd_w=pCPnf&pd_rd_wg=xBnEB&pf_rd_p=758bfbc8-a8f2-4456-bf65-ae5d502eac06&pf_rd_r=271BAAF0ZD8ANXYENT9T&psc=1&refRID=271BAAF0ZD8ANXYENT9T'
	msg = f'Subject: {subject}\n\n{body}'

	server.sendmail(
		'adithyabhatpr@gmail.com',
		'adithyabhatpr@gmail.com',
		msg
	)

	print("hey....email has been sent!")

	server.quit()



desired_price = 90000.0

while True:
	check_price(desired_price)
	time.sleep(3600) # check every hour
