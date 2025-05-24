string = "https://www.zillow.com/port-orchard-wa-98367/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A47.569283357135156%2C%22south%22%3A47.377367302695376%2C%22east%22%3A-122.49415891943359%2C%22west%22%3A-122.8134490805664%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A99754%2C%22regionType%22%3A7%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A4%2C%22max%22%3Anull%7D%2C%22baths%22%3A%7B%22min%22%3A2%2C%22max%22%3Anull%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
trial = string.split("%22")
index = 0
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

