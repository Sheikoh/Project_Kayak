import scrapy

class BookingSpider(scrapy.Spider):
    name = "Booking_data"
    start_urls = ["https://www.booking.com/searchresults.html?ss=Lyon"]

    web_booking = {"form_booking" : ["div[data-testid='property-card-container']",''],
           "name": ["div[data-testid='title']::text", ".getall()"],
           "url" : ["a[data-testid='title-link']::attr(href)", "get()"]}

    def get_data(self, hotel, web_booking):
        for key, value in web_booking.items():
            method
            yield {
                key: hotel.css(value[0]).get()
            }
    

    def parse(self, response, web_booking):
        hotels = response.css("div[data-testid='property-card-container']")
        print('test')
        print(hotels)
        for hotel in hotels:
            yield {

                "hotel_name" : hotel.css("div[data-testid='title']::text").get(),
                "hotel_url" : hotel.css("a[data-testid='title-link']::attr(href)").get()
                
            }
        