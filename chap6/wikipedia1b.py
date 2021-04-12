import requests
import codecs
api_base_url = 'https://ja.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content' }
wiki_data = requests.get(api_base_url, params=api_params)
fo = codecs.open('C:\\Users\\USER\\Documents\\test_python_easy_sample\\chap6\\wiki1b.html', 'w', 'utf-8')
fo.write(wiki_data.text)
fo.close()