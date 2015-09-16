index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    content_split = content.split()
    for word in content_split:
        add_to_index(index, word, url)
    return

add_page_to_index(index,'fake.text',"This is a test")
print index
