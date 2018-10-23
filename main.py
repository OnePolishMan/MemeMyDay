from controls import *

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen, urlretrieve


# create main window and add title to it
root = tk.Tk()
root.title("MemeMyDay")

frame = tk.Frame(root, width=300, height=400)
frame.pack(side='top', fill='both', expand=True)

# create scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# create a white canvas
cv = tk.Canvas(frame, bg='black')
cv.config(yscrollcommand=scrollbar.set)
cv.pack(side=tk.LEFT, fill='both', expand=True)
cv.config(scrollregion=cv.bbox("all"))

scrollbar.config(command=cv.yview)

set_start_point(cv, root)

# bind mouse click event to main window
cv.bind("<Button-1>",
          lambda event, _cv=cv, _root=root, _scrollbar=scrollbar: left_mouse_click(event, _cv, _root, _scrollbar))
cv.bind("<Button-3>",
          lambda event, _cv=cv, _root=root, _scrollbar=scrollbar: right_mouse_click(event, _cv, _root, _scrollbar))

root.bind("<Button-4>", lambda event, _cv=cv: on_mousewheel(event, _cv))
root.bind("<Button-5>", lambda event, _cv=cv: on_mousewheel(event, _cv))

root.mainloop()
