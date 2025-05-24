import mysql.connector
from datetime import datetime
import pytz
from extractor import extracting

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Nannu2005@",  # Replace with your password
    "database": "zillow_db"   # Replace with your database name
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()
#
# PST = pytz.timezone("US/Pacific")
# datetime_pst = datetime.now(PST)
# current_time = datetime_pst.strftime("%Y-%m-%d %H:%M:%S")

# URLs to scrape
urls = [
    "https://www.zillow.com/port-orchard-wa-98366/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.73945608056641%2C%22east%22%3A-122.4201659194336%2C%22south%22%3A47.45117673561711%2C%22north%22%3A47.64444274254075%7D%2C%22usersSearchTerm%22%3A%2298366%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A99753%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A4%2C%22max%22%3Anull%7D%2C%22baths%22%3A%7B%22min%22%3A2%2C%22max%22%3Anull%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    "https://www.zillow.com/port-orchard-wa-98367/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A47.57009408819216%2C%22south%22%3A47.3765535928562%2C%22east%22%3A-122.49415891943359%2C%22west%22%3A-122.8134490805664%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A99754%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A4%2C%22max%22%3Anull%7D%2C%22baths%22%3A%7B%22min%22%3A2%2C%22max%22%3Anull%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
]

# Loop through each URL
for string in urls:
    # Extract data
    final = [("Address", "Bedrooms", "Bathrooms", "Sqft Area", "GeoCoordinates", "Price", "Zestimate Price", "Rent Zestimate Price", "Url", "Days on Zillow", "Parcel ID", "Year Built", "ScrapedAt")]
    extracting(final, string)
    # print(final)


    # Insert data into the database only if it doesn't already exist
    insert_query = """
            INSERT INTO rent
            (Address, Bedrooms, Bathrooms, SqftArea, GeoCoordinates, Price, ZestimatePrice, RentZestimatePrice, Url, DaysOnZillow, parcel_id, year_built, ScrapedAt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            Address=VALUES(Address),
            Bedrooms=VALUES(Bedrooms),
            Bathrooms=VALUES(Bathrooms),
            SqftArea=VALUES(SqftArea),
            GeoCoordinates=VALUES(GeoCoordinates),
            Price=VALUES(Price),
            ZestimatePrice=VALUES(ZestimatePrice),
            RentZestimatePrice=VALUES(RentZestimatePrice),
            DaysOnZillow=VALUES(DaysOnZillow),
            parcel_id=VALUES(parcel_id),
            year_built=VALUES(year_built),
            ScrapedAt=VALUES(ScrapedAt)
        """
    for row in final[1:]:
        print("Inserting row:", row)# Skip header
        cursor.execute(insert_query, row)

    # Commit the transaction
    connection.commit()
    print("Data successfully saved into local MySQL database, avoiding duplicates.")

if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection closed.")