import requests
def scraping(string):
    trial = string.split("%22")
    zip_1 = trial[0].split("/")
    index_zip = zip_1.index("www.zillow.com")
    zip_2 = zip_1[index_zip + 1].split("-")
    zip_code = int(zip_2[len(zip_2) - 1]) + 1387

    index_west = trial.index("west")
    west = (trial[index_west + 1].strip("%3A").strip("%2C")).strip("%7D")
    # west = float(west)

    index_east = trial.index("east")
    east = (trial[index_east + 1].strip("%3A").strip("%2C")).strip("%7D")
    # east = float(east)

    index_north = trial.index("north")
    north = (trial[index_north + 1].strip("%3A").strip("%2C")).strip("%7D")
    # north = float(north)

    index_south = trial.index("south")
    south = (trial[index_south + 1].strip("%3A").strip("%2C")).strip("%7D")
    # south = float(south)

    url = "https://www.zillow.com/async-create-search-page-state"

    payload = {
        "searchQueryState": {
            "pagination": {},
            "isMapVisible": True,
            "mapBounds": {
                "west": west,
                "east": east,
                "south": south,
                "north": north
            },
            "usersSearchTerm": "Port Orchard WA 98367, Port Orchard WA 98366",
            "regionSelection": [
                {
                    "regionId": zip_code,
                    "regionType": 7
                }
            ],
            "filterState": {
                "isForRent": {"value": True},
                "isForSaleByAgent": {"value": False},
                "isForSaleByOwner": {"value": False},
                "isNewConstruction": {"value": False},
                "isComingSoon": {"value": False},
                "isAuction": {"value": False},
                "isForSaleForeclosure": {"value": False},
                "beds": {
                    "min": 4,
                    "max": None
                },
                "baths": {
                    "min": 2,
                    "max": None
                },
                "isTownhouse": {"value": False}
            },
            "isListVisible": True
        },
        "wants": {"cat1": ["mapResults"]},
        "requestId": 2,
        "isDebugRequest": False
    }
    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-Ch-Ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        }

    response = requests.put(url, json=payload, headers=headers)
    return response.json()

