import requests, sys
import codecs
search_word = sys.argv[1]
api_base_url = 'https://ja.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content' }
api_params['titles'] = search_word
wiki_data = requests.get(api_base_url, params=api_params)
fo = codecs.open('C:\\Users\\USER\\Documents\\test_python_easy_sample\\chap6\\wiki2.html', 'w', 'utf-8')
fo.write(wiki_data.text)
fo.close()