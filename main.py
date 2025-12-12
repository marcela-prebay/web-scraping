from bs4 import BeautifulSoup
import requests
import time

def find_books():
    html_text = requests.get('https://books.toscrape.com/catalogue/category/books/romance_8/index.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    books = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for index, book in enumerate(books):
        book_name = book.find('h3').text
        price = book.find('p', class_ = 'price_color').text.replace('Â', '')
        link = book.article.h3.a['href']
        rating = book.find('p', class_ = 'star-rating')

        if rating:
            class_list = rating['class'] 
            rating_map = {
                'One': 1,
                'Two': 2,
                'Three': 3,
                'Four': 4,
                'Five': 5
            }
            rating_text = class_list[1] 
            stars = rating_map.get(rating_text)

        with open(f'posts/{index}.txt', 'w') as f:   
            f.write(f'''
            Book: {book_name}
            Price: {price}
            Rating: {stars}
            Link: {link}
            ''')
        print(f'File saved: {index}')

if __name__ == '__main__':
    while True: 
        find_books()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

