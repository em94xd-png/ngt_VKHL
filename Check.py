import os

theme_store = {}

def theme_files():
    global theme_store

    path_1 = os.path.dirname(os.path.abspath(__file__))
    path_2 = os.path.join(path_1, "themes")

    for _ in os.listdir(path_2):
        if _.endswith("json"):
            split_it = os.path.splitext(_)[0]
            path_full = os.path.join(path_2, _)
            theme_store[split_it] = path_full

theme_files()
print(theme_store)