from jbzdy_pl import get_img_urls, get_page_number
from img import Img

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen, urlretrieve

current_index = 0
img_list = []

cv_img = object

scrollable = False


def set_start_point(cv, root):
    global cv_img
    global img_list
    global scrollable

    img_urls = get_img_urls(0)
    for url in img_urls:
        img_list.append(Img(url))

    # put the image on the canvas with
    # create_image(xpos, ypos, image, anchor)
    cv_img = cv.create_image(10, 10, image=img_list[current_index].img, anchor='nw')

    x = 80
    y = 100
    w = img_list[current_index].img.width() + 35
    h = img_list[current_index].img.height() + 20

    if h > 700:
        h = 700
        scrollable = True
    else:
        scrollable = False

    # scale main window to fit image size'
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.title("Strona - " + str(get_page_number()))


def left_mouse_click(event, cv, root, scrollbar):
    global current_index
    global img_list
    global cv_img
    global scrollable

    if current_index == 0:
        if get_page_number() == 1:
            return
        img_list = []
        img_urls = get_img_urls(-1)
        for url in img_urls:
            img_list.append(Img(url))
        current_index = len(img_list)-1
        root.title("Strona - " + str(get_page_number()))
    else:
        current_index -= 1

    img = img_list[current_index].img

    cv.delete(cv_img)
    cv_img = cv.create_image(10, 10, image=img, anchor='nw')
    cv.config(yscrollcommand=scrollbar.set)
    cv.config(scrollregion=cv.bbox("all"))

    w = img_list[current_index].img.width() + 35
    h = img_list[current_index].img.height() + 20
    x = root.winfo_x()
    y = root.winfo_y()

    if h > 700:
        h = 700
        scrollable = True
    else:
        scrollable = False

    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


def right_mouse_click(event, cv, root, scrollbar):
    global current_index
    global img_list
    global cv_img
    global scrollable

    current_index += 1

    if current_index == len(img_list):
        img_list = []
        img_urls = get_img_urls(1)
        for url in img_urls:
            img_list.append(Img(url))
        current_index = 0
        root.title("Strona - " + str(get_page_number()))

    img = img_list[current_index].img

    cv.delete(cv_img)
    cv_img = cv.create_image(10, 10, image=img, anchor='nw')
    cv.config(yscrollcommand=scrollbar.set)
    cv.config(scrollregion=cv.bbox("all"))

    w = img_list[current_index].img.width() + 35
    h = img_list[current_index].img.height() + 20
    x = root.winfo_x()
    y = root.winfo_y()

    if h > 700:
        h = 700
        scrollable = True
    else:
        scrollable = False

    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


def on_mousewheel(event, cv):
    factor = 2

    if not scrollable:
        return

    if event.num == 4:
        cv.yview('scroll', -1 * factor, 'units')
    if event.num == 5:
        cv.yview('scroll', factor, 'units')
