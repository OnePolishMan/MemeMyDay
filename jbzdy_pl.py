import re

try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen, urlretrieve


# set first page at the beginning
page_number: int = 1

img_urls = []


def get_page_number():
    global page_number
    return page_number


def get_img_urls(direction):
    # get images from jbzdy.pl

    global page_number
    global img_urls

    if direction == 1:
        print("Loading more memes...!")
        page_number += 1
    elif direction == -1:
        if page_number > 1:
            print("Getting back...")
            page_number -= 1
        else:
            return img_urls
    elif direction == 0:
        print("Setting beginning state")

    img_urls = []

    website_url = "https://jbzdy.pl/strona/" + str(page_number)
    website_src = urlopen(website_url).read().decode('utf-8')

    pattern_global = "<img class=\"resource-image\" src=\".+\" alt=\".*\" />"
    pattern_url = "https://.+\.jpg"

    img_list_raw = re.findall(pattern_global, website_src)
    for raw in img_list_raw:
        url = re.findall(pattern_url, raw)
        for x in url:
            img_urls.append(x)

    return img_urls
