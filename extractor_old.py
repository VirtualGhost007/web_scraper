from audioop import error


def data_extractor():
    import pandas as pd
    from datetime import datetime
    import openpyxl
    import json
    from bs4 import BeautifulSoup
    with open("page.html") as response:

        web_page = response

        soup = BeautifulSoup(web_page, "html.parser")
        address_list = []
        price_list = []
        bd_list = []
        ba_list = []
        sqft_list = []
        url_list = []
        geo_list = []
        test = soup.find_all("script")
        print(test[2])

        for i in test:
            try:
                data = json.loads(i.text)
                print(data['geo']['latitude'])
                geo_list.append(f"latitude {data['geo']['latitude']} longitude {data['geo']['longitude']}")
            except KeyError:
                geo_list.append("latitude None longitude None")
                continue


        for link in soup.find_all("a"):
            url = link.get("href")
            if url in url_list:
                continue
            if "https" in url:
                url_list.append(url)
            else:
                continue

        for area in soup.find_all("b"):
            no = area.text
            type_area = area.next_sibling.next_sibling.text
            if type_area == "bds":
                bd_list.append(no + type_area)
            elif type_area == "ba":
                ba_list.append(no + type_area)
            elif type_area == "sqft":
                sqft_list.append(no + type_area)
            else:
                continue

        for price in soup.find_all("span"):
            price1 = price.text
            if "$" in price1:
                print(price1)
                price_list.append(price1)
            else:
                continue

        for address in soup.find_all("address"):
            address1 = address.text.strip()
            address_list.append(address1)

    i = 0
    for price in price_list:
        if "bds" in price:
            price_list.append(price)
            price_list.append(price_list[i + 1])
            price_list.append(price_list[i + 2])
            price_list.pop(i)
            price_list.pop(i + 1)
            price_list.pop(i + 2)
            address_list.append(address_list[i])
            address_list.append(address_list[i])
            address_list.append(address_list[i])
            address_list.pop(i)
            geo_list.append(geo_list[i])
            geo_list.append(geo_list[i])
            geo_list.append(geo_list[i])
            geo_list.pop(i)
            break
        i += 1

    diff = len(price_list) - len(ba_list)
    for j in range(diff):
        ba_list.append("None")
        bd_list.append("None")
        sqft_list.append("None")

    final = [('Address', 'Bedrooms', 'Bathrooms', 'Sqft Area', 'Price', 'Url')]
    print(len(geo_list))
    print(len(url_list), len(price_list), len(address_list))
    for i in range(len(price_list)):
        final.append((address_list[i], bd_list[i], ba_list[i], sqft_list[i], price_list[i], url_list[i]))

    current_date = datetime.now().strftime("%d-%m-%Y")

    pd.DataFrame(final).to_excel(f'{current_date}.xlsx', header=False, index=False)
data_extractor()