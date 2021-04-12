import requests, pprint
api_url = 'https://ja.wikipedia.org/w/api.php'
api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content' }
wiki_data = requests.get(api_url, params=api_params).json()
pprint.pprint(wiki_data)