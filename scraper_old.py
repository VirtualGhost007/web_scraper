def scraper(url=str):
    from bs4 import BeautifulSoup
    import requests

    url = "https://www.zillow.com/port-orchard-wa-98367/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.96205766113282%2C%22east%22%3A-122.32347733886719%2C%22south%22%3A47.3034414025953%2C%22north%22%3A47.690809086082666%7D%2C%22mapZoom%22%3A11%2C%22usersSearchTerm%22%3A%22Port%20Orchard%20WA%2098367%2C%20Port%20Orchard%20WA%2098366%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A99754%2C%22regionType%22%3A7%7D%2C%7B%22regionId%22%3A99753%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A4%2C%22max%22%3Anull%7D%2C%22baths%22%3A%7B%22min%22%3A2%2C%22max%22%3Anull%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
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

    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    wanted = soup.find("div", "result-list-container")
    wanted = str(wanted)
    with open("page.html", "w") as html:
        html.write(wanted)