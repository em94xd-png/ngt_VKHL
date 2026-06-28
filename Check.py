import os

def theme_path():
    path_1 = os.path.dirname(os.path.abspath(__file__))
    path_2 = os.path.join(path_1, "themes")
    
    for _ in os.listdir(path_2):
        if _.endswith(".json"):
            theme_key = os.path.splitext(_)[0]
            theme_key_path = os.path.join(path_2, _)
            

theme_path()