index = []

def add_to_index(index,keyword,url):
    in_index = False
    record = []
    urls = []
    for entry in index:
        if keyword == entry[0]:
            in_index = True
            entry[1].append(url)
            return
    if not in_index:
        record.append(keyword)
        urls.append(url)
        record.append(urls)
        index.append(record)
    return index


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'computing','http://acmasees.org')
add_to_index(index,'udacity','http://npr.org')
print index
