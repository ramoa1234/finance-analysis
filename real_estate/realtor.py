import requests, json

cookies = {
    'split': 'n',
    'split_tcv': '109',
    '__vst': 'a4f46f97-818b-4eb3-be89-6ac10315dcbf',
    '__bot': 'false',
    '__split': '84',
    '_lr_env_src_ats': 'false',
    'G_ENABLED_IDPS': 'google',
    'mdLogger': 'false',
    'kampyle_userid': 'e221-5cc0-2168-c6f8-7d8e-4df6-9934-1424',
    '__ssn': '8e5a4236-c9f3-4700-b16d-a65c5227a766',
    '__ssnstarttime': '1729657319',
    '_lr_retry_request': 'true',
    'criteria': 'sprefix%3D%252Fnewhomecommunities%26area_type%3Dcity%26city%3DWeston%26pg%3D1%26state_code%3DFL%26state_id%3DFL%26loc%3DWeston%252C%2520FL%26locSlug%3DWeston_FL%26county_fips%3D12011%26county_fips_multi%3D12011',
    'AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg': '1',
    'kampyleUserSession': '1729657321728',
    'kampyleUserSessionsCount': '8',
    'kampyleSessionPageCounter': '1',
    'kampyleUserPercentile': '16.957098653328995',
    'AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '-1124106680%7CMCIDTS%7C20020%7CMCMID%7C74817516618400596614988662968578924832%7CMCAID%7CNONE%7CMCOPTOUT-1729664539s%7CNONE%7CvVersion%7C5.2.0',
}

headers = {
    'accept': 'application/json, text/javascript',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'split=n; split_tcv=109; __vst=a4f46f97-818b-4eb3-be89-6ac10315dcbf; __bot=false; __split=84; _lr_env_src_ats=false; G_ENABLED_IDPS=google; mdLogger=false; kampyle_userid=e221-5cc0-2168-c6f8-7d8e-4df6-9934-1424; __ssn=8e5a4236-c9f3-4700-b16d-a65c5227a766; __ssnstarttime=1729657319; _lr_retry_request=true; criteria=sprefix%3D%252Fnewhomecommunities%26area_type%3Dcity%26city%3DWeston%26pg%3D1%26state_code%3DFL%26state_id%3DFL%26loc%3DWeston%252C%2520FL%26locSlug%3DWeston_FL%26county_fips%3D12011%26county_fips_multi%3D12011; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; kampyleUserSession=1729657321728; kampyleUserSessionsCount=8; kampyleSessionPageCounter=1; kampyleUserPercentile=16.957098653328995; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C20020%7CMCMID%7C74817516618400596614988662968578924832%7CMCAID%7CNONE%7CMCOPTOUT-1729664539s%7CNONE%7CvVersion%7C5.2.0',
    'dnt': '1',
    'origin': 'https://www.realtor.com',
    'priority': 'u=1, i',
    'rdc-ab-tests': 'commute_travel_time_variation:v1',
    'referer': 'https://www.realtor.com/realestateandhomes-search/Weston_FL',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

params = {
    'client_id': 'rdc-search-new-communities',
    'schema': 'vesta',
}

json_data = {
    'query': '\n  query TransformCommunitySearch($query: CommunitySearchCriteria!, $limit: Int) {\n    community_search(query: $query, limit: $limit) {\n      count\n      total\n      results {\n        source {\n          id\n        }\n        community_metrics {\n          leads_month_to_date\n        }\n        builder {\n          builder_id\n          href\n          name\n          source_builder_id\n          logo {\n            href\n          }\n        }\n        property_id\n        description {\n          name\n          baths_min\n          baths_max\n          beds_max\n          beds_min\n          sqft_max\n          sqft_min\n        }\n        location {\n          address {\n            city\n            state_code\n            postal_code\n          }\n        }\n        list_price_max\n        list_price_min\n        primary_photo(https:true) {\n          description\n          href\n        }\n        photos(limit: 5, https: true) {\n          href\n        }\n        permalink\n      }\n    }\n  }\n',
    'variables': {
        'query': {
            'sales_builder': True,
            'search_location': {
                'location': 'Weston, FL',
                'buffer': 20,
            },
        },
        'limit': 200,
    },
    'nrQueryType': 'PREMIUM_CARD_SRP',
    'isClient': True,
    'visitor_id': 'a4f46f97-818b-4eb3-be89-6ac10315dcbf',
}

response = requests.post(
    'https://www.realtor.com/api/v1/rdc_search_srp',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)


if response.status_code == 200:
    try:
        # Parse the JSON response
        data = response.json()

        # Function to recursively search for property_id
        def find_property_ids(obj):
            if isinstance(obj, dict):
                # If it's a dictionary, check each key-value pair
                for key, value in obj.items():
                    if key == 'property_id':
                        print(f"Property ID: {value}")
                    # Recursively call the function on the value
                    find_property_ids(value)
            elif isinstance(obj, list):
                # If it's a list, iterate over each item
                for item in obj:
                    find_property_ids(item)

        # Start the search from the root of the JSON data
        find_property_ids(data)
    
    except ValueError as e:
        print("Error parsing JSON:", e)

else:
    print(f"Request failed with status code {response.status_code}")