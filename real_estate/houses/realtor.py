import requests

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
    'AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg': '1',
    '_lr_retry_request': 'true',
    'kampylePageLoadedTimestamp': '1729662818256',
    'kampyleUserSession': '1729662933812',
    'kampyleUserSessionsCount': '14',
    'srchID': '27dcddf59b6a43349825a6ec1b65d260',
    'AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '-1124106680%7CMCIDTS%7C20020%7CMCMID%7C74817516618400596614988662968578924832%7CMCAID%7CNONE%7CMCOPTOUT-1729670142s%7CNONE%7CvVersion%7C5.2.0',
    'criteria': 'sprefix%3D%252Fnewhomecommunities%26area_type%3Dcity%26city%3DWeston%26pg%3D1%26state_code%3DFL%26state_id%3DFL%26loc%3DWeston%252C%2520FL%26locSlug%3DWeston_FL%26county_fips%3D12011%26county_fips_multi%3D12011',
    'kampyleSessionPageCounter': '2',
    'kampyleUserPercentile': '13.62950558086884',
}

headers = {
    'accept': 'application/json, text/javascript',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'split=n; split_tcv=109; __vst=a4f46f97-818b-4eb3-be89-6ac10315dcbf; __bot=false; __split=84; _lr_env_src_ats=false; G_ENABLED_IDPS=google; mdLogger=false; kampyle_userid=e221-5cc0-2168-c6f8-7d8e-4df6-9934-1424; __ssn=8e5a4236-c9f3-4700-b16d-a65c5227a766; __ssnstarttime=1729657319; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; _lr_retry_request=true; kampylePageLoadedTimestamp=1729662818256; kampyleUserSession=1729662933812; kampyleUserSessionsCount=14; srchID=27dcddf59b6a43349825a6ec1b65d260; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C20020%7CMCMID%7C74817516618400596614988662968578924832%7CMCAID%7CNONE%7CMCOPTOUT-1729670142s%7CNONE%7CvVersion%7C5.2.0; criteria=sprefix%3D%252Fnewhomecommunities%26area_type%3Dcity%26city%3DWeston%26pg%3D1%26state_code%3DFL%26state_id%3DFL%26loc%3DWeston%252C%2520FL%26locSlug%3DWeston_FL%26county_fips%3D12011%26county_fips_multi%3D12011; kampyleSessionPageCounter=2; kampyleUserPercentile=13.62950558086884',
    'dnt': '1',
    'origin': 'https://www.realtor.com',
    'priority': 'u=1, i',
    'rdc-ab-test-client': 'rdc-search-for-sale',
    'rdc-ab-tests': 'commute_travel_time_variation:v1',
    'referer': 'https://www.realtor.com/realestateandhomes-search/Weston_FL/pg-2',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

params = {
    'client_id': 'rdc-search-for-sale-search',
    'schema': 'vesta',
}

limit = 100

json_data = {
    'query': '\n  query ConsumerSearchQuery(\n    $query: HomeSearchCriteria!\n    $limit: Int\n    $offset: Int\n    $search_promotion: SearchPromotionInput\n    $sort: [SearchAPISort]\n    $sort_type: SearchSortType\n    $client_data: JSON\n    $bucket: SearchAPIBucket\n    $mortgage_params: MortgageParamsInput\n  ) {\n    home_search: home_search(\n      query: $query\n      sort: $sort\n      limit: $limit\n      offset: $offset\n      sort_type: $sort_type\n      client_data: $client_data\n      bucket: $bucket\n      search_promotion: $search_promotion\n      mortgage_params: $mortgage_params\n    ) {\n      count\n      total\n      search_promotion {\n        names\n        slots\n        promoted_properties {\n          id\n          from_other_page\n        }\n      }\n      mortgage_params {\n        interest_rate\n      }\n      properties: results {\n        property_id\n        list_price\n        search_promotions {\n          name\n          asset_id\n        }\n        primary_photo(https: true) {\n          href\n        }\n        rent_to_own {\n          right_to_purchase\n          rent\n        }\n        listing_id\n        matterport\n        virtual_tours {\n          href\n          type\n        }\n        status\n        products {\n          products\n          brand_name\n        }\n        source {\n          id\n          type\n          spec_id\n          plan_id\n          agents {\n            office_name\n          }\n        }\n        lead_attributes {\n          show_contact_an_agent\n          opcity_lead_attributes {\n            cashback_enabled\n            flip_the_market_enabled\n          }\n          lead_type\n          ready_connect_mortgage {\n            show_contact_a_lender\n            show_veterans_united\n          }\n        }\n        community {\n          description {\n            name\n          }\n          property_id\n          permalink\n          advertisers {\n            office {\n              hours\n              phones {\n                type\n                number\n                primary\n                trackable\n              }\n            }\n          }\n          promotions {\n            description\n            href\n            headline\n          }\n        }\n        permalink\n        price_reduced_amount\n        description {\n          name\n          beds\n          baths_consolidated\n          sqft\n          lot_sqft\n          baths_max\n          baths_min\n          beds_min\n          beds_max\n          sqft_min\n          sqft_max\n          type\n          sub_type\n          sold_price\n          sold_date\n        }\n        location {\n          street_view_url\n          address {\n            line\n            postal_code\n            state\n            state_code\n            city\n            coordinate {\n              lat\n              lon\n            }\n          }\n          county {\n            name\n            fips_code\n          }\n        }\n        open_houses {\n          start_date\n          end_date\n        }\n        branding {\n          type\n          name\n          photo\n        }\n        flags {\n          is_coming_soon\n          is_new_listing(days: 14)\n          is_price_reduced(days: 30)\n          is_foreclosure\n          is_new_construction\n          is_pending\n          is_contingent\n        }\n        list_date\n        photos(limit: 2, https: true) {\n          href\n        }\n        advertisers {\n          type\n          builder {\n            name\n            href\n            logo\n          }\n        }\n      }\n    }\n\n    commute_polygon: get_commute_polygon(query: $query) {\n      areas {\n        id\n        breakpoints {\n          width\n          height\n          zoom\n        }\n        radius\n        center {\n          lat\n          lng\n        }\n      }\n      boundary\n    }\n  }\n',
    'variables': {
        'geoSupportedSlug': 'Weston_FL',
        'query': {
            'primary': True,
            'status': [
                'for_sale',
                'ready_to_build',
            ],
            'search_location': {
                'location': 'Weston, FL',
            },
        },
        'client_data': {
            'device_data': {
                'device_type': 'desktop',
            },
        },
        'limit': 42,
        'offset': 42,
        'sort_type': 'relevant',
        'search_promotion': {
            'names': [
                'CITY',
            ],
            'slots': [],
            'promoted_properties': [
                [],
            ],
        },
    },
    'isClient': True,
    'visitor_id': 'a4f46f97-818b-4eb3-be89-6ac10315dcbf',
    'operationName': 'ConsumerSearchQuery',
}

response = requests.post(
    'https://www.realtor.com/api/v1/rdc_search_srp',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)


data = response.json()

# Navigate through the nested structure to get 'total'
total = data.get('data', {}).get('home_search', {}).get('total')
count = data.get('data', {}).get('home_search', {}).get('count')

# Print the result
print(f"The total is: {total}, and the count is {count}")

def fetch_all_properties():
    # Start with an empty list to collect all properties
    all_properties = []
    
    # Get the first response to determine total and count
    offset = 0
    limit = 42  # Use the initial limit
    total = None

    while True:
        # Update json_data for the current request
        new_json_data = json_data.copy()
        new_json_data['variables']['limit'] = limit
        new_json_data['variables']['offset'] = offset  # Update the offset for pagination

        # Make the request
        response = requests.post(
            'https://www.realtor.com/api/v1/rdc_search_srp',
            params=params,
            cookies=cookies,
            headers=headers,
            json=new_json_data,
        )

        data = response.json()
        
        # Check if data is present and extract properties
        home_search = data.get('data', {}).get('home_search', {})
        properties = home_search.get('properties', [])
        count = home_search.get('count', 0)
        total = home_search.get('total', 0)

        # Append the properties to the all_properties list
        all_properties.extend(properties)

        # Break the loop if we've fetched all properties
        if len(all_properties) >= total:
            break

        # Update the offset for the next request
        offset += limit

    return all_properties

# Fetch all properties
all_properties = fetch_all_properties()

# Print the total number of properties fetched
print(all_properties[0])
print(f"Total properties fetched: {len(all_properties)}")


