import requests
from bs4 import BeautifulSoup


def scrape_url(url):
    headers={"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    page = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="corePrice_feature_div").get_text()
    description = soup.find(id="feature-bullets").get_text()
    image = soup.find('img', class_="a-dynamic-image").attrs['src']
    priceConverted = price.split("R", 2)[:2][1]


    return {
        "title": title,
        "price": priceConverted,
        "description": description,
        "image_url": image,
        "url": url,
        "created_at": "",}
