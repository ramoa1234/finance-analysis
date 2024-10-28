import requests

cookies = {
    'zguid': '24|%249004da79-092b-4cec-96e5-657833435e30',
    'zjs_anonymous_id': '%229004da79-092b-4cec-96e5-657833435e30%22',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%226ae4b8bd-2c2a-4ec4-926a-743dc82ae772%22',
    'zgsession': '1|94ecc9a3-c067-4b01-8fc4-4c4afb4074b6',
    'JSESSIONID': '4D0FFC7C3C881164EA3606EB78C956ED',
    'AWSALB': '1o9YQjpIelkBjN+D65hidGwDOgqZ8coAu4p1MtBiem+dm/x5NmZnRvlAqfITMW5b1GXu2+vdk95DotKRDk0DiV5ghyrCKuCYuLVNLeGJXW1YVpAYpNPRNDp7uPfd',
    'AWSALBCORS': '1o9YQjpIelkBjN+D65hidGwDOgqZ8coAu4p1MtBiem+dm/x5NmZnRvlAqfITMW5b1GXu2+vdk95DotKRDk0DiV5ghyrCKuCYuLVNLeGJXW1YVpAYpNPRNDp7uPfd',
    'search': '6|1732649629233%7Crect%3D25.772098281544988%2C-80.17825747607421%2C25.7465114875915%2C-80.20915652392577%26rid%3D55477%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26listPriceActive%3D1%26type%3Dcondo%2Capartment%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26excludeNullAvailabilityDates%3D0%26isRoomForRent%3D0%26isEntirePlaceForRent%3D1%26ita%3D0%26stl%3D0%26fur%3D0%26os%3D0%26ca%3D0%26np%3D0%26hasDisabledAccess%3D0%26hasHardwoodFloor%3D0%26areUtilitiesIncluded%3D0%26highSpeedInternetAvailable%3D0%26elevatorAccessAvailable%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0955477%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'zguid=24|%249004da79-092b-4cec-96e5-657833435e30; zjs_anonymous_id=%229004da79-092b-4cec-96e5-657833435e30%22; zjs_user_id=null; zg_anonymous_id=%226ae4b8bd-2c2a-4ec4-926a-743dc82ae772%22; zgsession=1|94ecc9a3-c067-4b01-8fc4-4c4afb4074b6; JSESSIONID=4D0FFC7C3C881164EA3606EB78C956ED; AWSALB=1o9YQjpIelkBjN+D65hidGwDOgqZ8coAu4p1MtBiem+dm/x5NmZnRvlAqfITMW5b1GXu2+vdk95DotKRDk0DiV5ghyrCKuCYuLVNLeGJXW1YVpAYpNPRNDp7uPfd; AWSALBCORS=1o9YQjpIelkBjN+D65hidGwDOgqZ8coAu4p1MtBiem+dm/x5NmZnRvlAqfITMW5b1GXu2+vdk95DotKRDk0DiV5ghyrCKuCYuLVNLeGJXW1YVpAYpNPRNDp7uPfd; search=6|1732649629233%7Crect%3D25.772098281544988%2C-80.17825747607421%2C25.7465114875915%2C-80.20915652392577%26rid%3D55477%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26listPriceActive%3D1%26type%3Dcondo%2Capartment%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26singlestory%3D0%26housing-connector%3D0%26parking-spots%3Dnull-%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26excludeNullAvailabilityDates%3D0%26isRoomForRent%3D0%26isEntirePlaceForRent%3D1%26ita%3D0%26stl%3D0%26fur%3D0%26os%3D0%26ca%3D0%26np%3D0%26hasDisabledAccess%3D0%26hasHardwoodFloor%3D0%26areUtilitiesIncluded%3D0%26highSpeedInternetAvailable%3D0%26elevatorAccessAvailable%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0955477%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09',
    'dnt': '1',
    'origin': 'https://www.zillow.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zillow.com/brickell-miami-fl/apartments/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

json_data = {
    'searchQueryState': {
        'pagination': {},
        'isMapVisible': False,
        'mapBounds': {
            'west': -80.20915652392577,
            'east': -80.17825747607421,
            'south': 25.7465114875915,
            'north': 25.772098281544988,
        },
        'regionSelection': [
            {
                'regionId': 55477,
                'regionType': 8,
            },
        ],
        'filterState': {
            'isForRent': {
                'value': True,
            },
            'isForSaleByAgent': {
                'value': False,
            },
            'isForSaleByOwner': {
                'value': False,
            },
            'isNewConstruction': {
                'value': False,
            },
            'isComingSoon': {
                'value': False,
            },
            'isAuction': {
                'value': False,
            },
            'isForSaleForeclosure': {
                'value': False,
            },
            'isSingleFamily': {
                'value': False,
            },
            'isTownhouse': {
                'value': False,
            },
            'isMultiFamily': {
                'value': False,
            },
            'isLotLand': {
                'value': False,
            },
            'isManufactured': {
                'value': False,
            },
        },
        'isListVisible': True,
        'mapZoom': 15,
    },
    'wants': {
        'cat1': [
            'listResults',
        ],
    },
    'requestId': 3,
    'isDebugRequest': False,
}

response = requests.put('https://www.zillow.com/async-create-search-page-state', cookies=cookies, headers=headers, json=json_data)
print(response.json())