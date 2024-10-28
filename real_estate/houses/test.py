import requests

cookies = {
    'split': 'n',
    'split_tcv': '109',
    # Additional cookies here
}

headers = {
    'accept': 'application/json, text/javascript',
    'content-type': 'application/json',
    # Additional headers here
}

params = {
    'client_id': 'rdc-search-for-sale-search',
    'schema': 'vesta',
}

# Set initial offset to 0
offset = 0
limit = 42  # Number of properties per request
total = None  # Initialize total to None

while total is None or offset < total:
    # Update the request payload with the current offset and limit
    json_data = {
        'query': '\n  query ConsumerSearchQuery(\n    $query: HomeSearchCriteria!\n    $limit: Int\n    $offset: Int\n    $search_promotion: SearchPromotionInput\n    $sort: [SearchAPISort]\n    $sort_type: SearchSortType\n    $client_data: JSON\n    $bucket: SearchAPIBucket\n    $mortgage_params: MortgageParamsInput\n  ) {\n    home_search: home_search(\n      query: $query\n      sort: $sort\n      limit: $limit\n      offset: $offset\n      sort_type: $sort_type\n      client_data: $client_data\n      bucket: $bucket\n      search_promotion: $search_promotion\n      mortgage_params: $mortgage_params\n    ) {\n      count\n      total\n      properties: results {\n        property_id\n        list_price\n      }\n    }\n  }\n',
        'variables': {
            'geoSupportedSlug': 'Weston_FL',
            'query': {
                'primary': True,
                'status': ['for_sale', 'ready_to_build'],
                'search_location': {'location': 'Weston, FL'},
            },
            'client_data': {'device_data': {'device_type': 'desktop'}},
            'limit': limit,
            'offset': offset,  # Use the current offset
            'sort_type': 'relevant',
        },
        'isClient': True,
        'visitor_id': 'a4f46f97-818b-4eb3-be89-6ac10315dcbf',
        'operationName': 'ConsumerSearchQuery',
    }

    # Make the API request
    response = requests.post(
        'https://www.realtor.com/api/v1/rdc_search_srp',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Parse the response
    data = response.json()

    # Get total and count of the properties
    home_search = data.get('data', {}).get('home_search', {})
    total = home_search.get('total')
    count = home_search.get('count')
    properties = home_search.get('properties', [])

    # Process the properties or print them
    for property_data in properties:
        print(f"Property ID: {property_data['property_id']}, Price: {property_data['list_price']}")

    # Increment the offset for the next request
    offset += limit

    # Optional: stop the loop if there are no more results
    if not properties:
        break

# Print final result
print(f"Total properties available: {total}")