import requests
from bs4 import BeautifulSoup

url = 'https://iolap.talentlyft.com/blog/iolap-academy-2022-faq-nv?fbclid=IwAR0ddXX1IAUuv0wDG4-CKZoHBgSao9X6z12FSIHyO2kpBzpOlfwyh6oyTQA'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# Extracting title
title = soup.title.text.strip()

# Extracting description
description_tag = soup.find('meta', attrs={"name": "description"})
description = description_tag["content"] if description_tag else "N/A"

# Extracting image URL
image_tag = soup.find('meta', attrs={"itemprop": "image"})
image_url = image_tag["content"] if image_tag else "N/A"

# Extracting Twitter card information
twitter_card_tag = soup.find('meta', attrs={"name": "twitter:card"})
twitter_card = twitter_card_tag["content"] if twitter_card_tag else "N/A"

twitter_title_tag = soup.find('meta', attrs={"name": "twitter:title"})
twitter_title = twitter_title_tag["content"] if twitter_title_tag else "N/A"

twitter_description_tag = soup.find('meta', attrs={"name": "twitter:description"})
twitter_description = twitter_description_tag["content"] if twitter_description_tag else "N/A"

twitter_image_tag = soup.find('meta', attrs={"name": "twitter:image"})
twitter_image = twitter_image_tag["content"] if twitter_image_tag else "N/A"

# Extracting Open Graph (OG) information
og_title_tag = soup.find('meta', attrs={"property": "og:title"})
og_title = og_title_tag["content"] if og_title_tag else "N/A"

og_url_tag = soup.find('meta', attrs={"property": "og:url"})
og_url = og_url_tag.get("content") if og_url_tag else "N/A"

og_image_tag = soup.find('meta', attrs={"property": "og:image"})
og_image = og_image_tag["content"] if og_image_tag else "N/A"

og_description_tag = soup.find('meta', attrs={"property": "og:description"})
og_description = og_description_tag["content"] if og_description_tag else "N/A"

# Write the extracted data to a text file
with open('extracted_data.txt', 'w') as file:
    file.write(f"Title: {title}\n")
    file.write(f"Description: {description}\n")
    file.write(f"Image URL: {image_url}\n")
    file.write(f"Twitter Card: {twitter_card}\n")
    file.write(f"Twitter Title: {twitter_title}\n")
    file.write(f"Twitter Description: {twitter_description}\n")
    file.write(f"Twitter Image: {twitter_image}\n")
    file.write(f"OG Title: {og_title}\n")
    file.write(f"OG URL: {og_url}\n")
    file.write(f"OG Image: {og_image}\n")
    file.write(f"OG Description: {og_description}\n")

print("Data written to extracted_data.txt")

