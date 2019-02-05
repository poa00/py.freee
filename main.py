import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

with open('targets.json', 'r') as f:
    targets_dict = json.load(f)

for target in targets_dict:
    print("==== Fetching datas from:", target['home_url'])
    s_html = urlopen(target['home_url']).read()
    soup_s = BeautifulSoup(s_html, "lxml")
    #s_title = soup_s.find(id='title-bar-title')
    print("Browsing:",soup_s.head.title.string)
    elems_to_find = target['elements']
    print("Searching for: [", len(elems_to_find), "] element(s)")
    for element in elems_to_find:
        if(element['action'] == "find_id"):
            elem_found = soup_s.find(id=element['identifier'])
            print("= Found ->", elem_found.string)
        elif(element['action'] == "find_all"):
            elems_found = soup_s.find_all(element['type'], {element['property']: element['identifier']})
            for e in elems_found:
                print("= Found ->", e.string)
