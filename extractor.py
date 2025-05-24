def extracting(final, string):
    import pytz
    from datetime import datetime
    from scraper import scraping
    from parcel import parcel_scraper
    file = scraping(string)
    data = file["cat1"]["searchResults"]["mapResults"]
    price_list = []
    bds_list = []
    ba_list = []
    address_list = []
    area_list = []
    geo_list = []
    zestimates_list = []
    rent_zest_list = []
    days_ago = []
    url_list = []
    parcel_id = []
    year_built = []

    PST = pytz.timezone("US/Pacific")
    datetime_pst = datetime.now(PST)
    current_time = datetime_pst.strftime("%Y-%m-%d %H:%M:%S")

    for i in range(len(data)):
        if "zpid" in data[i]:
            wanted = data[i]
        else:
            continue
        price_list.append(wanted["price"])
        address_list.append(wanted["address"])
        part = wanted["address"].split(" ")
        need = f"{part[0]}+{part[1]}+{part[2]}"
        url1 = f"https://psearch.kitsap.gov/pdetails/Default?parcel={need}&type=site"
        # print(url1)
        parcel_scraper(url1, year_built, parcel_id)
        # print(year_built)
        # print(parcel_id)
        bds_list.append(wanted["beds"])
        ba_list.append(wanted["baths"])
        area_list.append(wanted["area"])
        geo_list.append(f"Latitude {wanted["latLong"]["latitude"]} Longitude {wanted["latLong"]["longitude"]}")
        # if "text" in wanted["variableData"]:
        #     days_ago.append(wanted["variableData"]["text"])
        # else:
        #     days_ago.append("None")
        url_list.append(f"https://www.zillow.com{wanted["detailUrl"]}")
        if "zestimate" in wanted["hdpData"]["homeInfo"]:
            zestimates_list.append(wanted["hdpData"]["homeInfo"]["zestimate"])
        else:
            zestimates_list.append("None")
        if "rentZestimate" in wanted["hdpData"]["homeInfo"]:
            rent_zest_list.append(wanted["hdpData"]["homeInfo"]["rentZestimate"])
        else:
            rent_zest_list.append("None")
        days_ago.append("%.2f" % (wanted["hdpData"]["homeInfo"]["timeOnZillow"] / 86400000))

    for i in range(len(price_list)):
        final.append((address_list[i], bds_list[i], ba_list[i], area_list[i], geo_list[i], price_list[i], zestimates_list[i], rent_zest_list[i], url_list[i], days_ago[i], parcel_id[i], year_built[i], current_time))

