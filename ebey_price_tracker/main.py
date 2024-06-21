import datetime
import requests
from bs4 import BeautifulSoup
import csv
import send_mail
url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355?Brand=Apple&Color=Purple&Model=Apple%2520iPhone%252014%2520Pro%2520Max&rt=nc"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,'lxml')
today = datetime.date.today()
file_name = f"{today}.csv"
with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write headers to the CSV file
    writer.writerow(['Title', 'Price', 'Shipping Cost', 'Number of Bids', 'Ending Time', 'Rating Stars', 'Number of Reviews'])
    
    # Find all listings
    lists = soup.find_all('li', class_='s-item s-item--large')
    
    for item in lists:
        # Find the title of the listing
        listing_title_elem = item.find('h3', class_='s-item__title')
        listing_title = listing_title_elem.text.strip() if listing_title_elem else 'N/A'

        # Find the rating and reviews section
        rating_reviews_div = item.find('div', class_='b-rating s-item__reviews')
        
        if rating_reviews_div:
            # Extract the rating (stars)
            rating_stars_div = rating_reviews_div.find('div', class_='star-rating b-rating__rating-star')
            stars_count = len(rating_stars_div.find_all('svg')) if rating_stars_div else 'N/A'
            
            # Extract the number of reviews
            rating_count_span = rating_reviews_div.find('span', class_='b-rating__rating-count')
            reviews_count = rating_count_span.text.strip('()') if rating_count_span else 'N/A'
        else:
            stars_count = 'N/A'
            reviews_count = 'N/A'

        # Find price, shipping cost, number of bids, and ending time
        price_span = item.find('span', class_='s-item__price')
        price = price_span.text.strip() if price_span else 'N/A'

        shipping_cost_span = item.find('span', class_='s-item__shipping')
        shipping_cost = shipping_cost_span.text.strip() if shipping_cost_span else 'N/A'

        bids_span = item.find('span', class_='s-item__bidCount')
        number_of_bids = bids_span.text if bids_span else 'N/A'

        ending_time_parent = item.find('span', class_='s-item__time-left')
        ending_time = ending_time_parent.text.strip() if ending_time_parent else 'N/A'

        # Print or process any of the extracted data here
        # print(f"Title: {listing_title}")
        # print(f"Price: {price}")
        # print(f"Shipping Cost: {shipping_cost}")
        # print(f"Number of Bids: {number_of_bids}")
        # print(f"Ending Time: {ending_time}")
        # print(f"Rating Stars: {stars_count}")
        # print(f"Number of Reviews: {reviews_count}")
        # print("----------------------------------")
        
        # # Write the row to the CSV file
        writer.writerow([
            listing_title,
            price,
            shipping_cost,
            number_of_bids,
            ending_time,
            stars_count,
            reviews_count
        ])
send_mail.send(filename=file_name)

# File will be automatically closed after exiting the 'with' block